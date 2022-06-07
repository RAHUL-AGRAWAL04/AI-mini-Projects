import numpy as np

# Load sudokus
sudoku = np.load("data/very_easy_puzzle.npy")
print("very_easy_puzzle.npy has been loaded into the variable sudoku")
print(f"sudoku.shape: {sudoku.shape}, sudoku[0].shape: {sudoku[0].shape}, sudoku.dtype: {sudoku.dtype}")

# Load solutions for demonstration
solutions = np.load("data/very_easy_solution.npy")
print()

# Print the first 9x9 sudoku...
print("First sudoku:")
print(sudoku[0], "\n")

# ...and its solution
print("Solution of first sudoku:")
print(solutions[0])

#verification Function for the solution obtained for the given problem
def validate(sudoku):
    cols = [[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        if sum(sudoku[i]) != 45: #sum of each row in solved 9x9 sudoku is excatly 45
            return False
        cols[0].append(sudoku[i][0])
        cols[1].append(sudoku[i][1])
        cols[2].append(sudoku[i][2])
        cols[3].append(sudoku[i][3])
        cols[4].append(sudoku[i][4])
        cols[5].append(sudoku[i][5])
        cols[6].append(sudoku[i][6])
        cols[7].append(sudoku[i][7])
        cols[8].append(sudoku[i][8])
    
    for x in cols:
        if sum(x) != 45:#sum of each column in solved 9x9 sudoku is excatly 45
            return False
    return True

def sudoku_solver(sudoku):
    #err_sudoku is a error matrix which will be given as output if the solution of given sudoku is not possible
    err_sudoku = [[-1, -1, -1, -1, -1, -1, -1, -1, -1],
                         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                         [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                         [-1, -1, -1, -1, -1, -1, -1, -1, -1]]
    
    solved_sudoku = my_solver(sudoku)                     
    
    #Verification code of the solution obtained.
    if solved_sudoku:
        solved_sudoku = sudoku
        if validate(solved_sudoku):
            return solved_sudoku
        else:
            return err_sudoku
    return err_sudoku

def structure_emp(sudoku, val_2):
    for R1 in range(9):
        for C1 in range(9):
            if(sudoku[R1][C1]== 0):
                val_2[0]= R1
                val_2[1]= C1
                return True
    return False
    
def structure_R1(sudoku, R1, vals):
    for i in range(9):
        if(sudoku[R1][i] == vals):
            return True
    return False 
    
def structure_C1(sudoku, C1, vals):
    for i in range(9):
        if(sudoku[i][C1] == vals):
            return True
    return False
    
def structure_dt(sudoku, R1, C1, vals):
    for i in range(3):
        for j in range(3):
            if(sudoku[i + R1][j + C1] == vals):
                return True
    return False
    
def loc_val(sudoku, R1, C1, val_3):
    return not structure_R1(sudoku, R1, val_3) and not structure_C1(sudoku, C1, val_3) and not structure_dt(sudoku, R1-R1%3,C1-C1%3, val_3)


def my_solver(sudoku):
    val_2 = [0, 0] 
    
    if(not structure_emp(sudoku, val_2)):
        return True
    R1 = val_2[0]
    C1 = val_2[1]
    for vals in range(1, 10):
        if(loc_val(sudoku, R1, C1, vals)):
            sudoku[R1][C1]= vals
            st=my_solver(sudoku)
            if(st):
                return True
            sudoku[R1][C1] = 0    
    return False



SKIP_TESTS = False

if not SKIP_TESTS:
    import time
    difficulties = ['very_easy', 'easy', 'medium', 'hard']

    for difficulty in difficulties:
        print(f"Testing {difficulty} sudokus")
        
        sudokus = np.load(f"data/{difficulty}_puzzle.npy")
        solutions = np.load(f"data/{difficulty}_solution.npy")
        
        count = 0
        for i in range(len(sudokus)):
            sudoku = sudokus[i].copy()
            print(f"This is {difficulty} sudoku number", i)
            print(sudoku)
            
            start_time = time.process_time()
            your_solution = sudoku_solver(sudoku)
            end_time = time.process_time()
            
            print(f"This is your solution for {difficulty} sudoku number", i)
            print(your_solution)
            
            print("Is your solution correct?")
            if np.array_equal(your_solution, solutions[i]):
                print("Yes! Correct solution.")
                count += 1
            else:
                print("No, the correct solution is:")
                print(solutions[i])
            
            print("This sudoku took", end_time-start_time, "seconds to solve.\n")

        print(f"{count}/{len(sudokus)} {difficulty} sudokus correct")
        if count < len(sudokus):
            break