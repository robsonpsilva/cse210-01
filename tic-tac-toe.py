
grid = [[1,'|',2,'|',3],
        ['-','+','-','+','-'],
        [4,'|',5,'|',6],
        ['-','+','-','+','-'],
        [7,'|',8,'|',9]]

def generates_grid():
    for line in grid:
            print(f'{line[0]}|{line[2]}|{line[4]}')
    

def main():
    generates_grid()

main()
