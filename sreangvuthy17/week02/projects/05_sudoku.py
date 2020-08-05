"""
                                                PROJECT 05 : Sudoku Validator 

    Description :   Sudoku (数独 sūdoku) (sometimes spelled as Su Doku, but also called Number Place or Nanpure) is a puzzle that is very popular in Japan. 
                    It was created in Indianapolis in 1979 by Howard Garns and it appeared in Dell Magazines afterwards. 

                    You will write a function that take a two-dimensional lists (array) as parameter that represent a Sudoku. 
                    You function can return three different possibilities: 
                        - “​Invalid Format​” : If the sudoku format is not valid (to be valid, a Sudoku board have to be sized 9x9 and contain number between 1 and 9 only)  
                        - “Not finished” : If the sudoku format is valid BUT not finished (for example all the cases contains values and the size of the board is 9x9 but a line, columns or region is incorrect (for example 2 identical numbers on the same line/columns/region). 
                        - “Finished” : If the sudoku format is valid AND finished without any mistakes.
                    
                    More about sudoku : ​https://simple.wikipedia.org/wiki/Sudoku 
                    Sudoku generator : ​https://www.sudokuweb.org/ 

    Requirements :  ● Program must be named : ​05_sudoku.py​ and saved into​ week02/projects 
                    ● Your function must be called ​sudoku(board) 
    
    Hint :  ❖ Two-dimensional list 
            ❖ Make sure you know how to play Sudoku, if not, take some time to try, it’s à good game for your brain! 
            ❖ Try to write your program with ‘human logic’. How would you do to check if the sudoku is valid first, and then if it’s finished or not? 
            ❖ This project doesn’t require any maths skills and formulas 
            ❖ Take your time to create your function and have fun doing it. 

    Output:
            sudoku([
            [1, 9, 8, 7, 6, 5, 4, 3, 2],
            [2, 1, 9, 8, 7, 6, 5, 4, 3],
            [3, 2, 1, 9, 8, 7, 6, 5, 4],
            [4, 3, 2, 1, 9, 8, 7, 6, 5],
            [5, 4, 3, 2, 1, 9, 8, 7, 6],
            [6, 5, 4, 3, 2, 1, 9, 8, 7],
            [7, 6, 5, 4, 3, 2, 1, 9, 8],
            [8, 7, 6, 5, 4, 3, 2, 1, 9],
            [9, 8, 7, 6, 5, 4, 3, 2, 1]
            ])
            >> Not Finished



            sudoku([
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8], 
            [1, 9, 8, 3, 4, 2, 5, 6, 7], 
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1], 
            [7, 1, 3, 9, 2, 4, 8, 5, 6], 
            [9, 6, 1, 5, 3, 7, 2, 8, 4], 
            [2, 8, 7, 4, 1, 9, 6, 3, 5], 
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
            ])
            >> Finish



            sudoku([
            [1, 1, 3, 5, 7, 9, 4, 6, 8], 
            [4, 9, 1, 2, 6, 1, 3, 7, 5], 
            [7, 5, 6, 1, 8, 4, 2, 1, 9], 
            [6, 4, 4, 1, 5, 8, 7, 9, 2], 
            [5, 2, 1, 7, 1, 1, 1, 1, 1], 
            [9, 8, 7, 4, 2, 6, 5, 3, 1], 
            [2, 1, 4, 9, 3, 5, 2, 2, 7], 
            [3, 6, 5, 8, 1, 7, 9, 2, 4], 
            [8, 7, 9, 6, 4, 2, 1, 5, 3]
            ])
            >> Not Finished



            sudoku([
            [0, 12, 3, 5, 7, 9, 4, 6, 8], 
            [4, 9, 1, 2, 3, 7, 5], 
            [7, 5, 6, 1, 8, 4, 2, 1, 9], 
            [6, 4, 4, 1, 5, 8, 7, 9, 2], 
            [5, 2, 1, 7,1, 1, 1, 1, 1], 
            [9, 8, 7, 4, 2, 6, 5, 3, 1], 
            [2, 1, 4, 9, 3, 5, 2, 2, 7], 
            [3, 6, 5, 8, 1, 7, 9, 2, 4], 
            [8, 7, 9, 6, 4, 2, 1, 5, 3]
            ])
            >> Invalid Format


            sudoku([])
            >> Invalid Format


"""
    
# Defining the function/method that take (my_sudoku) parameter/augument
def sudoku(my_sudoku):
    # inside the function/method
    # Check if length of list in sudoku list is 9 or not
    if len(my_sudoku) is not 9:
        print("sudoku(" + str(my_sudoku) + ")")
        print(">> Invalid Format")
        return ">> Invalid Format"

    # Create new_list to Convert sudoku to new 3x3 sudoku
    new_list, tem1, tem2, tem3 = [], [], [], []
    for li in my_sudoku:
        # Check if each number in each list 
        if len(li) != 9:
            print("sudoku(" + str(my_sudoku) + ")")
            print(">> Invalid Format")
            return ">> Invalid Format"
        # Check if each number in range 1-9
        for number in li:
            if number > 9 or number < 1:
                print("sudoku(" + str(my_sudoku) + ")")
                print(">> Invalid Format")
                return ">> Invalid Format"
        # Add each 3 number to temp list to create a new list of new_list
        for n in range(0, 3):
            tem1.append(li[n])
            tem2.append(li[n+3])
            tem3.append(li[n+6])
        # When each temp list length is 9 add to new_list and clear temp list
        if len(tem1) == 9:
            new_list.append(tem1)
            new_list.append(tem2)
            new_list.append(tem3)
            tem1, tem2, tem3 = [], [], []

    # Loop to Check Each Row and column contain duplicate or not
    for num in range(0,9):
        for num1 in range(0,9):
            for num2 in range(num1,8):
                # Check if each row of sudoku contain duplicate or not
                if my_sudoku[num][num1] == my_sudoku[num][num2+1]:
                    print("sudoku(" + str(my_sudoku) + ")")
                    print(">> Not Finished")
                    return ">> Not Finished"
                # Check if each colmun of sudoku contain duplicate or not
                if my_sudoku[num1][num] == my_sudoku[num2+1][num]:
                    print("sudoku(" + str(my_sudoku) + ")")
                    print(">> Not Finished")
                    return ">> Not Finished"
                # Check if each row of new 3x3 sudoku contain duplicate or not
                if new_list[num][num1] == new_list[num][num2+1]:
                    print("sudoku(" + str(my_sudoku) + ")")
                    print(">> Not Finished")
                    return ">> Not Finished"

    #if Not duplicate in Row, Column or 3x3 Sudoku it is finish.
    else:
        print("sudoku(" + str(my_sudoku) + ")")
        print(">> Finish")
        return ">> Finish"


# outside the function/method
# call sudoku() function/method with passing list of list into (my_sudoku) parameter/augument
sudoku([
[1, 9, 8, 7, 6, 5, 4, 3, 2],
[2, 1, 9, 8, 7, 6, 5, 4, 3],
[3, 2, 1, 9, 8, 7, 6, 5, 4],
[4, 3, 2, 1, 9, 8, 7, 6, 5],
[5, 4, 3, 2, 1, 9, 8, 7, 6],
[6, 5, 4, 3, 2, 1, 9, 8, 7],
[7, 6, 5, 4, 3, 2, 1, 9, 8],
[8, 7, 6, 5, 4, 3, 2, 1, 9],
[9, 8, 7, 6, 5, 4, 3, 2, 1]
])

sudoku([
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8], 
[1, 9, 8, 3, 4, 2, 5, 6, 7], 
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1], 
[7, 1, 3, 9, 2, 4, 8, 5, 6], 
[9, 6, 1, 5, 3, 7, 2, 8, 4], 
[2, 8, 7, 4, 1, 9, 6, 3, 5], 
[3, 4, 5, 2, 8, 6, 1, 7, 9]
])

sudoku([
[1, 1, 3, 5, 7, 9, 4, 6, 8], 
[4, 9, 1, 2, 6, 1, 3, 7, 5], 
[7, 5, 6, 1, 8, 4, 2, 1, 9], 
[6, 4, 4, 1, 5, 8, 7, 9, 2], 
[5, 2, 1, 7, 1, 1, 1, 1, 1], 
[9, 8, 7, 4, 2, 6, 5, 3, 1], 
[2, 1, 4, 9, 3, 5, 2, 2, 7], 
[3, 6, 5, 8, 1, 7, 9, 2, 4], 
[8, 7, 9, 6, 4, 2, 1, 5, 3]
])
                                                                                                                            
sudoku([
[0, 12, 3, 5, 7, 9, 4, 6, 8], 
[4, 9, 1, 2, 3, 7, 5], 
[7, 5, 6, 1, 8, 4, 2, 1, 9], 
[6, 4, 4, 1, 5, 8, 7, 9, 2], 
[5, 2, 1, 7,1, 1, 1, 1, 1], 
[9, 8, 7, 4, 2, 6, 5, 3, 1], 
[2, 1, 4, 9, 3, 5, 2, 2, 7], 
[3, 6, 5, 8, 1, 7, 9, 2, 4], 
[8, 7, 9, 6, 4, 2, 1, 5, 3]
])

sudoku([])
