#Michael Han, 101157504, Assignment 5

def readLevel(num):
    '''this function takes a number as an arguement and uses that number to read the corresponding
    level file. It then reads the file into a 2D list of rows of symbols in the file. this function will except for
    error if the file with the given number does not exist'''
    try:
        #making empty gameboard
        gameboard=[]
        #opening the file + the integer the user has given
        f = open(f"levels/ascii_level{num}.txt", 'r')
        #for every line in the file
        for line in f:
            #get rid of \n
            line = line.strip("\n")
            #add the line as a list of symbols to gameboard
            gameboard.append(list(line))
        #closes file
        f.close()
        #returns the 2D list of symbols
        return gameboard

    except:
        return print("Please try again")
        exit()

def displayBoard(lis):
    '''this function takes in the 2D list of symbols as an arguement, and displays the 2D list
    as a board with row and column numbers (row and columns are adjusted accordingly)'''
    #adding row numbers
    rowNumbers = "   "
    for i in range(len(lis[0])):
        if len(str(i))==1:
            rowNumbers+=str(i)
        else:
            rowNumbers+=str(i%10)
    #printing row numbers
    print(rowNumbers)

    #adding dashed lines
    dash = "   "
    #for the length of rowNumbers - 3 spaces at the start
    for i in range(len(rowNumbers)-3):
        dash+="-"
    print(dash)

    #adding column numbers and row of symbols
    for i in range(len(lis)):
        #making empty string
        string=""
        #adding all elements of sublist to string
        for j in range(len(lis[i])):
            string+=lis[i][j]
        #printing a 0 infront of 1 digit row numbers and printing string of the line
        if len(str(i))==1:
            print(f"0{i}|{string}")
        #printing row number and printing string of the line
        else:
            print(f"{i}|{string}")


def getUserAction(maxRow,maxColumn):
    '''this function takes the max number of rows and columns as arguements and asks for user input for
    symbols (checks if it's a valid symbol), row (checks if it's a valid row), and column(checks if it's a valid column)
    then it returns a list containing the symbol, row and column'''
    action=[]
    #getting user input for symbol, looping until user enters valid symbol
    while True:
        inputSym=input("Please enter a symbol: ")
        #if the user input is one of these symbols
        if inputSym=='&' or inputSym=='@' or inputSym=='#' or inputSym=='%':
            #append user's symbol into action, end loop
            action.append(inputSym)
            break
        #if user input is not valid
        else: 
            print("Please enter ONE of these symbols: & @ # %")
    #getting user input for row, looping until user enters valid symbol
    while True:
        try:
            row=input(f"Please enter a row [0, {maxRow-1}]: ")
            #if user enters a row that's greater than the max row
            if int(row) > maxRow-1:
                print(f"Bad row input, please enter a row from [0, {maxRow-1}]: ")
            #if user enters number less than 0
            elif int(row) < 0:
                print(f"Bad row input, please enter a row from [0, {maxRow-1}]: ")
            #if user enters valid row
            else:
                #append the user's row into action, end loop
                action.append(int(row))
                break
        except:
            print("Please enter a number")
    #getting user input for column, looping until user enters a valid symbol
    while True:
        try:
            column=input(f"Please enter a column [0, {maxColumn-1}]: ")
            #if user enters a colmun that's greater than the max column
            if int(column) > maxColumn-1:
                print(f"Bad row input, please enter a row from [0, {maxColumn-1}]: ")
            #if user enters a number less than 0
            elif int(column) < 0:
                print(f"Bad row input, please enter a row from [0, {maxColumn-1}]: ")
            #if user enters a valid column
            else:
                #append user's column into action, end loop
                action.append(int(column))
                break
        except:
            print("Please enter a number")
    return action
    

def fill(board,targetSym,inputSym,row,column):
    '''this function changes all continguous symbols to the user's symbol (starting with user's
    given location). It takes the board, the target symbol (calculated by the user's given location),
    the symbol the user wants to change it to, and the row and column.
    If the symbol at given location is already the symbol the user is trying to
    change it to, it just ends the function, and counts it as a move. If the symbol at given location needs to be changed, it will
    first check to see if the symbol at location isn't already the input symbol, and it will also check that it's indeed the target symbol
    it will change the symbol to the input symbol, and call the functions 4 more times, checking each adjacent location. It will keep
    recursively doing this until all adjacent symbols are changed to the input symbol'''
    
    #if row is less than 0
    if row < 0:
        pass
    #if column is less than 0
    elif column < 0:
        pass
    #if row is bigger than the max number of rows
    elif row > len(board)-1:
        pass
    #if column is bigger than the max number if columns
    elif column > len(board[0])-1:
        pass
    #base cases
    else:
        #if symbol at row,column already is input symbol
        if board[row][column]==inputSym:
            return
        #if symbol at row,column is not the target symbol
        if board[row][column]!=targetSym:
            pass
    
    #recursive cases
    #if symbol needs to be changed (if the location is not the input symbol and is the target symbol)
        if board[row][column]!=inputSym and board[row][column]==targetSym:
            board[row][column]=inputSym
            #for symbol right of current location
            fill(board,targetSym,inputSym,row+1,column)
            #for symbol left of current location
            fill(board,targetSym,inputSym,row-1,column)
            #for symbol above current location
            fill(board,targetSym,inputSym,row,column+1)
            #for symbol below current location
            fill(board,targetSym,inputSym,row,column-1)
    
    

def main():
    '''this function is the function that runs the game. it calls on the other functions
    for reading level, displaying board, getting the users action and changing the symbols
    at the end of the game, it will tell you the total moves it took for you to complete the game
    and it will ask you if you want to play again. If yes, the game will restart, if no, the game will end'''
    playAgain = True
    while playAgain == True:
        print("welcome to ASCII Fill!")
        totalMoves=0
        #for all 5 levels
        for l in range(0,5):
            print(f"Level {l+1}")
            #reads gameboard of current level
            gameboard = readLevel(l+1)
            #sets number of moves for current level
            moves=0
            #not solved
            notSolved=True
            #while it's not solved
            while notSolved == True:
                #printing gameboard
                displayBoard(gameboard)
                #calling getUserAction to get user action
                action = getUserAction(len(gameboard),len(gameboard[0]))
                #setting row and column to action[1] and action[2] respectively
                row = action[1]
                column = action[2]
                #finding targetSym (at row and column)
                targetSym = gameboard[row][column]
                #calling fill function to change board 
                fill(gameboard, targetSym, action[0], action[1], action[2])
                #adds one move
                moves+=1
                #setting the symbol in top left corner to check if all symbols match
                check=gameboard[0][0]
                #checking if every symbol is the same
                for i in range (0, len(gameboard)):
                    #for symbol in each sublist (row)
                    for symbol in gameboard[i]:
                        #if symbol does not equal check
                        if symbol!=check:
                            solved='n'
                            break
                        #if symbols are the same
                        else:
                            solved='y'
                #if solved is 'y', the current level will end
                if solved == 'y':
                    notSolved=False
            #shows the current level's board one last time
            displayBoard(gameboard)
            #tells user the number of moves it took to complete level
            print(f"Level {l+1} completed in {moves} moves")
            #adding moves for this level to total moves
            totalMoves+=moves
        #after all 5 levels
        #setting initial validAns = True    
        validAns=True  
                      
        while validAns == True:
            ans = input("Would you like to play again? (yes or no)")
            #if ans is yes, end loop
            if ans == 'yes':
                validAns = False
            #if ans is no, end loop
            elif ans == 'no':
                validAns = False
            #keep looping until valid answer is given
            else:
                print("Please enter yes or no")
                
        #if ans is yes, game will restart
        if ans == 'yes':
            playAgain = True
            print(f"Completed with a total of {totalMoves} moves")
            
        #if ans is no, game will end
        elif ans == 'no':
            playAgain = False
            print(f"Completed with a total of {totalMoves} moves")        

        
            
                        
#calling main to start game
main()