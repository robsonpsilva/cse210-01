from tic_tac_toe import print_grid, generates_and_fill_grid, check_grid_position_available,\
validate_player_victory

import pytest

def test_print_grid():
    grid = [['1','|','2','|','3'],
        ['-','+','-','+','-'],
        ['4','|','5','|','6'],
        ['-','+','-','+','-'],
        ['7','|','8','|','9']]
    string1 = print_grid(grid)
    string2 = '1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n'
    assert string1 == string2

def test_generates_and_fill_grid():
    #Initialize grid with its default configuration
    grid = [['1','|','2','|','3'],
        ['-','+','-','+','-'],
        ['4','|','5','|','6'],
        ['-','+','-','+','-'],
        ['7','|','8','|','9']]
    
    #Changes the grid first test
    grid = generates_and_fill_grid(grid, '9', 'o')
    #Formats a new grid to comparison
    grid_aux = [['1','|','2','|','3'],
        ['-','+','-','+','-'],
        ['4','|','5','|','6'],
        ['-','+','-','+','-'],
        ['7','|','8','|','o']]
    row = 0
    for line in grid:
        assert line == grid_aux[row]
        row += 1
    
    #Changes the grid second test
    grid = generates_and_fill_grid(grid, '4', 'x')
     #Formats a new grid to comparison
    grid_aux = [['1','|','2','|','3'],
        ['-','+','-','+','-'],
        ['x','|','5','|','6'],
        ['-','+','-','+','-'],
        ['7','|','8','|','o']]
    row = 0
    for line in grid:
        assert line == grid_aux[row]
        row += 1
def test_check_grid_position_available():
    
    #First test, verifies a free position in the following grid
    #This test must return that the position is free to use
    grid = [['1','|','2','|','3'],
        ['-','+','-','+','-'],
        ['4','|','5','|','6'],
        ['-','+','-','+','-'],
        ['7','|','8','|','9']]
    
    assert check_grid_position_available(grid, '2') == True
    
    #Second test, verifies a position ocupied in the following grid
    #This test must return that the position is occupied and can not
    #be used to put a new value

    grid_aux = [['1','|','2','|','3'],
        ['-','+','-','+','-'],
        ['x','|','5','|','6'],
        ['-','+','-','+','-'],
        ['7','|','8','|','o']]
    assert check_grid_position_available(grid_aux, '9') == False

def test_validate_player_victory():
    grid = [['x','|','x','|','x'],
        ['-','+','-','+','-'],
        ['4','|','5','|','6'],
        ['-','+','-','+','-'],
        ['7','|','8','|','9']]
    assert validate_player_victory(grid) == True

    grid = [['x','|','x','|','o'],
        ['-','+','-','+','-'],
        ['4','|','o','|','6'],
        ['-','+','-','+','-'],
        ['o','|','8','|','9']]
    assert validate_player_victory(grid) == True

    grid = [['x','|','x','|','o'],
        ['-','+','-','+','-'],
        ['4','|','o','|','6'],
        ['-','+','-','+','-'],
        ['x','|','8','|','9']]
    assert validate_player_victory(grid) == False

    grid = [['1','|','2','|','3'],
        ['-','+','-','+','-'],
        ['4','|','5','|','6'],
        ['-','+','-','+','-'],
        ['7','|','8','|','9']]
    assert validate_player_victory(grid) == False


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])