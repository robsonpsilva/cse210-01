user_input_flag = True

grid = [[1,'|',2,'|',3],
        ['-','+','-','+','-'],
        [4,'|',5,'|',6],
        ['-','+','-','+','-'],
        [7,'|',8,'|',9]]

def generates_grid():
    for line in grid:
            print(f'{line[0]}|{line[2]}|{line[4]}')

def select_player_input():
    if user_input_flag == False:
        message = 'x\'s turn to choose a square (1-9):'
    else:
        message = 'o\'s turn to choose a square (1-9):'    
    user_input_flag = not user_input_flag
    return message
    
     
    

def main():
    generates_grid()

main()
