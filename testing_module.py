import trees
# import games
# import players
import pytest

#TODO TREE

#TODO __contains__  (3 TESTS)

def test_contains_no_player_in_tree():
    """No player in the tree with that name"""
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))

    assert q1.__contains__('Tony') is False

    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (50, 50))
    d1.insert('Grace', (120, 80))
    d1.insert('Rohan', (150, 150))
    assert d1.__contains__('Tony') is False


def test_contains_simple_tree():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))

    assert q1.__contains__('Parinita') is True
    assert q1.__contains__('Grace') is True
    assert q1.__contains__('Rohan') is True

    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (50, 50))
    d1.insert('Grace', (120, 80))
    d1.insert('Rohan', (150, 150))
    assert d1.__contains__('Parinita') is True
    assert d1.__contains__('Grace') is True
    assert d1.__contains__('Rohan') is True

def test_contains_complex_tree():
    """Picture 4 to picture 5 in the handout"""
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))
    q1.insert('Parimal', (120, 180))

    assert q1.__contains__('Parinita') is True
    assert q1.__contains__('Grace') is True
    assert q1.__contains__('Rohan') is True
    assert q1.__contains__('Parimal') is True
    assert q1.__contains__('Emily') is False

    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (40, 40))
    d1.insert('Rohan', (40, 50))
    d1.insert('Grace', (30, 60))
    d1.insert('Parimal', (120, 180))

    assert d1.__contains__('Parinita') is True
    assert d1.__contains__('Grace') is True
    assert d1.__contains__('Rohan') is True
    assert d1.__contains__('Parimal') is True
    assert d1.__contains__('Emily') is False

# todo ************************************************************************

#TODO _find_name (4 TESTS)

def test_find_name_no_name_in_tree():
    '''QuadTree'''
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))

    assert q1._find_name('Tony') is None

    '''TwoDTree'''
    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (50, 50))
    d1.insert('Grace', (120, 80))
    d1.insert('Rohan', (150, 150))
    assert d1._find_name('Tony') is None


def test_find_name_simple_tree():
    '''QuadTree'''
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    #ne insert
    q1.insert('Grace', (120, 80))
    #se insert
    q1.insert('Rohan', (150, 150))

    assert q1._find_name('Parinita') == (50, 50)
    assert q1._find_name('Grace') == (120, 80)
    assert q1._find_name('Rohan') == (150, 150)

    '''TwoDTree'''
    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (50, 50))
    #gt insert
    d1.insert('Grace', (120, 80))
    #gt gt insert
    d1.insert('Rohan', (150, 150))

    assert d1._find_name('Parinita') == (50, 50)
    assert d1._find_name('Grace') == (120, 80)
    assert d1._find_name('Rohan') == (150, 150)


def test_find_name_complex_tree():
    """Picture 4 to picture 5 in the handout"""
    '''QuadTree'''
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))
    q1.insert('Parimal', (120, 180))

    assert q1._find_name('Parinita') == (50, 50)
    assert q1._find_name('Grace') == (120, 80)
    assert q1._find_name('Rohan') == (150, 150)
    assert q1._find_name('Parimal') == (120, 180)
    assert q1._find_name('Emily') is None

    '''TwoDTree'''
    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (40, 40))
    d1.insert('Rohan', (40, 50))
    d1.insert('Grace', (30, 60))
    d1.insert('Parimal', (120, 180))

    assert d1._find_name('Parinita') == (40, 40)
    assert d1._find_name('Grace') == (30, 60)
    assert d1._find_name('Rohan') == (40, 50)
    assert d1._find_name('Parimal') == (120, 180)
    assert d1._find_name('Emily') is None

def test_find_name_duplicate():
    """ Testing how the tree handles duplicates"""
    '''QuadTree'''
    q1 = trees.QuadTree((100, 100))
    q1.insert('Rohan', (50, 50))
    q1.insert('Parinita', (40, 40))
    q1.insert('Grace', (75, 89))
    q1.insert('Parimal', (50, 51))

    q1.insert('Rohan', (120, 30))

    assert q1._find_name('Rohan') == (50, 50)

    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (40, 40))
    d1.insert('Rohan', (40, 50))
    d1.insert('Rohan', (41, 40))
    d1.insert('Grace', (30, 60))
    d1.insert('Rohan', (120, 180))

    assert d1._find_name('Rohan') == (40, 50)

# todo ************************************************************************

#TODO remove (3 TESTS, TESTS)

'''QuadTree'''

def test_remove_simple_quad_tree():
    """Testing remove with Picture 2 to picture 3 in the handout"""
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Parimal', (120, 180))

    q1.remove('Parinita')

    assert q1._name is None
    assert q1._point is None
    assert q1._centre == (100, 100)

    assert q1._nw is None

    assert q1._ne._centre == (150, 50)
    assert q1._ne._point == (120, 80)
    assert q1._ne._name == 'Grace'

    assert q1._se._centre == (150, 150)
    assert q1._se._point == (120, 180)
    assert q1._se._name == 'Parimal'


def test_remove_complex_quad_tree():
    """Testing remove on Picture 1 to picture 2 in the handout"""
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))
    q1.insert('Parimal', (120, 180))

    q1.remove('Rohan')

    assert q1._name is None
    assert q1._point is None
    assert q1._centre == (100, 100)

    assert q1._nw._centre == (50, 50)
    assert q1._nw._point == (50, 50)
    assert q1._nw._name == 'Parinita'

    assert q1._ne._centre == (150, 50)
    assert q1._ne._point == (120, 80)
    assert q1._ne._name == 'Grace'

    assert q1._se._centre == (150, 150)
    assert q1._se._point == (120, 180)
    assert q1._se._name == 'Parimal'
    assert q1._se._nw is None
    assert q1._se._ne is None
    assert q1._se._sw is None
    assert q1._se._se is None


def test_remove_not_promoting_bc_not_a_leaf_quad_tree():
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    q1.remove('Parinita')

    assert q1._name is None
    assert q1._point is None
    assert q1._centre == (100, 100)
    assert q1._nw is not None
    assert q1._ne is None
    assert q1._sw is None
    assert q1._se is None

    assert q1._nw._name is None
    assert q1._nw._point is None
    assert q1._nw._centre == (50, 50)
    assert q1._nw._nw is None
    assert q1._nw._ne is None
    assert q1._nw._sw is None
    assert q1._nw._se is not None

    assert q1._nw._se._name is None
    assert q1._nw._se._point is None
    assert q1._nw._se._centre == (75, 75)

    assert q1._nw._se._nw._point == (60, 60)
    assert q1._nw._se._nw._name == 'Rohan'

    assert q1._nw._se._se._point == (80, 90)
    assert q1._nw._se._se._name == 'Grace'

    assert q1._nw._se._ne is None
    assert q1._nw._se._sw is None


# todo ************************************************************************

#TODO move (TESTS)

'''QuadTree'''
def test_move__player_out_of_board():
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    with pytest.raises(trees.OutOfBoundsError):
        q1.move('Parinita', 'E', 50)


def test_move__name_doesnt_exist_on_board():
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    res = q1.move('Tony', 'E', 20)
    assert res is None

def test_move__player_simple():
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    assert q1._name is None
    assert q1._point is None
    assert q1._centre == (100, 100)
    assert q1._nw is not None
    assert q1._ne is not None
    assert q1._sw is None
    assert q1._se is None


    assert q1._ne._name == 'Parinita'
    assert q1._ne._point == (170, 30)
    assert q1._ne._centre == (150, 50)
    assert q1._ne._nw is None
    assert q1._ne._ne is None
    assert q1._ne._sw is None
    assert q1._ne._se is None

    assert q1._nw._name is None
    assert q1._nw._point is None
    assert q1._nw._centre == (50, 50)
    assert q1._nw._nw is None
    assert q1._nw._ne is None
    assert q1._nw._sw is None
    assert q1._nw._se is not None

    assert q1._nw._se._name is None
    assert q1._nw._se._point is None
    assert q1._nw._se._centre == (75, 75)

    assert q1._nw._se._nw._point == (60, 60)
    assert q1._nw._se._nw._name == 'Rohan'

    assert q1._nw._se._se._point == (80, 90)
    assert q1._nw._se._se._name == 'Grace'

    assert q1._nw._se._ne is None
    assert q1._nw._se._sw is None

    #AFTER MOVING

    res = q1.move('Parinita', 'E', 20)
    assert res == (190, 30)

    res2 = q1.move('Rohan', 'S', 30)
    assert res2 == (60, 90)

    assert q1._name is None
    assert q1._point is None
    assert q1._centre == (100, 100)
    assert q1._nw is not None
    assert q1._ne is not None
    assert q1._sw is None
    assert q1._se is None

    assert q1._ne._name == 'Parinita'
    assert q1._ne._point == (190, 30)
    assert q1._ne._centre == (150, 50)

    assert q1._nw._name is None
    assert q1._nw._point is None
    assert q1._nw._centre == (50, 50)
    assert q1._nw._nw is None
    assert q1._nw._ne is None
    assert q1._nw._sw is None
    assert q1._nw._se is not None

    assert q1._nw._se._name is None
    assert q1._nw._se._point is None
    assert q1._nw._se._centre == (75, 75)
    assert q1._nw._se._nw is None
    assert q1._nw._se._ne is None
    assert q1._nw._se._sw is not None
    assert q1._nw._se._se is not None

    assert q1._nw._se._sw._name == 'Rohan'
    assert q1._nw._se._sw._point == (60, 90)
    assert q1._nw._se._sw._centre == (62, 87)
    assert q1._nw._se._sw._nw is None
    assert q1._nw._se._sw._ne is None
    assert q1._nw._se._sw._sw is None
    assert q1._nw._se._sw._se is None

    assert q1._nw._se._se._name == 'Grace'
    assert q1._nw._se._se._point == (80, 90)
    assert q1._nw._se._se._centre == (87, 87)
    assert q1._nw._se._se._nw is None
    assert q1._nw._se._se._ne is None
    assert q1._nw._se._se._sw is None
    assert q1._nw._se._se._se is None

# todo ************************************************************************
#
# TODO move_point (TESTS)
#
# todo ************************************************************************

#TODO _determine_corners (TESTS)

# todo ************************************************************************

#TODO _check_in_box (TESTS)

# todo ************************************************************************

#TODO names_in_range (TESTS)

def test_names_in_range_simple_name_in_range():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    assert q1.names_in_range((40, 40), 'SE', 25) == ['Parinita']

def test_names_in_range_simple_name_not_in_range():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    assert q1.names_in_range((40, 40), 'SE', 9) == []

def test_names_in_range_two_names():
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    assert q1.names_in_range((50, 50), 'SE', 50) == ['Rohan', 'Grace']


def test_names_in_range_two_names_deeper_quad_tree():
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    assert q1.names_in_range((100, 90), 'NW', 20) == ['Grace']


def test_names_in_range_complex_quad_tree():
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (175, 25))
    q1.insert('Grace', (20, 25))
    q1.insert('Rohan', (180, 25))
    q1.insert('Parimal', (176, 100))
    q1.insert('Tony', (75, 150))

    assert q1.names_in_range((80, 120), 'SW', 40) == ['Tony']
    assert q1.names_in_range((170, 30), 'NE', 6) == ['Parinita']

    assert q1.names_in_range((180, 25), 'NE', 1) == ['Rohan']
    assert q1.names_in_range((180, 25), 'NW', 1) == ['Rohan']
    assert q1.names_in_range((180, 25), 'SE', 1) == ['Rohan']
    assert q1.names_in_range((180, 25), 'SW', 1) == ['Rohan']

    assert q1.names_in_range((180, 25), 'NW', 5) == ['Rohan', 'Parinita'] or \
           q1.names_in_range((180, 25), 'NW', 5) == ['Parinita', 'Rohan']

def test_names_in_range_edges():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (0, 0))

    assert q1.names_in_range((1, 1), 'NW', 20) == ['Parinita']

# todo ************************************************************************

#TODO depth (TESTS)

# todo ************************************************************************

#TODO is_empty (TESTS)
#
#
#
#
#
#
#

# todo ************************************************************************
# todo ************************************************************************
# todo ************************************************************************
# todo ************************************************************************
# todo ************************************************************************
# todo ************************************************************************


#TODO QUAD TREE



# todo ************************************************************************

#TODO contains_point (3 TESTS)
def test_contains_point_no_point_quad_tree():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))

    assert q1.contains_point((200, 200)) is False

def test_contains_point_simple_quad_tree():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))

    assert q1.contains_point((150, 150)) is True

def test_contains_point_complex_quad_tree():
    """Picture 4 to picture 5 in the handout"""
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))
    q1.insert('Parimal', (120, 180))

    assert q1.contains_point((120, 180)) is True
    assert q1.contains_point((120, 181)) is False

# todo ************************************************************************

#TODO _create_new_subtree (0 TESTS)

# todo ************************************************************************

#TODO _insert_helper (0 TESTS)

# todo ************************************************************************

#TODO insert (8 TESTS)
def test_insert_empty_quad_tree():
    """Picture 1 to picture 2 in the handout"""
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))

    assert q1._name == 'Parinita'
    assert q1._point == (50, 50)

    # assert getattr(q1, '_nw') is None
    assert q1._nw is None
    assert q1._ne is None
    assert q1._sw is None
    assert q1._se is None


def test_insert_single_quad_tree():
    """Picture 2 to picture 3 in the handout"""
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))

    assert q1._name is None
    assert q1._point is None

    assert q1._nw._centre == (50, 50)
    assert q1._nw._point == (50, 50)
    assert q1._nw._name == 'Parinita'

    assert q1._ne._centre == (150, 50)
    assert q1._ne._point == (120, 80)
    assert q1._ne._name == 'Grace'


def test_insert_adding_a_child_quad_tree():
    """Picture 3 to picture 4 in the handout"""
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))

    assert q1._name is None
    assert q1._point is None

    assert q1._nw._centre == (50, 50)
    assert q1._nw._point == (50, 50)
    assert q1._nw._name == 'Parinita'

    assert q1._ne._centre == (150, 50)
    assert q1._ne._point == (120, 80)
    assert q1._ne._name == 'Grace'

    assert q1._se._centre == (150, 150)
    assert q1._se._point == (150, 150)
    assert q1._se._name == 'Rohan'


def test_insert_splitting_a_child_quad_tree():
    """Picture 4 to picture 5 in the handout"""
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))
    q1.insert('Parimal', (120, 180))

    assert q1._name is None
    assert q1._point is None

    assert q1._nw._centre == (50, 50)
    assert q1._nw._point == (50, 50)
    assert q1._nw._name == 'Parinita'

    assert q1._ne._centre == (150, 50)
    assert q1._ne._point == (120, 80)
    assert q1._ne._name == 'Grace'

    assert q1._se._centre == (150, 150)
    assert q1._se._point is None
    assert q1._se._name is None

    assert q1._se._nw._centre == (125, 125)
    assert q1._se._nw._point == (150, 150)
    assert q1._se._nw._name == 'Rohan'

    assert q1._se._sw._centre == (125, 175)
    assert q1._se._sw._point == (120, 180)
    assert q1._se._sw._name == 'Parimal'


def test_insert_player_in_existing_point_simple_quad_tree():
    """Picture 1 to picture 2 in the handout"""
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))

    with pytest.raises(trees.OutOfBoundsError):
        q1.insert('Grace', (50, 50))

    assert q1._name == 'Parinita'
    assert q1._point == (50, 50)
    assert q1._nw is None
    assert q1._ne is None
    assert q1._sw is None
    assert q1._se is None

def test_insert_player_in_existing_point_complex_quad_tree():
    """Picture 4 to picture 5 in the handout"""
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))
    q1.insert('Parimal', (120, 180))

    with pytest.raises(trees.OutOfBoundsError):
        q1.insert('Tony', (120, 180))

    assert q1._name is None
    assert q1._point is None

    assert q1._nw._centre == (50, 50)
    assert q1._nw._point == (50, 50)
    assert q1._nw._name == 'Parinita'

    assert q1._ne._centre == (150, 50)
    assert q1._ne._point == (120, 80)
    assert q1._ne._name == 'Grace'

    assert q1._se._centre == (150, 150)
    assert q1._se._point is None
    assert q1._se._name is None

    assert q1._se._nw._centre == (125, 125)
    assert q1._se._nw._point == (150, 150)
    assert q1._se._nw._name == 'Rohan'

    assert q1._se._sw._centre == (125, 175)
    assert q1._se._sw._point == (120, 180)
    assert q1._se._sw._name == 'Parimal'

def test_insert_complex_nested_example():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    q1.insert('Bob', (190, 30))

    assert q1._name is None
    assert q1._point is None
    assert q1._centre == (100, 100)

    assert q1._nw._centre == (50, 50)
    assert q1._nw._point is None
    assert q1._nw._name is None

    assert q1._ne._centre == (150, 50)
    assert q1._ne._point is None
    assert q1._ne._name is None

    assert q1._ne._ne._centre == (175, 25)
    assert q1._ne._ne._point is None
    assert q1._ne._ne._name is None
    assert q1._ne._ne._nw is None
    assert q1._ne._ne._ne is None
    assert q1._ne._ne._sw is not None
    assert q1._ne._ne._se is not None

    assert q1._ne._ne._sw._name == 'Parinita'
    assert q1._ne._ne._sw._point == (170, 30)

    assert q1._ne._ne._se._name == 'Bob'
    assert q1._ne._ne._se._point == (190, 30)

def test_insert_duplicate_names():
    q1 = trees.QuadTree((100, 100))
    #se corner
    q1.insert('Parinita', (90, 80))
    #sw corner
    q1.insert('Parinita', (60, 80))

    assert q1._nw._se._se._name == 'Parinita'
    assert q1._nw._se._se._point == (90, 80)

    assert q1._nw._se._sw._name == 'Parinita'
    assert q1._nw._se._sw._point == (60, 80)

def test_insert_small_pixels():
    q1 = trees.QuadTree((1, 1))
    q1.insert('Parinita', (1, 0)) #ne
    q1.insert('Rohan', (0, 1)) #sw
    q1.insert('Grace', (0, 0)) #nw
    q1.insert('Koby', (1, 1)) #se

    assert q1._centre == (1, 1)
    assert q1._nw._centre == (0, 0)

    assert q1._nw._sw._point == (0, 1)
    assert q1._nw._sw._name == 'Rohan'

    assert q1._nw._ne._point == (1, 0)
    assert q1._nw._ne._name == 'Parinita'

    assert q1._nw._nw._point == (0, 0)
    assert q1._nw._nw._name == 'Grace'

    assert q1._nw._se._point == (1, 1)
    assert q1._nw._se._name == 'Koby'

def test_crazy():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Grace', (81, 90))
    q1.insert('Eng', (80, 90))

#
#

# todo ************************************************************************
#
# TODO _find_point (3 TESTS)

def test_find_point_doesnt_exist():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    q1.insert('Bob', (190, 30))

    assert q1._find_point((0, 0)) is None
    assert q1._find_point((60, 61)) is None

def test_find_point_simple_quadtree():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    q1.insert('Bob', (190, 30))

    assert q1._find_point((80, 90)) == 'Grace'
    assert q1._find_point((190, 30)) == 'Bob'

def test_find_point_complex_quadtree():
    pass

#FIXME!!!!!!!!!!!!!!!!!!!!!!!!!
def test_cray():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (81, 90))
    q1.insert('Rohan', (62, 90))
    q1.insert('Parimal', (82, 90))
    #fixme
    q1.insert('Grace', (80, 90))
    q1.insert('Vaishali', (80, 150))

    assert q1._find_point((80, 90)) == 'Grace'
    assert q1._find_point((81, 90)) == 'Grace'
    assert q1._find_point((82, 90)) == 'Parimal'
    assert q1._find_point((80, 150)) == 'Vaishali'
#
# todo ************************************************************************

#TODO _num_kids (0 TESTS)

# todo ************************************************************************

#TODO _promote_leaf (0 TESTS)

#todo ************************************************************************

#TODO remove_point (6 TESTS)

def test_remove_point_simple_quad_tree():
    """Picture 2 to picture 3 in the handout"""
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Parimal', (120, 180))

    q1.remove_point((50, 50))

    assert q1._name is None
    assert q1._point is None
    assert q1._centre == (100, 100)

    assert q1._nw is None

    assert q1._ne._centre == (150, 50)
    assert q1._ne._point == (120, 80)
    assert q1._ne._name == 'Grace'

    assert q1._se._centre == (150, 150)
    assert q1._se._point == (120, 180)
    assert q1._se._name == 'Parimal'


def test_remove_point_complex_quad_tree():
    """Picture 1 to picture 2 in the handout"""
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (50, 50))
    q1.insert('Grace', (120, 80))
    q1.insert('Rohan', (150, 150))
    q1.insert('Parimal', (120, 180))

    q1.remove_point((150, 150))

    assert q1._name is None
    assert q1._point is None
    assert q1._centre == (100, 100)

    assert q1._nw._centre == (50, 50)
    assert q1._nw._point == (50, 50)
    assert q1._nw._name == 'Parinita'

    assert q1._ne._centre == (150, 50)
    assert q1._ne._point == (120, 80)
    assert q1._ne._name == 'Grace'

    assert q1._se._centre == (150, 150)
    assert q1._se._point == (120, 180)
    assert q1._se._name == 'Parimal'
    assert q1._se._nw is None
    assert q1._se._ne is None
    assert q1._se._sw is None
    assert q1._se._se is None

def test_remove_point_not_promoting_bc_not_a_leaf_quad_tree():
    q1 = trees.QuadTree((100, 100))

    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    q1.remove_point((170, 30))

    assert q1._name is None
    assert q1._point is None
    assert q1._centre == (100, 100)
    assert q1._nw is not None
    assert q1._ne is None
    assert q1._sw is None
    assert q1._se is None

    assert q1._nw._name is None
    assert q1._nw._point is None
    assert q1._nw._centre == (50, 50)
    assert q1._nw._nw is None
    assert q1._nw._ne is None
    assert q1._nw._sw is None
    assert q1._nw._se is not None

    assert q1._nw._se._name is None
    assert q1._nw._se._point is None
    assert q1._nw._se._centre == (75, 75)

    assert q1._nw._se._nw._point == (60, 60)
    assert q1._nw._se._nw._name == 'Rohan'

    assert q1._nw._se._se._point == (80, 90)
    assert q1._nw._se._se._name == 'Grace'

    assert q1._nw._se._ne is None
    assert q1._nw._se._sw is None


def test_remove_complex_nested_example():
    q1 = trees.QuadTree((100, 100))
    q1.insert('Parinita', (170, 30))
    q1.insert('Grace', (80, 90))
    q1.insert('Rohan', (60, 60))

    q1.insert('Bob', (190, 30))

    q1.remove_point((170, 30))


    assert q1._name is None
    assert q1._point is None
    assert q1._centre == (100, 100)

    assert q1._nw._centre == (50, 50)
    assert q1._nw._point is None
    assert q1._nw._name is None

    assert q1._ne._centre == (150, 50)
    assert q1._ne._point == (190, 30)
    assert q1._ne._name == 'Bob'

# todo ************************************************************************

#TODO _names_in_range_helper (TESTS)

#todo ************************************************************************

#TODO size (TESTS)

# todo ************************************************************************

#TODO height (TESTS)

# todo ************************************************************************

#TODO _depth_helper (TESTS)

# todo ************************************************************************

#TODO is_leaf (TESTS)







# todo ************************************************************************
# todo ************************************************************************
# todo ************************************************************************
# todo ************************************************************************
# todo ************************************************************************
# todo ************************************************************************

#TODO TWOD TREE

#TODO _split_type_num (TESTS)

# todo ************************************************************************

#TODO _num_kids (TESTS)

# todo ************************************************************************

#TODO contains_point (TESTS)

# todo ************************************************************************

#TODO _create_new_subtree (TESTS)

# todo ************************************************************************

#TODO _insert_helper (TESTS)

# todo ************************************************************************

#TODO insert

def test_insert_simple_twoDtree():
    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (30, 40))

    assert d1._point == (30, 40)
    assert d1._name == 'Parinita'

def test_insert_handout_1_to_3_twoDtree():
    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (30, 100))

    assert d1._point == (30, 100)
    assert d1._name == 'Parinita'

    d1.insert('Rohan', (150, 80))
    assert d1._gt._point == (150, 80)
    assert d1._gt._name == 'Rohan'
    assert d1._gt._nw is None
    assert d1._gt._se is None

def test_insert_handout_3_to_4_twoDtree():
    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (30, 100))
    d1.insert('Rohan', (150, 80))
    d1.insert('Grace', (150, 20))

    assert d1._gt._lt._point == (150, 20)
    assert d1._gt._lt._name == 'Grace'
    assert d1._gt._lt._nw is None
    assert d1._gt._lt._se is None


def test_insert_handout_4_to_5_twoDtree():
    d1 = trees.TwoDTree((0, 0), (200, 200))
    d1.insert('Parinita', (30, 100))
    d1.insert('Rohan', (150, 80))
    d1.insert('Grace', (150, 20))
    d1.insert('Tony', (20, 20))

    assert d1._lt._point == (20, 20)
    assert d1._lt._name == 'Tony'
    assert d1._lt._nw is None
    assert d1._lt._se is None

# todo ************************************************************************

#TODO _find_point (TESTS)

# todo ************************************************************************

#TODO _find_largest_node_value (TESTS)
def test_simple_2D_tree():
    d1 = trees.TwoDTree((0, 0), (500, 500))
    d1.insert('a', (100, 100))
    d1.insert('b', (50, 100))

    d1.insert('c', (4, 200))
    d1.insert('d', (1, 150))
    d1.insert('e', (20, 210))

    d1.insert('f', (70, 75))
    d1.insert('g', (5, 80))
    d1.insert('h', (75, 20))

    assert d1._lt._find_largest_node_value(0) == ('h', (75, 20))
    assert d1._lt._find_largest_node_value(1) == ('e', (20, 210))
#
# # todo ************************************************************************
#
# #TODO remove_point (TESTS)
#
# # todo ************************************************************************
#
# #TODO _names_in_range_helper (TESTS)
#
# # todo ************************************************************************
#
# #TODO size (TESTS)
#
# # todo ************************************************************************
#
# #TODO height (TESTS)
#
# # todo ************************************************************************
#
# #TODO _depth_helper (TESTS)
#
# # todo ************************************************************************
#
# #TODO is_leaf (TESTS)
#
# # todo ************************************************************************
#
# #TODO balance (TESTS)

def test_balance_2Dtree_only_root():
    tree = trees.TwoDTree((0, 0), (500, 500))
    tree.insert('a', (250, 250))
    tree.balance()
    assert tree._name == 'a'
    assert tree._point == (250,250)
    assert tree._nw == (0,0)
    assert tree._se == (500,500)
    assert tree._lt == None
    assert tree._gt == None
    assert tree._split_type == 'x'

def test_balance_2Dtree_empty_tree():
    tree = trees.TwoDTree((0, 0), (500, 500))
    tree.balance()
    assert tree._name == None
    assert tree._point == None
    assert tree._nw == (0,0)
    assert tree._se == (500,500)
    assert tree._lt == None
    assert tree._gt == None
    assert tree._split_type == 'x'

def test_balance_2Dtree_left_skewed():
    tree = trees.TwoDTree((0, 0), (500, 500))
    tree.insert('a', (450, 450))
    tree.insert('b', (350, 350))
    tree.insert('c', (250, 250))
    tree.insert('d', (150, 150))

    assert tree.height() == 4
    tree.balance()

    assert tree._name == 'c'
    assert tree._point == (250,250)
    assert tree._nw == (0,0)
    assert tree._se == (500,500)
    assert tree._lt is not None
    assert tree._gt is not None
    assert tree._split_type == 'x'

    assert tree._lt._name == 'd'
    assert tree._lt._point == (150, 150)
    assert tree._lt._nw is None
    assert tree._lt._se is None
    assert tree._lt._lt is None
    assert tree._lt._gt is None
    assert tree._lt._split_type == 'y'

    assert tree._gt._name == 'b'
    assert tree._gt._point == (350, 350)
    assert tree._gt._nw is None
    assert tree._gt._se is None
    assert tree._gt._lt is None
    assert tree._gt._gt is not None
    assert tree._gt._split_type == 'y'

    assert tree._gt._gt._name == 'a'
    assert tree._gt._gt._point == (450, 450)
    assert tree._gt._gt._nw is None
    assert tree._gt._gt._se is None
    assert tree._gt._gt._lt is None
    assert tree._gt._gt._gt is None
    assert tree._gt._gt._split_type == 'x'

    assert tree.height() == 3

def test_balance_2Dtree_compicated():
    tree = trees.TwoDTree((0, 0), (500, 500))
    tree.insert('a', (250, 250))
    tree.insert('b', (300, 250))
    tree.insert('c', (300, 200))
    tree.insert('d', (300, 300))
    tree.insert('e', (275, 300))
    tree.insert('f', (275, 350))
    tree.insert('g', (290, 350))

    tree.balance()

    assert tree._point == (290, 350)
    assert tree._name == 'g'

    assert tree._lt._point == (275, 300)
    assert tree._lt._name == 'e'

    assert tree._lt._lt._point == (250, 250)
    assert tree._lt._lt._name == 'a'

    assert tree._lt._gt._point == (275, 350)
    assert tree._lt._gt._name == 'f'

    assert tree._gt._point == (300, 250)
    assert tree._gt._name == 'b'

    assert tree._gt._lt._point == (300, 200)
    assert tree._gt._lt._name == 'c'

    assert tree._gt._gt._point == (300, 300)
    assert tree._gt._gt._name == 'd'

if __name__ == '__main__':
    import pytest
    pytest.main(['testing_module.py'])
    # test_cray()
    # test_insert_small_pixels()
    # test_balance_2Dtree_left_skewed()
