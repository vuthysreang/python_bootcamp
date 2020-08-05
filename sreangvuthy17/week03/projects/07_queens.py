"""
    Description:    The aim of the project is to place 8 queens on a chessboard without them being able to run into each other in a single move. 
                        - A chessboard is composed of 8x8 squares. 
                        - One square can contain one queen maximum. 
                        - A queen can move in rows, column and diagonal. 
 
                    The functions will returns the number of possibilities of placing 8 queens on a chessboard without them being able to run into each others. 
                    Also will display all the possibilities found. 
 
                    You should use recursivity to solve this problem. You’re program must give the answer in less than 2 seconds. 
 
                    For the output you can display the chess boards as you want. 
                    
    Requirements :  ● Program name : ​07_queens.py  
                    ● Directory : ​week03/projects  
                    ● Function name : ​queens 
 
    Hint :  ❖ backtracking 
            ❖ recursivity 

    EXAMPLE: ================================================================= 
    VALID BOARD : 
    
    . . . . . . . Q     [0][0][0][0][0][0][0][1]    00000001 
    . . Q . . . . .     [0][0][1][0][0][0][0][0]    00100000 
    Q . . . . . . .     [1][0][0][0][0][0][0][0]    10000000
    . . . . . Q . .     [0][0][0][0][0][1][0][0]    00000100 
    . Q . . . . . .     [0][1][0][0][0][0][0][0]    01000000 
    . . . . Q . . .     [0][0][0][0][1][0][0][0]    00001000 
    . . . . . . Q .     [0][0][0][0][0][0][1][0]    00000010 
    . . . Q . . . .     [0][0][0][1][0][0][0][0]    00010000 

    INVALID BOARD : 
    
    . . . . . . . Q     [0][0][0][0][0][0][0][1]    00000001 
    . . . . . Q . .     [0][0][0][0][0][1][0][0]    00000100 
    . . . Q . . . .     [0][0][0][0][1][0][0][0]    00010000 
    . . . . . . Q .     [0][0][0][0][0][0][1][0]    00000010 
    . . . . . . Q .     [0][0][0][0][0][0][1][0]    00000010 
    . . . . Q . . .     [0][0][0][0][1][0][0][0]    00001000 
    . . Q . . . . .     [0][0][1][0][0][0][0][0]    00100000 
    . . . . Q . . .     [0][0][0][0][1][0][0][0]    00001000


"""


class EightQueens:

    """Generate all valid solutions for the n queens puzzle"""
    def queens(self, size):
        if size == 8:
            # Store the puzzle (problem) size and the number of valid solutions
            self.size = size
            self.possibilities = 0
            self.solve()
            print("=> Found", self.possibilities, "possibilities.")
            return self.possibilities
        else:
            print("=> Wrong instruction. You can only take an integer in parameter only number 8 that represent the number of the queens and the size of the board.")
            return False

    def solve(self):
        """Solve the n queens puzzle and print the number of solutions"""
        positions = [-1] * self.size
        self.put_queen(positions, 0)

    def put_queen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            self.show_full_board(positions)
            self.possibilities += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)

    def check_place(self, positions, ocuppied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(ocuppied_rows):
            if positions[i] == column or positions[i] - i == column - ocuppied_rows or positions[i] + i == column + ocuppied_rows:
                return False
        return True

    def show_full_board(self, positions):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")


def main():
    """Initialize and solve the n queens puzzle"""
    EightQueens().queens(8)

if __name__ == "__main__":
    # execute only if run as a script
    main()
