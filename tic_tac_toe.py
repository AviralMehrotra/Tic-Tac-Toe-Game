import random
import os
import numpy as np

row_1=["--","--","--"]
row_2=["--","--","--"]
row_3=["--","--","--"]
grid=np.array([row_1,row_2,row_3])

check_row_1=["0","0","0"]
check_row_2=["0","0","0"]
check_row_3=["0","0","0"]
check_grid=np.array([check_row_1,check_row_2,check_row_3])

coordinates=["11","12","13","21","22","23","31","32","33"]
new_heading = "Tic Tac Toe"

def userTurn():
    player="User"
    userInput= input("\nType the coordinates where you want to input your mark (column, row): ")
    columnIndex= int(userInput[0])
    rowIndex= int(userInput[1])
    if ifFilled(rowIndex-1, columnIndex-1)== 1:
        grid[rowIndex-1][columnIndex-1]= "❌"
        boxFilled(rowIndex-1, columnIndex-1)
        checkIfWon(player)
        
    else:
        print("\nEnter the coordinates which are not filled yet")
        userTurn()
    printTTT(grid)

def computerTurn():
    player="Computer's"
    random.shuffle(coordinates)
    cords=coordinates.pop()
    compColumnIndex= int(cords[0])
    compRowIndex= int(cords[1])
    if ifFilled(compRowIndex-1, compColumnIndex-1)== 1:
        grid[compRowIndex-1][compColumnIndex-1]= "⭕"
        boxFilled(compRowIndex-1, compColumnIndex-1)
        checkIfWon(player)
    else:
        computerTurn()
    
    printTTT(grid)
    

def boxFilled(rowIndex, columnIndex):
    check_grid[rowIndex, columnIndex]="1"

def ifFilled(rowIndex, columnIndex):
    if check_grid[rowIndex, columnIndex]=="1":
        return 0
    else:
        return 1

def checkIfWon(player):
    #horizontal ways
    if grid[0,0]==grid[0,1]==grid[0,2]=="❌" or grid[0,0]==grid[0,1]==grid[0,2]=="⭕":
        print(f"{player} Wins\n")
        printTTT(grid)
        exit()
    elif grid[1,0]==grid[1,1]==grid[1,2]=="❌" or grid[1,0]==grid[1,1]==grid[1,2]=="⭕":
        print(f"{player} Wins\n")
        printTTT(grid)
        exit()
    elif grid[2,0]==grid[2,1]==grid[2,2]=="❌" or grid[2,0]==grid[2,1]==grid[2,2]=="⭕":
        print(f"{player} Wins\n")
        printTTT(grid)
        exit()
    #vertical ways
    elif grid[0,0]==grid[1,0]==grid[2,0]=="❌" or grid[0,0]==grid[1,0]==grid[2,0]=="⭕":
        print(f"{player} Wins\n")
        printTTT(grid)
        exit()
    elif grid[0,1]==grid[1,1]==grid[2,1]=="❌" or grid[0,1]==grid[1,1]==grid[2,1]=="⭕":
        print(f"{player} Wins\n")
        printTTT(grid)
        exit()
    elif grid[0,2]==grid[1,2]==grid[2,2]=="❌" or grid[0,2]==grid[1,2]==grid[2,2]=="⭕":
        print(f"{player} Wins\n")
        printTTT(grid)
        exit()
    #diagonal ways
    elif grid[0,0]==grid[1,1]==grid[2,2]=="❌" or grid[0,0]==grid[1,1]==grid[2,2]=="⭕":
        print(f"{player} Wins\n")
        printTTT(grid)
        exit()
    elif grid[0,2]==grid[1,1]==grid[2,0]=="❌" or grid[0,2]==grid[1,1]==grid[2,0]=="⭕":
        print(f"{player} Wins\n")
        printTTT(grid)
        exit()

# Function to print Tic Tac Toe
def printTTT(grid):
    print("\n")
    print("\t      |      | ")
    print("\t  {}  |  {}  |  {} ".format(grid[0,0], grid[0,1], grid[0,2]))
    print('\t______|______|______')
 
    print("\t      |      | ")
    print("\t  {}  |  {}  |  {} ".format(grid[1,0], grid[1,1], grid[1,2]))
    print('\t______|______|______')
 
    print("\t      |      | ")
    print("\t  {}  |  {}  |  {} ".format(grid[2,0], grid[2,1], grid[2,2]))
    print("\t      |      | ")
    print("\n")

def ifDraw():
    if check_grid[0,0]==check_grid[0,1]==check_grid[0,2]==check_grid[1,0]==check_grid[1,1]==check_grid[1,2]==check_grid[2,0]==check_grid[2,1]==check_grid[2,2]=="1":
        print("\t Its a draw ! ")
        exit()
    
    

os.system('cls')

print(new_heading)
print("\n\nInputs must be in the form of 11, 12, 13, 21, 22, 23, 31, 32, 33 \n")
printTTT(grid)
while True:
    print("\nYour Turn !")
    userTurn()
    ifDraw()
    print("\nComputer's Turn !")
    computerTurn()


