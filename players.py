"""Tag You're It!

=== Module Description ===

This file contains classes that describe a Player object.
"""
from __future__ import annotations
import random
from typing import List, Tuple, Optional, Set
from trees import OutOfBoundsError


class Player:
    """ A Player that is a player in the field

   === Private Attributes ===
   _name:
        the name of the player
   _location:
        the location of the player
    _colour:
        the colour of the player
    _vision:
        the vision statistic of the player
    _speed:
        the speed statistic of the player
    _game:
        the game object the player is associated with
    _points:
        the points of the player
    _targets:
        a list representing players that self must target
    _enemies:
        a list representing players that self must avoid
    _direction:
        the direction self is currently moving in

   === Representation Invariants ===
   None
   """
    _name: str
    _location: Tuple[int, int]
    _colour: str
    _vision: int
    _speed: int
    _game: 'Game'
    _points: int
    _targets: List[str]
    _enemies: List[str]
    _direction: str

    def __init__(self, name: str, vision: int, speed: int, game: 'Game',
                 colour: str, location: Tuple[int, int]) -> None:
        """Initializes a new Player object with name <name>, vision <vision>,
        speed <speed>, colour <colour> and is located at <location> in the
        game object <game>

        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1._name
        'Parinita'
        """
        self._name = name
        self._location = location
        self._colour = colour
        self._vision = vision
        self._speed = speed
        self._game = game
        self._points = 0
        self._targets = []
        self._enemies = []
        self._direction = random.choice(['N', 'S', 'E', 'W'])

    def set_colour(self, colour: str) -> None:
        """ Change the colour of self

        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1.set_colour('green')
        >>> p1._colour
        'green'
        """
        self._colour = colour

    def increase_points(self, points: int) -> None:
        """ Increase <self>'s points by <points>

        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1.increase_points(1)
        >>> p1._points
        1
        """
        self._points += points

    def get_points(self) -> int:
        """ Return the number of points <self> currently has
        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1.increase_points(1)
        >>> p1.increase_points(5)
        >>> p1.increase_points(12)
        >>> p1.get_points()
        18
        """
        return self._points

    def select_target(self, name: str) -> None:
        """ Add a target to <self>'s target list

        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1._targets
        []
        >>> p1.select_target('Rohan')
        >>> p1.get_targets()
        ['Rohan']
        """
        if name not in self._targets and name not in self._enemies:
            self._targets.append(name)

    def ignore_target(self, name: str) -> None:
        """ Remove a target from <self>'s target list
        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1.select_target('Rohan')
        >>> p1.select_target('Grace')
        >>> p1.get_targets()
        ['Rohan', 'Grace']
        >>> p1.ignore_target('Rohan')
        >>> p1.get_targets()
        ['Grace']
        """
        self._targets.remove(name)

    def get_targets(self) -> List[str]:
        """ Return a copy of the list of target names
        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1.select_target('Rohan')
        >>> p1.select_target('Grace')
        >>> p1.get_targets()
        ['Rohan', 'Grace']
         """
        return self._targets[:]

    def select_enemy(self, name: str) -> None:
        """ Add an enemy to <self>'s target list
        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1._enemies
        []
        >>> p1.select_enemy('Rohan')
        >>> p1.get_enemies()
        ['Rohan']
        """
        if name not in self._enemies and name not in self._targets:
            self._enemies.append(name)

    def ignore_enemy(self, name: str) -> None:
        """ Remove an enemy from <self>'s enemy list
        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1.select_enemy('Rohan')
        >>> p1.select_enemy('Grace')
        >>> p1.get_enemies()
        ['Rohan', 'Grace']
        >>> p1.ignore_enemy('Rohan')
        >>> p1.get_enemies()
        ['Grace']
        """
        self._enemies.remove(name)

    def get_enemies(self) -> List[str]:
        """ Return a copy of the list of enemy names
        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1.select_enemy('Rohan')
        >>> p1.select_enemy('Grace')
        >>> p1.get_targets()
        ['Rohan', 'Grace']
        """
        return self._enemies[:]

    def reverse_direction(self) -> None:
        """ Update the direction so that <self> will move in the opposite
        direction

        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1._direction = 'N'
        >>> p1.reverse_direction()
        >>> p1._direction
        'S'
        """
        if self._direction == 'N':
            self._direction = 'S'
        elif self._direction == 'S':
            self._direction = 'N'
        elif self._direction == 'E':
            self._direction = 'W'
        elif self._direction == 'W':
            self._direction = 'E'

    def set_speed(self, speed: int) -> None:
        """ Update <self>'s speed to <speed>

        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1.set_speed(20)
        >>> p1._speed
        20
        """
        self._speed = speed

    def _num_targets_and_enemies(self, player_lst: List[str])\
            -> List[int, int]:
        """Return the number of targets and enemies based off of the names in
        <player_lst>

        >>> p1 = Player('Parinita', 2, 3, 'Game', 'purple', (20, 20))
        >>> p1.select_target('Rohan')
        >>> p1.select_enemy('Grace')
        >>> p1.select_enemy('Parimal')
        >>> p1._num_targets_and_enemies(['Grace', 'Rohan', 'Parimal'])
        [1, 2]
        """
        num_targets = 0
        num_enemies = 0

        for player in player_lst:
            if player in self._targets:
                num_targets += 1
            elif player in self._enemies:
                num_enemies += 1

        return [num_targets, num_enemies]

    def next_direction(self) -> Set[str]:
        """ Update the direction to move the next time self.move is called. This
        direction should be determined by the relative number of visible targets
        and enemies.

        Return a set of all equally good directions to move towards.

        This method should call the names_in_range Tree method exactly twice.

        This method should set self._direction to a subset of:
        ('N', 'S', 'E', 'W')
        """
        direction1, direction2 = random.sample(['NE', 'NW', 'SE', 'SW'], 2)

        lst1 = self._game.field.names_in_range(self._location, direction1,
                                               self._vision)
        lst2 = self._game.field.names_in_range(self._location, direction2,
                                               self._vision)

        # calculates the number of targets and enemies in direction1 and
        # direction2
        # direction 1 and direction 2 in {NW, NE, SW, SE}
        lst1_targets_enemies = self._num_targets_and_enemies(lst1)
        lst2_targets_enemies = self._num_targets_and_enemies(lst2)

        n_stats, s_stats, e_stats, w_stats = [0, 0], [0, 0], [0, 0], [0, 0]

        # calculates the number of targets and enemies in N, S, E, W

        n_stats, s_stats, e_stats, w_stats = _calculate_direction_stats(
            direction1, n_stats, s_stats, e_stats, w_stats,
            lst1_targets_enemies)

        n_stats, s_stats, e_stats, w_stats = _calculate_direction_stats(
            direction2, n_stats, s_stats, e_stats, w_stats,
            lst2_targets_enemies)

        # calculates the number of targets running towards and number of enemies
        # running away from if you pick a particular direction to run in
        # want the max num bc the direction_nums are calculates as:
        # # of targets running to + # of enemies running away from
        # Hence, bigger the number, better the chance as you're running towards
        # more targets and lesser enemies
        # Misha said to calculate this way so just do it
        poss_direc = {'N': n_stats[0] + s_stats[1],
                      'S': s_stats[0] + n_stats[1],
                      'E': e_stats[0] + w_stats[1],
                      'W': w_stats[0] + e_stats[1]}
        direction_to_go = [i for i, j in poss_direc.items()
                           if j == max(poss_direc.values())]

        if len(direction_to_go) == 1:
            self._direction = direction_to_go[0]
        else:
            self._direction = random.choice(direction_to_go)

        return set(direction_to_go)

    def move(self) -> None:
        """ Move <self> in the direction described by self._direction by the
        number of steps described by self._speed. Make sure to keep track of the
        updated location of self.

        If the movement would move self out of bounds, move self in the opposite
        direction instead. self should continue to move in this new direction
        until next_direction is called again.
        """
        try:
            self._location = self._game.field.move_point(self._location,
                                                         self._direction,
                                                         self._speed)
        except OutOfBoundsError:
            self.reverse_direction()


def _calculate_direction_stats(direction: str,
                               n_stats: List[int, int],
                               s_stats: List[int, int],
                               e_stats: List[int, int],
                               w_stats: List[int, int],
                               tar_ene: List[int, int]) -> \
                               Tuple[List, List, List, List]:
    """Calculates the direction stats based off of <direction> and updates
    <n_stats>, <s_stats>, <e_stats>, <w_stats> with <tar_ene>

    >>> _calculate_direction_stats('NE', [0, 0], [0, 0], [0, 0], [0, 0], [2, 1])
    ([2, 1], [0, 0], [2, 1], [0, 0])
    """
    targets = tar_ene[0]
    enemies = tar_ene[1]
    if direction == 'NE':
        n_stats[0] += targets
        n_stats[1] += enemies
        e_stats[0] += targets
        e_stats[1] += enemies

    elif direction == 'NW':
        n_stats[0] += targets
        n_stats[1] += enemies
        w_stats[0] += targets
        w_stats[1] += enemies
    elif direction == 'SE':
        s_stats[0] += targets
        s_stats[1] += enemies
        e_stats[0] += targets
        e_stats[1] += enemies
    elif direction == 'SW':
        s_stats[0] += targets
        s_stats[1] += enemies
        w_stats[0] += targets
        w_stats[1] += enemies

    return n_stats, s_stats, e_stats, w_stats


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(
        config={'extra-imports': ['typing', 'random', 'games', 'trees'],
                'disable': ['R0913', 'R0902', 'W0611', 'R1710', 'R1702']})
