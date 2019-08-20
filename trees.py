"""CSC148 Assignment 1 - Tag You're It!

=== CSC148 Summer 2019 ===
Department of Computer Science,
University of Toronto

=== Module Description ===

This file contains classes that describe two tree data structures: QuadTree and
TwoDTree.

As discussed in the handout, you may not change any of the public behaviour
(attributes, methods) given in the starter code, but you can definitely add
new functions, classes and methods to complete your work here.

"""
from __future__ import annotations
from typing import Optional, List, Tuple, Dict


class OutOfBoundsError(Exception):
    """ Raises an OutOfBoundsError"""
    pass


class Tree:
    """ A Tree that stores data. This is an abstract class.

    === Private Attributes ===
    _name:
         the name of the player stored in the Tree
    _point:
         the point of the player stored in the Tree

    === Representation Invariants ===
    None
    """
    _name: Optional[str]
    _point: Optional[Tuple[int, int]]

    def __init__(self) -> None:
        """ Initializes a new Tree object."""

        self._name = None
        self._point = None

    def __contains__(self, name: str) -> bool:
        """ Return True if a player named <name> is stored in this tree.

        Runtime: O(n)

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (50, 40))
        >>> q1.__contains__('Parinita')
        True
        >>> q1.__contains__('Parimal')
        False
        """
        if self._name == name:
            return True

        _, kids = self._num_kids()
        for kid in kids:
            temp_find = kid.__contains__(name)
            if temp_find:
                return temp_find
        return False

    def _num_kids(self) -> Tuple[int, List]:
        """ Returns the number of children self has and a list containing the
        children of self

        Runtime: O(1)
        """
        raise NotImplementedError

    def contains_point(self, point: Tuple[int, int]) -> bool:
        """ Return True if a player at location <point> is stored in this tree.

        Runtime: O(log(n))
        """
        raise NotImplementedError

    def _find_name(self, name: str) -> Optional[Tuple[int, int]]:
        """ Finds and returns the point the player named <name> is in the tree.
        If the player doesn't exist, return None.

        Runtime: O(n)

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Rohan', (50, 40))
        >>> q1.insert('Parinita', (102, 130))
        >>> q1._find_name('Parinita')
        (102, 130)
        >>> q1._find_name('Grace')
        None
        """

        if self._name == name:
            return self._point

        _, kids = self._num_kids()
        for kid in kids:
            temp_find = kid._find_name(name)
            if temp_find:
                return temp_find
        return None

    def insert(self, name: str, point: Tuple[int, int]) -> None:
        """Insert a player named <name> into this tree at point <point>.

        Raise an OutOfBoundsError if <point> is out of bounds.

        Runtime: O(log(n))
        """
        raise NotImplementedError

    def remove(self, name: str) -> None:
        """ Remove information about a player named <name> from this tree.

        If there isn't a player with <name> in the tree, fail silently.

        Runtime: O(n)

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (35, 40))
        >>> q1.remove('Parinita')
        >>> q1.__contains__('Parinita')
        False
        """
        found_point = self._find_name(name)
        if found_point is not None:
            self.remove_point(found_point)

    def remove_point(self, point: Tuple[int, int]) -> None:
        """ Remove information about a player at point <point> from this tree.

        If there isn't a player at point <point> in the tree, fail silently.

        Runtime: O(log(n))
        """
        raise NotImplementedError

    def move(self, name: str, direction: str, steps: int) -> \
            Optional[Tuple[int, int]]:
        """ Return the new location of the player named <name> after moving it
        in the given <direction> by <steps> steps.

        If there isn't a player with <name> in the tree, fail silently.

        Raise an OutOfBoundsError if this would move the player named
        <name> out of bounds (before moving the player).

        Runtime: O(n)

        === precondition ===
        direction in ['N', 'S', 'E', 'W']

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (35, 40))
        >>> q1.move('Rohan', 'E', 10)
        >>> q1._find_name('Rohan')
        (170, 20)
        """
        found_point = self._find_name(name)
        if found_point is not None:
            new_loc = found_point
            if direction == 'N':
                new_loc = (new_loc[0], new_loc[1] - steps)
            elif direction == 'S':
                new_loc = (new_loc[0], new_loc[1] + steps)
            elif direction == 'E':
                new_loc = (new_loc[0] + steps, new_loc[1])
            elif direction == 'W':
                new_loc = (new_loc[0] - steps, new_loc[1])

            try:
                self.insert(name, new_loc)
                self.remove_point(found_point)
                return new_loc

            except OutOfBoundsError:
                raise OutOfBoundsError

    def _find_point(self, point: Tuple[int, int]) -> Optional[str]:
        """ Finds and returns the name of the player at point <point> in the
         tree. If the point doesn't exist, return None.

         Runtime: O(log(n))
         """
        raise NotImplementedError

    def move_point(self, point: Tuple[int, int], direction: str, steps: int) \
            -> Optional[Tuple[int, int]]:
        """ Return the new location of the player at point <point> after moving
        it in the given <direction> by <steps> steps.

        If there isn't a player at point <point> in the tree, fail silently.

        Raise an OutOfBoundsError if this would move the player at point
        <point> out of bounds (before moving the player).

        Moving a point may require the tree to be reorganized. This method
        should do the minimum amount of tree reorganization possible to move
        the given point properly.

        Runtime: O(log(n))

        === precondition ===
        direction in ['N', 'S', 'E', 'W']

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (35, 40))
        >>> q1.move_point((30, 40), 'S', 100)
        >>> q1._find_name('Parinita')
        (130, 40)

        """
        old_name = self._find_point(point)
        if old_name:
            new_loc = None
            if direction == 'N':
                new_loc = (point[0], point[1] - steps)
            elif direction == 'S':
                new_loc = (point[0], point[1] + steps)
            elif direction == 'E':
                new_loc = (point[0] + steps, point[1])
            elif direction == 'W':
                new_loc = (point[0] - steps, point[1])

            try:
                self.insert(old_name, new_loc)
                self.remove_point(point)
                return new_loc

            except OutOfBoundsError:
                raise OutOfBoundsError

    def _check_in_box(self, tl: Tuple[int, int], bl: Tuple[int, int],
                      tr: Tuple[int, int], br: Tuple[int, int]) -> bool:
        """Returns True if the point in self lies within the box created by
        <tl>, <bl>, <tr>, <br>.

         Runtime: O(1)

         >>> q1 = QuadTree((100, 100))
         >>> q1.insert('Parinita', (30, 40))
         >>> q1.insert('Rohan', (150, 20))
         >>> q1.insert('Grace', (35, 40))
         >>> q1._ne._check_in_box((145, 15), (145, 25), (155, 15), (155, 25))
         True
         """
        return tl[0] <= self._point[0] <= br[0] and \
               tr[1] <= self._point[1] <= bl[1]

    def _names_in_range_helper(self, tl: Tuple[int, int], bl: Tuple[int, int],
                               tr: Tuple[int, int],
                               br: Tuple[int, int]) -> List[str]:
        """Returns a list of player names that lie within the box created by
        <tl>, <bl>, <tr> and <br>

        Runtime: faster than O(n) when distance is small
        """
        raise NotImplementedError

    def names_in_range(self, point: Tuple[int, int], direction: str,
                       distance: int) -> List[str]:
        """ Return a list of names of players whose location is in the
        <direction>relative to <point> and whose location is within <distance>
        along both the x and y axis.

        For example: names_in_range((100, 100), 'SE', 10) should return the
        names of all the players south east of (100, 100) and within 10 steps in
        either direction. In other words, find all players whose location is in
        the box with corners at:(100, 100) (110, 100) (100, 110) (110, 110)

        Runtime: faster than O(n) when distance is small

        === precondition ===
        direction in ['NE', 'SE', 'NE', 'SW']

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (35, 40))
        >>> q1.names_in_range((20, 20), 'SE', 50)
        ['Parinita', 'Grace']
        """
        tl, bl, tr, br = _determine_corners(point, direction, distance)
        return self._names_in_range_helper(tl, bl, tr, br)

    def size(self) -> int:
        """ Return the number of nodes in <self>

        Runtime: O(n)
        """
        raise NotImplementedError

    def height(self) -> int:
        """ Return the height of <self>

        Height is measured as the number of nodes in the path from the root of
        this tree to the node at the greatest depth in this tree.

        Runtime: O(n)
        """
        raise NotImplementedError

    def _depth_helper(self, tree: Tree, depth: int) -> Optional[int]:
        """ Returns the depth of the subtree <tree> relative to self. Returns
        None if <tree> is not a descendant of <self>. This means that depth > 0
        for <tree> to be a descendant of <self>

        Runtime: O(log(n))
        """
        raise NotImplementedError

    def depth(self, tree: Tree) -> Optional[int]:
        """ Return the depth of the subtree <tree> relative to <self>. Return
        None if <tree> is not a descendant of <self>

        Runtime: O(log(n))

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (35, 40))
        >>> q1.depth(q1._ne)
        1
        """
        num = self._depth_helper(tree, 0)
        if num:
            if num > 0:
                return num
            else:
                return None
        return None

    def is_leaf(self) -> bool:
        """ Return True if <self> has no children

        Runtime: O(1)
        """
        raise NotImplementedError

    def is_empty(self) -> bool:
        """ Return True if <self> does not store any information about the
        location of any players.

        Runtime: O(1)

        >>> q1 = QuadTree((100, 100))
        >>> q1.is_empty()
        True
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.is_empty()
        False
        """
        return self._point is None and self.is_leaf() is True


def _determine_corners(point: Tuple[int, int], direction: str,
                       distance: int) -> Tuple[Tuple[int, int],
                                               Tuple[int, int],
                                               Tuple[int, int],
                                               Tuple[int, int]]:
    """Returns a tuple containing the corners of the box in which we need to
    check for players. The box is created by starting at point <point> and
    extending it into direction <direction> by <distance> steps.

    Precondition: direction in {'NE', 'NW', 'SE', 'SW'}

    Runtime: O(1)
    >>> _determine_corners((0, 0), 'SE', 10)
    ((0, 0), (0, 10), (10, 0), (10, 10))
    """
    top_left, bottom_left, top_right, bottom_right = (0, 0), (0, 0), \
                                                     (0, 0), (0, 0)

    if direction == 'NW':
        top_left = (point[0] - distance, point[1] - distance)
        bottom_left = (point[0] - distance, point[1])
        top_right = (point[0], point[1] - distance)
        bottom_right = point
    elif direction == 'SW':
        top_left = (point[0] - distance, point[1])
        bottom_left = (point[0] - distance, point[1] + distance)
        top_right = point
        bottom_right = (point[0], point[1] + distance)
    elif direction == 'NE':
        top_left = (point[0], point[1] - distance)
        bottom_left = point
        top_right = (point[0] + distance, point[1] - distance)
        bottom_right = (point[0] + distance, point[1])
    elif direction == 'SE':
        top_left = point
        bottom_left = (point[0], point[1] + distance)
        top_right = (point[0] + distance, point[1])
        bottom_right = (point[0] + distance, point[1] + distance)

    return top_left, bottom_left, top_right, bottom_right


class QuadTree(Tree):
    """ A QuadTree that stores data in a quad tree structure

    === Private Attributes ===
    _centre:
         the centre of the QuadTree
    _ne:
        the NE child of self
    _nw:
        the NW child of self
    _se:
        the SE child of self
    _sw:
        the SW child of self

    === Representation Invariants ===
    None
    """
    _centre: Tuple[int, int]
    _ne: Optional[QuadTree]
    _nw: Optional[QuadTree]
    _se: Optional[QuadTree]
    _sw: Optional[QuadTree]

    def __init__(self, centre: Tuple[int, int]) -> None:
        """Initialize a new Tree instance

        Runtime: O(1)

        >>> q1 = QuadTree((100, 100))
        >>> q1._centre
        (100, 100)
        """
        Tree.__init__(self)
        if centre[0] >= 0 and centre[1] >= 0:
            self._centre = (int(centre[0]//1), int(centre[1]//1))
        else:
            return

        self._ne = None
        self._nw = None
        self._se = None
        self._sw = None

    def contains_point(self, point: Tuple[int, int]) -> bool:
        """ Return True if a player at location <point> is stored in this tree.

        Runtime: O(log(n))

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (35, 40))
        >>> q1.contains_point((150, 20))
        True
        >>> q1.contains_point((0, 0))
        False
        """

        if self._point == point:
            return True

        if point[0] <= self._centre[0] and point[1] <= self._centre[1] and \
                self._nw:
            # go into _nw tree
            return self._nw.contains_point(point)

        elif point[0] <= self._centre[0] and point[1] > self._centre[1] and \
                self._sw:
            # go into _sw tree
            return self._sw.contains_point(point)

        elif point[0] > self._centre[0] and point[1] <= self._centre[1] and \
                self._ne:
            # go into _ne tree
            return self._ne.contains_point(point)

        elif point[0] > self._centre[0] and point[1] > self._centre[1] and \
                self._se:
            # go into _se tree
            return self._se.contains_point(point)

        else:
            return False

    def _create_new_subtree(self, direction: str, tl_corner: Tuple[int, int],
                            br_corner: Tuple[int, int],
                            point: Tuple[int, int], name: str) -> None:
        """ Creates a new subtree in the <direction> quadrant of self with
        point <point> and a player named <name>. <corner> helps in determining
        the new QuadTree's centre attribute

        Precondition: direction in {'ne', 'nw', 'se', 'sw'}

        >>> q1 = QuadTree((100, 100))
        >>> q1._create_new_subtree('nw', (0, 0), (100, 100), (30, 40), 'Rohan')
        >>> q1._create_new_subtree('ne', (100, 0), (200, 100), (130, 40), 'Bri')
        >>> q1._nw._point
        (30, 40)
        >>> q1._ne._point
        (130, 40)
        """
        if direction == 'nw':
            x_temp = int((self._centre[0] + tl_corner[0]) / 2)
            y_temp = int((self._centre[1] + tl_corner[1]) / 2)
            self._nw = QuadTree((x_temp, y_temp))
            self._nw._point = point
            self._nw._name = name
        elif direction == 'ne':
            ne_corner = (br_corner[0], tl_corner[1])

            x_temp = int((self._centre[0] + ne_corner[0]) / 2)
            y_temp = int((self._centre[1] + ne_corner[1]) / 2)
            self._ne = QuadTree((x_temp, y_temp))
            self._ne._point = point
            self._ne._name = name
        elif direction == 'sw':
            sw_corner = (tl_corner[0], br_corner[1])

            x_temp = int((self._centre[0] + sw_corner[0]) / 2)
            y_temp = int((self._centre[1] + sw_corner[1]) / 2)
            self._sw = QuadTree((x_temp, y_temp))
            self._sw._point = point
            self._sw._name = name
        elif direction == 'se':

            x_temp = int((self._centre[0] + br_corner[0]) / 2)
            y_temp = int((self._centre[1] + br_corner[1]) / 2)
            self._se = QuadTree((x_temp, y_temp))
            self._se._point = point
            self._se._name = name

    def _insert_helper(self, name: str, point: Tuple[int, int],
                       tl_corner: Tuple[int, int],
                       br_corner: Tuple[int, int]) -> None:
        """ Inserts a player named <name> in this tree at point <point>
        <corner> describes the top left corner of the current rectangle

        Raise an OutOfBoundsError if <point> already exists in the tree.

        Runtime: O(log(n))

        >>> q1 = QuadTree((100, 100))
        >>> q1._insert_helper('Parinita', (30, 40), (0, 0), (200, 200))
        >>> q1._point
        (30, 40)
        >>> q1._name
        'Parinita'
        """

        # if self.is_empty():
        if self._point is None:
            if self.is_leaf():
                self._point = point
                self._name = name
            else:
                if point[0] <= self._centre[0] and point[1] <= self._centre[1]:
                    # go into _nw tree
                    if self._nw:
                        temp_tl_corner = tl_corner
                        temp_br_corner = self._centre

                        self._nw._insert_helper(name, point, temp_tl_corner,
                                                temp_br_corner)
                    else:
                        # fixme
                        self._create_new_subtree('nw', tl_corner, br_corner,
                                                 point, name)

                elif point[0] <= self._centre[0] and point[1] > self._centre[1]:
                    # go into _sw tree
                    if self._sw:
                        temp_tl_corner = (tl_corner[0], self._centre[1])
                        temp_br_corner = (self._centre[0], br_corner[1])
                        self._sw._insert_helper(name, point, temp_tl_corner,
                                                temp_br_corner)
                    else:
                        # fixme
                        self._create_new_subtree('sw', tl_corner, br_corner,
                                                 point, name)

                elif point[0] > self._centre[0] and point[1] <= self._centre[1]:
                    # go into _ne tree
                    if self._ne:
                        temp_tl_corner = (self._centre[0], tl_corner[1])
                        temp_br_corner = (br_corner[0], self._centre[1])
                        self._ne._insert_helper(name, point, temp_tl_corner,
                                                temp_br_corner)
                    else:
                        # fixme
                        self._create_new_subtree('ne', tl_corner, br_corner,
                                                 point, name)

                elif point[0] > self._centre[0] and point[1] > self._centre[1]:
                    # go into _se tree
                    if self._se:
                        temp_tl_corner = self._centre
                        temp_br_corner = br_corner
                        self._se._insert_helper(name, point, temp_tl_corner,
                                                temp_br_corner)
                    else:
                        # fixme
                        self._create_new_subtree('se', tl_corner, br_corner,
                                                 point, name)
        # fixme
        else:
            if self._point == point:
                raise OutOfBoundsError
            self._point, temp_point = None, self._point
            self._name, temp_name = None, self._name

            if temp_point[0] <= self._centre[0] and temp_point[1] <= \
                    self._centre[1]:
                # go into _nw tree
                self._create_new_subtree('nw', tl_corner, br_corner, temp_point,
                                         temp_name)

            elif temp_point[0] <= self._centre[0] and temp_point[1] > \
                    self._centre[1]:
                # go into _sw tree
                self._create_new_subtree('sw', tl_corner, br_corner, temp_point,
                                         temp_name)

            elif temp_point[0] > self._centre[0] and temp_point[1] <= \
                    self._centre[1]:
                # go into _ne tree
                self._create_new_subtree('ne', tl_corner, br_corner, temp_point,
                                         temp_name)

            elif temp_point[0] > self._centre[0] and temp_point[1] > \
                    self._centre[1]:
                # go into _se tree
                self._create_new_subtree('se', tl_corner, br_corner, temp_point,
                                         temp_name)

            self._insert_helper(name, point, tl_corner, br_corner)

    def insert(self, name: str, point: Tuple[int, int]) -> None:
        """Insert a player named <name> into this tree at point <point>.

        Raise an OutOfBoundsError if <point> is out of bounds.
        Runtime: O(log(n))

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1._point
        (30, 40)
        >>> q1._name
        'Parinita'
        """
        if point[0] > 2 * self._centre[0] or point[1] > 2 * self._centre[1] or \
                point[0] < 0 or point[1] < 0:
            raise OutOfBoundsError
        else:
            self._insert_helper(name, point, (0, 0),
                                (2 * self._centre[0], 2 * self._centre[1]))

    def _find_point(self, point: Tuple[int, int]) -> Optional[str]:
        """ Finds and returns the name of the player at point <point> in the
         tree. If the point doesn't exist, return None.

         Runtime: O(log(n))

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (35, 40))
        >>> q1._find_point((35, 40))
        'Grace'
        >>> q1._find_point((0, 0))
        None
         """

        if self._point == point:
            return self._name

        if point[0] <= self._centre[0] and point[1] <= self._centre[1]:
            # go into _nw tree
            if self._nw:
                return self._nw._find_point(point)

        elif point[0] <= self._centre[0] and point[1] > self._centre[1]:
            # go into _sw tree
            if self._sw:
                return self._sw._find_point(point)

        elif point[0] > self._centre[0] and point[1] <= self._centre[1]:
            # go into _ne tree
            if self._ne:
                return self._ne._find_point(point)

        elif point[0] > self._centre[0] and point[1] > self._centre[1]:
            # go into _se tree
            if self._se:
                return self._se._find_point(point)

    def _num_kids(self) -> Tuple[int, List]:
        """ Returns the number of children self has and a list containing the
        children of self

        Runtime: O(1)

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (35, 40))
        >>> q1._num_kids()
        (2, [q1._nw, q1._ne])
        """
        count = 0
        kids = []
        if self._nw:
            count += 1
            kids.append(self._nw)
        if self._ne:
            count += 1
            kids.append(self._ne)
        if self._sw:
            count += 1
            kids.append(self._sw)
        if self._se:
            count += 1
            kids.append(self._se)
        return count, kids

    def _promote_leaf(self) -> None:
        """ Determines if a leaf must be promoted up in the case where it is
        no longer needed to differentiate between nodes as there's only one node
        left after removing a node.

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1._nw = None
        >>> q1._promote_leaf()
        >>> q1._point
        (150, 20)
        >>> q1._name
        'Rohan'
        """
        num, kids = self._num_kids()
        if num == 1:
            if kids[0].is_leaf():
                self._point = kids[0]._point
                self._name = kids[0]._name
                self._nw = None
                self._ne = None
                self._sw = None
                self._se = None

    def remove_point(self, point: Tuple[int, int]) -> None:
        """ Remove information about a player at point <point> from this tree.

        If there isn't a player at point <point> in the tree, fail silently.

        Runtime: O(log(n))

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.remove_point((30, 40))
        >>> q1.contains_point((30, 40))
        False
        """
        if self._point == point:
            self._point = None
            self._name = None
        else:
            if point[0] <= self._centre[0] and point[1] <= self._centre[1]:
                # go into _nw tree
                if self._nw:
                    if self._nw._point == point:
                        self._nw = None
                        self._promote_leaf()
                    else:
                        self._nw.remove_point(point)
                        self._promote_leaf()

            elif point[0] <= self._centre[0] and point[1] > self._centre[1]:
                # go into _sw tree
                if self._sw:
                    if self._sw._point == point:
                        self._sw = None
                        self._promote_leaf()

                    else:
                        self._sw.remove_point(point)
                        self._promote_leaf()

            elif point[0] > self._centre[0] and point[1] <= self._centre[1]:
                # go into _ne tree
                if self._ne:
                    if self._ne._point == point:
                        self._ne = None
                        self._promote_leaf()
                    else:
                        self._ne.remove_point(point)
                        self._promote_leaf()

            elif point[0] > self._centre[0] and point[1] > self._centre[1]:
                # go into _se tree
                if self._se:
                    if self._se._point == point:
                        self._se = None
                        self._promote_leaf()
                    else:
                        self._se.remove_point(point)
                        self._promote_leaf()

    def _names_in_range_helper(self, tl: Tuple[int, int], bl: Tuple[int, int],
                               tr: Tuple[int, int], br: Tuple[int, int]) \
            -> List[str]:
        """Returns a list of player names that lie within the box created by
        <tl>, <bl>, <tr> and <br>

        Runtime: faster than O(n) when distance is small

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1._names_in_range_helper((0, 0), (0, 100), (100, 0), (100, 100))
        ['Parinita']
        """
        if self.is_leaf():
            if self._check_in_box(tl, bl, tr, br):
                return [self._name]
            else:
                return []
        else:
            #need to check which all quadrants the corners are in
            player_lst = []
            box_corners = [tl, bl, tr, br]
            in_subtrees = []
            for corner in box_corners:
                in_tree = None
                if corner[0] <= self._centre[0] and \
                        corner[1] <= self._centre[1] and self._nw:
                    # go into _nw tree
                    in_tree = self._nw

                elif corner[0] <= self._centre[0] and \
                        corner[1] > self._centre[1] and self._sw:
                    # go into _sw tree
                    in_tree = self._sw

                elif corner[0] > self._centre[0] and \
                        corner[1] <= self._centre[1] and self._ne:
                    # go into _ne tree
                    in_tree = self._ne

                elif corner[0] > self._centre[0] and \
                        corner[1] > self._centre[1] and self._se:
                    # go into _se tree
                    in_tree = self._se

                if in_tree not in in_subtrees and in_tree is not None:
                    in_subtrees.append(in_tree)

            for subtree in in_subtrees:
                player_lst.extend(subtree._names_in_range_helper(tl, bl, tr, br)
                                  )

            return player_lst

    def size(self) -> int:
        """ Return the number of nodes in <self>

        Runtime: O(n)

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (20, 120))
        >>> q1.size()
        4

        """
        count = 1
        if self._ne is not None:
            count += self._ne.size()

        if self._nw is not None:
            count += self._nw.size()

        if self._se is not None:
            count += self._se.size()

        if self._sw is not None:
            count += self._sw.size()

        return count

    def height(self) -> int:
        """ Return the height of <self>

        Height is measured as the number of nodes in the path from the root of
        this tree to the node at the greatest depth in this tree.

        Runtime: O(n)

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (20, 120))
        >>> q1.height()
        2
        """
        total_height = 1

        ne_h = 0
        nw_h = 0
        se_h = 0
        sw_h = 0
        if self._ne is not None:
            ne_h += self._ne.height()

        if self._nw is not None:
            nw_h += self._nw.height()

        if self._se is not None:
            se_h += self._se.height()

        if self._sw is not None:
            sw_h += self._sw.height()

        max_h = max(ne_h, nw_h, se_h, sw_h)
        return total_height + max_h

    def _depth_helper(self, tree: Tree, depth: int) -> Optional[int]:
        """ Returns the depth of the subtree <tree> relative to self. Returns
        None if <tree> is not a descendant of <self>. This means that depth > 0
        for <tree> to be a descendant of <self>

        Runtime: O(log(n))

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.insert('Rohan', (150, 20))
        >>> q1.insert('Grace', (20, 120))
        >>> q1._depth_helper(q1._ne, 0)
        1
        """
        if self._point == tree._point:
            if self is tree:
                return depth
            else:
                return None
        else:
            if tree._point[0] <= self._centre[0] and \
                    tree._point[1] <= self._centre[1] and self._nw:
                # go into _nw tree
                return self._nw._depth_helper(tree, depth + 1)

            elif tree._point[0] <= self._centre[0] and \
                    tree._point[1] > self._centre[1] and self._sw:
                # go into _sw tree
                return self._sw._depth_helper(tree, depth + 1)

            elif tree._point[0] > self._centre[0] and \
                    tree._point[1] <= self._centre[1] and self._ne:
                # go into _ne tree
                return self._ne._depth_helper(tree, depth + 1)

            elif tree._point[0] > self._centre[0] and \
                    tree._point[1] > self._centre[1] and self._se:
                # go into _se tree
                return self._se._depth_helper(tree, depth + 1)
            else:
                return None

    def is_leaf(self) -> bool:
        """ Return True if <self> has no children

        Runtime: O(1)

        >>> q1 = QuadTree((100, 100))
        >>> q1.insert('Parinita', (30, 40))
        >>> q1.is_leaf()
        True
        """
        return self._ne is None and self._nw is None and self._se is None and \
               self._sw is None

# TODO *************************************************************************


class TwoDTree(Tree):
    """ A TwoDTree that stores data in a 2D tree structure

    === Private Attributes ===
    _name:
         the name of the player stored in the TwoDTree
    _point:
         the point of the player stored in the TwoDTree
    _nw:
        the north-west corner of the boundary
    _se:
        the south-east corner of the boundary
    _lt:
        the LT child of self. If the x/y coordinate is less than or
        equal to the self._point, the new point goes into the LT child
        of self.
    _gt:
        the GT child of self. If the x/y coordinate is greater than the
        self._point, the new point goes into the GT child of self.
    _split_type:
        the split type of self. If self if the root node, then its split
        type is always 'x'. Else self's split type depends on that of
        its parent.
    === Representation Invariants ===
    None
    """
    _nw: Optional[Tuple[int, int]]
    _se: Optional[Tuple[int, int]]
    _lt: Optional[TwoDTree]
    _gt: Optional[TwoDTree]
    _split_type: str

    def __init__(self, nw: Optional[Tuple[int, int]] = None,
                 se: Optional[Tuple[int, int]] = None) -> None:
        """Initialize a new Tree instance

        Runtime: O(1)

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1._nw
        (0, 0)
        >>> d1._se
        (200, 200)
        """
        Tree.__init__(self)
        self._nw = nw
        self._se = se
        self._lt = None
        self._gt = None
        self._split_type = 'x'

    def _split_type_num(self) -> int:
        """ Returns an integer representation of self._split_type. Return 0 if
        self._split_type == 'x' and return 1 if self._split_type == 'y'.

        Runtime: O(1)

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1._split_type_num()
        0
        >>> d1._split_type = 'y'
        >>> d1._split_type_num()
        1
        """
        if self._split_type == 'x':
            return 0
        elif self._split_type == 'y':
            return 1

    def _num_kids(self) -> Tuple[int, List]:
        """ Returns the number of children self has and a list containing the
        children of self

        Runtime: O(1)

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1._num_kids()
        (2, [d1._lt, d1._gt])
        """
        count = 0
        kids = []
        if self._lt:
            count += 1
            kids.append(self._lt)
        if self._gt:
            count += 1
            kids.append(self._gt)
        return count, kids

    def contains_point(self, point: Tuple[int, int]) -> bool:
        """ Return True if a player at location <point> is stored in this tree.

        Runtime: O(log(n))

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1.contains_point((50, 50))
        True
        >>> d1.contains_point((0, 0))
        False
        """
        if self._point == point:
            return True

        num = self._split_type_num()

        if point[num] <= self._point[num] and self._lt:
            # go into lt
            return self._lt.contains_point(point)
        elif point[num] > self._point[num] and self._gt:
            # go into gt
            return self._gt.contains_point(point)
        else:
            return False

    def _create_new_subtree(self, point: Optional[Tuple[int, int]] = None,
                            name: Optional[str] = None) -> TwoDTree:
        """ Creates a new subtree in the <direction> quadrant of self with
        point <point> and a player named <name>. <corner> helps in determining
        the new QuadTree's centre attribute

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1._create_new_subtree((50, 50), 'Parinita')
        >>> d1._lt._point
        (50, 50)
        >>> d1._lt._name
        'Parinita'
        >>> d1._lt._split_type
        'y'
        """
        new_tree = TwoDTree()
        new_tree._point = point
        new_tree._name = name

        if self._split_type == 'x':
            new_tree._split_type = 'y'
        elif self._split_type == 'y':
            new_tree._split_type = 'x'

        return new_tree

    def _insert_helper(self, name: str, point: Tuple[int, int]) -> None:
        """ Inserts a player named <name> in this tree at point <point>
        <corner> describes the top left corner of the current rectangle

        Raise an OutOfBoundsError if <point> already exists in the tree.

        Runtime: O(log(n))

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1._insert_helper('Rohan', (100, 100))
        >>> d1._point
        (100, 100)
        >>> d1._name
        'Rohan'
        """
        if self._point is None:
            self._point = point
            self._name = name
        else:
            if self._point == point:
                raise OutOfBoundsError
            num = self._split_type_num()

            if point[num] <= self._point[num]:
                # go into lt
                if self._lt is None:
                    # make a new subtree
                    self._lt = self._create_new_subtree(point, name)
                else:
                    self._lt._insert_helper(name, point)

            elif point[num] > self._point[num]:
                # go into gt
                if self._gt is None:
                    # make a new subtree
                    self._gt = self._create_new_subtree(point, name)
                else:
                    self._gt._insert_helper(name, point)

    def insert(self, name: str, point: Tuple[int, int]) -> None:
        """Insert a player named <name> into this tree at point <point>.

        Raise an OutOfBoundsError if <point> is out of bounds.

        Runtime: O(log(n))

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1._point
        (100, 100)
        >>> d1._name
        'Rohan
        """
        if point[0] < self._nw[0] or point[0] > self._se[0] or \
                point[1] < self._nw[1] or point[1] > self._se[1]:
            raise OutOfBoundsError
        self._insert_helper(name, point)

    def _find_point(self, point: Tuple[int, int]) -> Optional[str]:
        """ Finds and returns the name of the player at point <point> in the
         tree. If the point doesn't exist, return None.

         Runtime: O(log(n))

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1._find_point((150, 150))
        'Grace'
        >>> d1._find_point((0, 0))
        None
        """

        if self._point == point:
            return self._name

        num = self._split_type_num()

        if point[num] <= self._point[num]:
            # go into _lt tree
            if self._lt:
                return self._lt._find_point(point)

        elif point[num] > self._point[num]:
            # go into _gt tree
            if self._gt:
                return self._gt._find_point(point)

    def _find_largest_node_value(self, orientation: int) -> \
            Tuple[str, Tuple[int, int]]:
        """ Return the node with the largest <orientation> value in self.

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1._find_largest_node_value(0)
        ('Grace', (150, 150))
        """

        if self.is_leaf():
            return self._name, self._point

        largest_point = self._point
        largest_point_name = self._name

        if self._split_type_num() == orientation:
            if self._gt:
                largest_point_name, largest_point = \
                    self._gt._find_largest_node_value(orientation)
            # return largest_point_name, largest_point

        else:
            if self._gt:
                gt_name, gt_point = self._gt._find_largest_node_value(
                    orientation)

            if self._lt:
                lt_name, lt_point = self._lt._find_largest_node_value(
                    orientation)

            if self._gt and self._lt:
                if gt_point[orientation] > lt_point[orientation]:
                    larger_point = gt_point
                    larger_name = gt_name
                else:
                    larger_point = lt_point
                    larger_name = lt_name

            elif self._gt:
                larger_point = gt_point
                larger_name = gt_name
            elif self._lt:
                larger_point = lt_point
                larger_name = lt_name

            if larger_point[orientation] > largest_point[orientation]:
                largest_point = larger_point
                largest_point_name = larger_name

        return largest_point_name, largest_point

    def _remove_point_helper(self, point: Tuple[int, int],
                             parent: Optional[TwoDTree]) -> None:
        """ Remove information about a player at point <point> from this tree.

        If there isn't a player at point <point> in the tree, fail silently.

        Runtime: O(log(n))

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1._remove_point_helper((150, 150), None)
        >>> d1.__contains__('Grace')
        False
        """
        if self._point == point:
            if self.is_leaf():
                # parent not None --> sever link to self
                # parent is None --> empty self bc root node
                if parent is not None:
                    num = parent._split_type_num()
                    if self._point[num] <= parent._point[num]:
                        parent._lt = None
                    elif self._point[num] > parent._point[num]:
                        parent._gt = None
                else:
                    self._point = None
                    self._name = None
            elif self._lt is not None:
                # need to get the point with the largest x/y value in self._lt

                largest_name, largest_point = self._lt._find_largest_node_value(
                    self._split_type_num())
                self._point = largest_point
                self._name = largest_name
                self._lt._remove_point_helper(largest_point, self)

            elif self._gt is not None:
                # need to switch self._gt to self._lt and search for the point
                # with the largest x/y value
                self._lt, self._gt = self._gt, None

                largest_name, largest_point = self._lt._find_largest_node_value(
                    self._split_type_num())
                self._point = largest_point
                self._name = largest_name
                self._lt._remove_point_helper(largest_point, self)

        else:
            num = self._split_type_num()

            if point[num] <= self._point[num] and self._lt:
                # go into lt
                self._lt._remove_point_helper(point, self)
            elif point[num] > self._point[num] and self._gt:
                # go into gt
                self._gt._remove_point_helper(point, self)

    def remove_point(self, point: Tuple[int, int]) -> None:
        """ Remove information about a player at point <point> from this tree.

        If there isn't a player at point <point> in the tree, fail silently.

        Runtime: O(log(n))

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1.remove_point((50, 50))
        >>> d1.__contains__('Parinita')
        False
        """
        self._remove_point_helper(point, None)

    def _names_in_range_helper(self, tl: Tuple[int, int], bl: Tuple[int, int],
                               tr: Tuple[int, int], br: Tuple[int, int]) \
            -> List[str]:
        """Returns a list of player names that lie within the box created by
        <tl>, <bl>, <tr> and <br>

        Runtime: faster than O(n) when distance is small

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1._names_in_range_helper((40, 40), (40, 60), (60, 40), (60, 60))
        ['Parinita']
        """
        if self.is_leaf():
            if self._check_in_box(tl, bl, tr, br):
                return [self._name]
            else:
                return []
        else:
            #need to check which all quadrants the corners are in
            player_lst = []
            box_corners = [tl, bl, tr, br]
            in_subtrees = []

            num = self._split_type_num()

            for corner in box_corners:
                in_tree = None
                if corner[num] <= self._point[num] and self._lt:
                    # go into _lt tree
                    in_tree = self._lt

                elif corner[num] > self._point[num] and self._gt:
                    # go into _gt tree
                    in_tree = self._gt

                if in_tree not in in_subtrees and in_tree is not None:
                    in_subtrees.append(in_tree)

            if self._check_in_box(tl, bl, tr, br):
                player_lst.append(self._name)

            for subtree in in_subtrees:
                player_lst.extend(subtree._names_in_range_helper(tl, bl, tr, br)
                                  )

            return player_lst

    def size(self) -> int:
        """ Return the number of nodes in <self>

        Runtime: O(n)

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1.size()
        3
        """
        count = 1
        if self._lt is not None:
            count += self._lt.size()

        if self._gt is not None:
            count += self._gt.size()

        return count

    def height(self) -> int:
        """ Return the height of <self>

        Height is measured as the number of nodes in the path from the root of
        this tree to the node at the greatest depth in this tree.

        Runtime: O(n)

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1.insert('Parimal', (75, 75))
        >>> d1.height()
        3
        """
        total_height = 1

        lt_h = 0
        gt_h = 0
        if self._lt is not None:
            lt_h += self._lt.height()

        if self._gt is not None:
            gt_h += self._gt.height()

        max_h = max(lt_h, gt_h)
        return total_height + max_h

    def _depth_helper(self, tree: Tree, depth: int) -> Optional[int]:
        """ Returns the depth of the subtree <tree> relative to self. Returns
        None if <tree> is not a descendant of <self>. This means that depth > 0
        for <tree> to be a descendant of <self>

        Runtime: O(log(n))

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1.insert('Parimal', (75, 75))
        >>> d1._depth_helper(d1._lt._gt, 0)
        2
        """
        if self._point == tree._point:
            if self is tree:
                return depth
            else:
                return None
        else:
            num = self._split_type_num()

            if tree._point[num] <= self._point[num] and self._lt:
                # go into _lt tree
                return self._lt._depth_helper(tree, depth + 1)

            elif tree._point[num] > self._point[num] and self._gt:
                # go into _gt tree
                return self._gt._depth_helper(tree, depth + 1)
            else:
                return None

    def is_leaf(self) -> bool:
        """ Return True if <self> has no children

        Runtime: O(1)

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.is_leaf()
        True
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.is_leaf()
        False
        """
        return self._lt is None and self._gt is None

    def _extract_tree_nodes(self) -> List[Tuple[int, int, str]]:
        """ Return a list of tuples containing the x coordinate, y coordinate
        and name of the player. This method uses an in order traversal to
        collect all the information of the nodes in the tree.

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (150, 150))
        >>> d1._extract_tree_nodes()
        [(50, 50, 'Parinita'), (100, 100, 'Rohan'), (150, 150, 'Grace')]
        """
        node_lst = []
        if self._lt:
            node_lst.extend(self._lt._extract_tree_nodes())
        node_lst.append((self._point[0], self._point[1], self._name))
        if self._gt:
            node_lst.extend(self._gt._extract_tree_nodes())

        return node_lst

    def _balance_helper(self, info_lst: List[Tuple[int, int, str]]) -> None:
        """ Balance <self> so that there is at most a difference of 1 between
        the size of the _lt subtree and the size of the _gt subtree for all
        trees in <self>.

        Precondition: the values in this tree must be possible to balance

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (75, 25))
        >>> d1.insert('Parimal', (25, 20))
        >>> d1._balance_helper(d1._extract_tree_nodes())
        >>> d1._extract_tree_nodes()
        [(25, 20, 'Parimal'), (50, 50, 'Parinita'),
        (75, 25, 'Grace'), (100, 100, 'Rohan)]
        """

        num = self._split_type_num()

        info_lst.sort(key=lambda x: x[num])

        median = _find_median(info_lst, num)

        self._point = (info_lst[median][0], info_lst[median][1])
        self._name = info_lst[median][2]

        left_lst = info_lst[:median]
        right_lst = info_lst[median+1:]

        if len(left_lst) > 0:
            self._lt = self._create_new_subtree()
            self._lt._balance_helper(left_lst)

        if len(right_lst) > 0:
            self._gt = self._create_new_subtree()
            self._gt._balance_helper(right_lst)

    def balance(self) -> None:
        """ Balance <self> so that there is at most a difference of 1 between
        the size of the _lt subtree and the size of the _gt subtree for all
        trees in <self>.

        Precondition: the values in this tree must be possible to balance

        >>> d1 = TwoDTree((0, 0), (200, 200))
        >>> d1.insert('Rohan', (100, 100))
        >>> d1.insert('Parinita', (50, 50))
        >>> d1.insert('Grace', (75, 25))
        >>> d1.insert('Parimal', (25, 20))
        >>> d1.balance()
        >>> d1._extract_tree_nodes()
        [(25, 20, 'Parimal'), (50, 50, 'Parinita'),
        (75, 25, 'Grace'), (100, 100, 'Rohan)]
        """
        # checks if self is empty
        if self.is_empty():
            return
        # collects info of all nodes in tree in an in-order traversal
        extracted_lst = self._extract_tree_nodes()
        #print(extracted_lst)

        # set children and the root value to be None
        self._lt, self._gt, self._point, self._name = None, None, None, None

        self._balance_helper(extracted_lst)

        #final_lst = self._extract_tree_nodes()
        #return final_lst


def _find_median(lst: List[Tuple[int, int, str]], num: int) -> int:
    """ Returns the median value of the <lst>. If there are multiple median
    values, return the one that is the furthest in the list. <num> tells which
    value in the tuple to look at and decide.

    Precondition: <lst> is already sorted by either the x or y value.

    >>> d1 = TwoDTree((0, 0), (200, 200))
    >>> d1.insert('Rohan', (100, 100))
    >>> d1.insert('Parinita', (50, 50))
    >>> d1.insert('Grace', (150, 150))
    >>> result = d1._extract_tree_nodes()
    [(50, 50, 'Parinita'), (100, 100, 'Rohan'), (150, 150, 'Grace')]
    >>> result._find_median(result, 0)
    1
    """
    middle = (len(lst) - 1)//2
    while middle + 1 < len(lst) and lst[middle][num] == lst[middle+1][num]:
        middle += 1
    return middle


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={'extra-imports': ['typing'],
                                'disable': ['R0913', 'R0902', 'W0611', 'R1710',
                                            'R1702']})
