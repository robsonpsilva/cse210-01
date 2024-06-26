"""
    Assignment - Write a code to perform a game Tiic-Tac-Toe after 
    lesson designation.

    Author: Robson Paulo da Silva

"""


user_input_flag = True


def generates_and_fill_grid(grid, option, mark =''):
    """
        This function generate and prints the tic-tac-toe grid
        option receives the cell chosed by the use and mark his leter
        'x' or 'o'
    """
    if option in ['1','2','3']:
        grid[0][2 * (int(option)-1)] = mark
    elif option in ['4','5','6']:
        grid[2][2 * (int(option)-4)] = mark
    elif option in ['7','8','9']:
        grid[4][2 * (int(option)-7)] = mark

    return grid

def check_grid_position_available(grid, option):
    """
        This function verifies if the user option is available,
        because in TIC-TAC-TOE, a placehold ocupied before can't be changed.
    """
    flag = True #True means free position
    if option in ['1','2','3']:
        if grid[0][2 * (int(option)-1)] in ['x','o']:
            flag = False #Means ocupied
    elif option in ['4','5','6']:
        if grid[2][2 * (int(option)-4)] in ['x','o']:
            flag = False #Means ocupied
    elif option in ['7','8','9']:
        if grid[4][2 * (int(option)-7)] in ['x','o']:
            flag = False #Means ocupied
    return flag

def print_grid(grid):
    #prints the grid in console
    grid_string = ''
    for line in grid:
        for cell in line:
            grid_string += f'{cell}'
        grid_string += '\n'
    print(grid_string)
    return grid_string


def select_player_input(user_input_flag):
    """
    There are two main massages possible in tic-tac-toe.
    This function serves to select between them. 
    """
    if user_input_flag == True:
        message = 'x\'s turn to choose a square (1-9):'
    else:
        message = 'o\'s turn to choose a square (1-9):'    
    return message

def validate_player_victory(grid):
    """
     [['1','|','2','|','3'],
      ['-','+','-','+','-'],
      ['4','|','5','|','6'],
      ['-','+','-','+','-'],
      ['7','|','8','|','9']]
    """
    flag = grid[0][0] == grid[0][2] == grid[0][4] or\
           grid[2][0] == grid[2][2] == grid[2][4] or\
           grid[4][0] == grid[4][2] == grid[4][4] or\
           grid[0][0] == grid[2][0] == grid[4][0] or\
           grid[0][2] == grid[2][2] == grid[4][2] or\
           grid[0][4] == grid[2][4] == grid[4][4] or\
           grid[0][0] == grid[2][2] == grid[4][4] or\
           grid[0][4] == grid[2][2] == grid[4][0]
           
    return flag

def main():
    flag = True
    grid =  [['1','|','2','|','3'],
      ['-','+','-','+','-'],
      ['4','|','5','|','6'],
      ['-','+','-','+','-'],
      ['7','|','8','|','9']]
    
    while True:

        #Show the tic-tac-toe grid because the player needs to choose 
        #the position they are going to select
        print_grid(grid)

        #gets user input 
        answer = input(select_player_input(flag))

        #Check if the data entry is integer number
        if answer.isdigit() == True:
            #if number THEN checks if it is in range between 1 and 9
            if answer in ['1','2','3','4','5','6','7','8','9']:
                #User entered a number in the right range
                
                #Verifies if the position is free
                if check_grid_position_available(grid,answer) == True:
                    #Means this position is free to use
                    if flag == True:
                        #Storage the player choice 
                        #Each player has one mark "x" or "y"
                        #True means x
                        grid = generates_and_fill_grid(grid,answer, 'x')
                        flag = False
                    else:
                        #Storage the player choice 
                        #Each player has one mark "x" or "y"
                        #False means y 
                        grid = generates_and_fill_grid(grid,answer, 'o')
                        flag = True
                    
                    #checks whether the player won the game with the last move
                    if validate_player_victory(grid) == True:
                        print('Congratulations you win the game!')
                        answer = input('Type q if you want to quit or everyone else to return to the application.')
                        if answer.lower() == 'q':
                            break
                        else:
                             grid = [['1','|','2','|','3'],
                                    ['-','+','-','+','-'],
                                    ['4','|','5','|','6'],
                                    ['-','+','-','+','-'],
                                    ['7','|','8','|','9']]   
                else:
                    #Means player selected a ocupied place
                    print('Error: The place selected is ocupied.')
                    answer = input('Type q if you want to quit or everyone else to return to the application.')
                    if answer.lower() == 'q':
                        break        
            else:
                #Means data entry is out of the range
                print('Error: Data entry must be a integer between 1 and 9.')
                answer = input('Type q if you want to quit or everyone else to return to the application.')
                if answer.lower() == 'q':
                    break
        else: #Mean data entry is not a integer number
            print('Error: Data entry is not a integer number.')
            answer = input('Type q if you want to quit or everyone else to return to the application.')
            if answer.lower() == 'q':
                break
    print('Application end')          

if __name__ == "__main__":
    main() 
