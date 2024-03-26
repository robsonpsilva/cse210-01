from tic_tac_toe import generates_grid, select_player_input
import pytest




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])