global N
N = 4
 
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()
 
# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def isSafe(board, row, col):
 
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
 
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True
 
def solveNQUtil(board, col):
     
    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True
 
    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):
 
        if isSafe(board, i, col):
             
            # Place this queen in board[i][col]
            board[i][col] = 1
 
            # recur to place rest of the queens
            if solveNQUtil(board, col + 1) == True:
                return True
 
            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0
 
    # if the queen can not be placed in any row in
    # this column col then return false
    return False
 

def solveNQ():
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]
 
    if solveNQUtil(board, 0) == False:
        print ("Solution does not exist")
        return False
 
    printSolution(board)
    return True
 
# Driver Code
solveNQ()



'''
Constraint satisfaction is a technique where a problem is solved when its values satisfy certain
constraints or rules of the problem. Such type of technique leads to a deeper understanding of the
problem structure as well as its complexity.
Constraint satisfaction depends on three components, namely:
 X: It is a set of variables.
 D: It is a set of domains where the variables reside. There is a specific domain for each
variable.
 C: It is a set of constraints which are followed by the set of variables.
In constraint satisfaction, domains are the spaces where the variables reside, following the problem
specific constraints. These are the three main elements of a constraint satisfaction technique. The
constraint value consists of a pair of {scope, rel}. The scope is a tuple of variables which participate
in the constraint and rel is a relation which includes a list of values which the variables can take to
satisfy the constraints of the problem

Naive Algorithm:
Generate all possible configurations of queens on board and print a configuration that satisfies the given constraints.

while there are untried configurations
{
    generate the next configuration
    if queens don’t attack in this configuration then
    {
        print this configuration;
    }
}

Time Complexity: O(N*NCN)
Auxiliary Space: O(N^2)


'''
