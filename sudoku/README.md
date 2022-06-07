In this task, the sudoku puzzle game has been solved using the AI based code.
For this purpose, a function has been added in the solution with name sudoku_solver(sudoku). Followings are the steps that are happening in it:

1: It will take one sudoku puzzle (a 9x9 NumPy array) as input, and returns the solved sudoku as another 9x9 NumPy array.
2: It will call the my_solver function in which through recursion approach the scheme will be followed in a way that the depth will be find out and then on false result the recursion will be happen.
3: Here, a check has been implemented to test if the defined location is correct for the grid or not. Based on this check, all of the information of columns and rows along with the grid is kept save. In case if any number with more than one occurance appear, the loop will be ended.
4: This will run for each of the 9 grids and the resultant will be a solved sudoku as another 9x9 NumPy array.
