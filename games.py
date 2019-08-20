"""Tag You're It!

=== Module Description ===

This file contains classes that describe a Game object.

As discussed in the handout, you may not change any of the public behaviour
(attributes, methods) given in the starter code, but you can definitely add
new functions, classes and methods to complete your work here.

"""
from __future__ import annotations
import random
from typing import Dict, Union, Optional
from players import Player
from trees import QuadTree, TwoDTree


class Game:
    """ A Game object representing the field. This is an abstract class and
    should not be instantiated directly.

   === Public Attributes ===
   field:
        type of field for the game. It can be either a QuadTree or a
        TwoDTree.

   === Representation Invariants ===
   None
    """
    field: Union[QuadTree, TwoDTree]

    def __init__(self, field: Union[QuadTree, TwoDTree]) -> None:
        """Initializes a game object with an empty <field>."""

        self.field = field

    def handle_collision(self, player1: str, player2: str) -> None:
        """ Perform some action when <player1> and <player2> collide """
        raise NotImplementedError

    def check_for_winner(self) -> Optional[str]:
        """ Return the name of the player or group of players that have
        won the game, or None if no player has won yet """
        raise NotImplementedError


class Tag(Game):
    """ A Tag Game object representing the field.

   === Private Attributes ===
   _players:
        a dictionary storing all the Player objects in the field.
    _it:
        the Player object that is 'it'.
    _duration:
        the duration of the game.

   === Representation Invariants ===
   None
   """
    _players: Dict[str, Player]
    _it: str
    _duration: int

    def __init__(self, n_players: int,
                 field: Union[QuadTree, TwoDTree],
                 duration: int,
                 max_speed: int,
                 max_vision: int) -> None:
        """Initializes a new Tag Game object with <n_players> players on a
        <field>. The duration of the game is <duration>. Each player has
        a maximum possible speed of <max_speed> and maximum possible vision of
        <max_vision>
        >>> tree = QuadTree((250, 250))
        >>> game = Tag(10, tree, 5, 3, 4)
        >>> len(game._players)
        10
        >>> all(name in game.field for name in game._players)
        True
        >>> game._it in game._players
        True
        >>> game._players[game._it]._colour
        'purple'
        """
        Game.__init__(self, field)
        self._duration = duration
        # self.field = field
        self._players = {}

        lst_x = []
        lst_y = []

        while len(lst_x) < n_players:
            random_x = random.randint(0, 500)
            random_y = random.randint(0, 500)

            if random_x not in lst_x or random_y not in lst_y:
                lst_x.append(random_x)
                lst_y.append(random_y)

        for i in range(n_players):
            new_player = Player(str(i), random.randint(0, max_vision),
                                random.randint(1, max_speed), self, 'green',
                                (lst_x[i], lst_y[i]))
            self._players[str(i)] = new_player
            self.field.insert(str(i), (lst_x[i], lst_y[i]))

        if len(self._players) > 0:
            random_player = random.choice(list(self._players.keys()))
            self._it = random_player
            self._players[random_player].set_colour('purple')

            for target in list(self._players.keys()):
                if target != self._it:
                    self._players[self._it].select_target(target)
                    self._players[target].select_enemy(self._it)

    def handle_collision(self, player1: str, player2: str) -> None:
        """ Perform some action when <player1> and <player2> collide.
        >>> tree = QuadTree((250, 250))
        >>> game = Tag(10, tree, 5, 3, 4)
        >>> it = game._it
        >>> it_points = game._players[it].get_points()
        >>> not_it = next(p for p in game._players if p != game._it)
        >>> game.handle_collision(it, not_it)
        >>> game._it == not_it
        True
        >>> it_points + 1 == game._players[game._it].get_points()
        True
        """
        self._players[player1].reverse_direction()
        self._players[player2].reverse_direction()

        if self._it == player1:
            # player1 is _it and tags player2
            self._it = player2
            self._players[player1].set_colour('green')
            self._players[player2].set_colour('purple')
            self._players[player2].increase_points(1)

            self._players[player1].ignore_target(player2)
            self._players[player1].select_enemy(player2)

            self._players[player2].ignore_enemy(player1)
            self._players[player2].select_target(player1)

        elif self._it == player2:
            # player2 is _it and tags player1
            self._it = player1
            self._players[player2].set_colour('green')
            self._players[player1].set_colour('purple')
            self._players[player1].increase_points(1)

            self._players[player2].ignore_target(player1)
            self._players[player2].select_enemy(player1)

            self._players[player1].ignore_enemy(player2)
            self._players[player1].select_target(player2)

    def check_for_winner(self) -> Optional[str]:
        """ Return the name of the player or group of players that have
        won the game, or None if no player has won yet

        >>> tree = QuadTree((250, 250))
        >>> game = Tag(2, tree, 5, 3, 4)
        >>> winner = next(p for p in game._players if p != game._it)
        >>> game.check_for_winner() == winner
        True
        """

        if len(self._players) > 2:

            delete = [k for k, v in self._players.items()
                      if k != self._it and v.get_points() > 0]
            for player in delete:
                del self._players[player]
                self.field.remove(player)

        elif len(self._players) == 2:
            # winner = [k for k in self._players.keys() if k != self._it]
            winner = [k for k in self._players if k != self._it]
            return winner[0]

        elif len(self._players) == 1:
            return list(self._players.keys())[0]

class ZombieTag(Game):
    """ A Tag Game object representing the field.

   === Private Attributes ===
   _humans:
        a dictionary storing all the human Player objects in the field.
    _zombies:
        a dictionary storing all the zombie Player objects in the field.
    _duration:
        the duration of the game.

   === Representation Invariants ===
   None
   """
    _humans: Dict[str, Player]
    _zombies: Dict[str, Player]
    _duration: int

    def __init__(self, n_players: int,
                 field_type: Union[QuadTree, TwoDTree],
                 duration: int,
                 max_speed: int,
                 max_vision: int) -> None:
        """Initializes a new ZombieTag Game objext with <n_players> humans and
        1 zombie at the start on a field <field_type>. This game has a duration
        <duration>. Each human has a maximum possible speed of <max_speed> and
        a maximum possible vision of <max_vision>.

        >>> tree = QuadTree((250, 250))
        >>> game = ZombieTag(10, tree, 5, 3, 4)
        >>> len(game._humans)
        10
        >>> all(name in game.field for name in game._zombies)
        True
        >>> all(name in game.field for name in game._humans)
        True
        >>> len(game._zombies.keys() & game._humans.keys())
        0
        >>> all(player._colour == 'green' for _, player in game._humans.items())
        True
        >>> len(game._zombies)
        1
        >>> game._zombies.popitem()[1]._colour
        'purple'
        """
        Game.__init__(self, field_type)
        self._duration = duration
        self._humans = {}
        self._zombies = {}

        lst_x = []
        lst_y = []

        while len(lst_x) < n_players + 1:
            random_x = random.randint(0, 500)
            random_y = random.randint(0, 500)

            if random_x not in lst_x or random_y not in lst_y:
                lst_x.append(random_x)
                lst_y.append(random_y)

        self._zombies['CS_POST'] = Player('CS_POST', max_vision, 1, self,
                                          'purple', (lst_x[-1], lst_y[-1]))
        self.field.insert('CS_POST', (lst_x[-1], lst_y[-1]))

        for i in range(n_players):
            new_player = Player(str(i), random.randint(0, max_vision),
                                random.randint(0, max_speed), self, 'green',
                                (lst_x[i], lst_y[i]))
            self._humans[str(i)] = new_player
            self.field.insert(str(i), (lst_x[i], lst_y[i]))

            self._humans[str(i)].select_enemy('CS_POST')
            self._zombies['CS_POST'].select_target(str(i))

    def handle_collision(self, player1: str, player2: str) -> None:
        """ Perform some action when <player1> and <player2> collide

        >>> tree = QuadTree((250, 250))
        >>> game = ZombieTag(10, tree, 5, 3, 4)
        >>> human = list(game._humans.values())[0]
        >>> zombie = list(game._zombies.values())[0]
        >>> game.handle_collision(human._name, zombie._name)
        >>> zombie._name in game._zombies
        True
        >>> human._name in game._zombies
        True
        >>> human._name not in game._humans
        True
        """

        if player1 in self._zombies and player2 in self._zombies:
            #both are zombies
            self._zombies[player1].reverse_direction()
            self._zombies[player2].reverse_direction()

        elif player1 in self._humans and player2 in self._humans:
            #both are humans
            self._humans[player1].reverse_direction()
            self._humans[player2].reverse_direction()

        else:
            if player1 in self._zombies:
                # player1 is zombie, #player2 is human
                self._zombies[player1].reverse_direction()
                self._humans[player2].reverse_direction()

                # update all zombie target lists to ignore player2
                for zombie in self._zombies:
                    self._zombies[zombie].ignore_target(player2)

                # change player2 to a zombie
                self._zombies[player2] = self._humans[player2]
                self._zombies[player2].set_speed(1)
                self._zombies[player2].set_colour('purple')
                del self._humans[player2]

                # tells the new player2 zombie who to target
                for target in self._zombies[player1].get_targets():
                    self._zombies[player2].select_target(target)

                # update all humans to avoid player2
                for human in self._humans:
                    self._humans[human].select_enemy(player2)

            elif player2 in self._zombies:
                # player2 is zombie, #player1 is human
                self._zombies[player2].reverse_direction()
                self._humans[player1].reverse_direction()

                # update all zombie target lists to ignore player1
                for zombie in self._zombies:
                    self._zombies[zombie].ignore_target(player1)

                # change player1 to a zombie
                self._zombies[player1] = self._humans[player1]
                self._zombies[player1].set_speed(1)
                self._zombies[player1].set_colour('purple')
                del self._humans[player1]

                # tells the new player1 zombie who to target
                for target in self._zombies[player2].get_targets():
                    self._zombies[player1].select_target(target)

                # update all humans to avoid player1
                for human in self._humans:
                    self._humans[human].select_enemy(player1)

    def check_for_winner(self) -> Optional[str]:
        """ Return the name of the player or group of players that have
        won the game, or None if no player has won yet

        >>> tree = QuadTree((250, 250))
        >>> game = ZombieTag(2, tree, 5, 3, 4)
        >>> game.check_for_winner()
        'humans'
        """
        if len(self._humans) > 0:
            return 'humans'
        else:
            return 'zombies'


class EliminationTag(Game):
    """ A Tag Game object representing the field.

   === Private Attributes ===
   _players:
        a dictionary storing all the Player objects in the field.

   === Representation Invariants ===
   None
   """

    _players: Dict[str, Player]

    def __init__(self, n_players: int,
                 field_type: Union[QuadTree, TwoDTree],
                 max_speed: int,
                 max_vision: int) -> None:
        """Intializes a new ElimnationTag Game object with <n_players> players
        on <field_type>. Each player has a maximum possible speed of <max_speed>
        and a maximum possible vision of <max_vision>.

        >>> tree = QuadTree((250, 250))
        >>> game = EliminationTag(10, tree, 3, 4)
        >>> len(game._players)
        10
        >>> all(name in game.field for name in game._players)
        True
        >>> items = game._players.items()
        >>> all(player._colour == 'random' for _, player in items)
        True
        """
        Game.__init__(self, field_type)
        self._players = {}

        lst_x = []
        lst_y = []

        while len(lst_x) < n_players:
            random_x = random.randint(0, 500)
            random_y = random.randint(0, 500)

            if random_x not in lst_x or random_y not in lst_y:
                lst_x.append(random_x)
                lst_y.append(random_y)

        player1 = Player('a', random.randint(0, max_vision),
                         random.randint(1, max_speed),
                         self, 'random', (lst_x[0], lst_y[0]))

        self.field.insert('a', (lst_x[0], lst_y[0]))
        self._players['a'] = player1

        for i in range(1, n_players, 1):
            name = (i+1)*'a'
            new_player = Player(name, random.randint(0, max_vision),
                                random.randint(1, max_speed),
                                self, 'random', (lst_x[i], lst_y[i]))
            self._players[name] = new_player
            self.field.insert(name, (lst_x[i], lst_y[i]))

            prev_name = i*'a'
            self._players[name].select_enemy(prev_name)
            self._players[prev_name].select_target(name)

        self._players[n_players*'a'].select_target('a')
        self._players['a'].select_enemy(n_players*'a')

    def handle_collision(self, player1: str, player2: str) -> None:
        """ Perform some action when <player1> and <player2> collide

        >>> tree = QuadTree((250, 250))
        >>> game = EliminationTag(10, tree, 3, 4)
        >>> player1 = list(game._players)[0]
        >>> player2 = game._players[player1].get_targets()[0]
        >>> p2targets = game._players[player2].get_targets()
        >>> points = game._players[player1].get_points()
        >>> game.handle_collision(player1, player2)
        >>> player1 in game._players
        True
        >>> player2 not in game._players
        True
        >>> game._players[player1].get_targets()[0] == p2targets[0]
        True
        >>> game._players[player1].get_points() - 1 == points
        True
        """
        if player1 not in self._players[player2].get_targets() and player2 not \
                in self._players[player1].get_targets():
            #neither players are in each others target lists
            self._players[player1].reverse_direction()
            self._players[player2].reverse_direction()

        elif player2 in self._players[player1].get_targets():
            # player1 is targeting player2
            player3 = self._players[player2].get_targets()[0]

            self._players[player1].ignore_target(player2)
            self._players[player1].select_target(player3)

            self._players[player3].ignore_enemy(player2)
            self._players[player3].select_enemy(player1)

            self.field.remove(player2)
            del self._players[player2]
            self._players[player1].increase_points(1)

        elif player1 in self._players[player2].get_targets():
            # player2 is targeting player1
            player3 = self._players[player1].get_targets()[0]

            self._players[player2].ignore_target(player1)
            self._players[player2].select_target(player3)

            self._players[player3].ignore_enemy(player1)
            self._players[player3].select_enemy(player2)

            self.field.remove(player1)
            del self._players[player1]
            self._players[player2].increase_points(1)

    def check_for_winner(self) -> Optional[str]:
        """ Return the name of the player or group of players that have
        won the game, or None if no player has won yet

        >>> tree = QuadTree((250, 250))
        >>> game = EliminationTag(10, tree, 3, 4)
        >>> player1 = list(game._players)[0]
        >>> game._players[player1].increase_points(1)
        >>> game.check_for_winner() == player1
        True
        """

        max_point = 0

        for player in self._players:
            temp_point = self._players[player].get_points()
            if temp_point > max_point:
                max_point = temp_point

        possible_winners = []
        for key in self._players:
            if self._players[key].get_points() == max_point:
                possible_winners.append(key)

        if len(possible_winners) == 1:
            return possible_winners[0]
        else:
            return None


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(
        config={'extra-imports': ['random', 'typing', 'players', 'trees'],
                'disable': ['R0913', 'R0902', 'W0611', 'R1710', 'R1702']})
