from tic_tac_toe import print_grid, generates_and_fill_grid
import pytest
import collections

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


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])