#  File: WordSearch.py

#  Description:

#  Student Name: Dao Ton-Nu

#  Student UT EID: dt26435  

#  Partner Name: Kalab Alemu

#  Partner UT EID: dt26435

#  Course Name: CS 313E 

#  Unique Number: 52590

#  Date Created: 8/29/2021

#  Date Last Modified: 9/3/2021

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    grid_size = sys.stdin.readline() #read in the first number
    grid_size = int(grid_size.strip())
    grid = [[0]*grid_size for i in range(grid_size)] #sets up a 2D list of zeroes the size of the grid
    currLn =''
    sys.stdin.readline()
    for r in range(grid_size):
        currLn = sys.stdin.readline() #reads current grid row
        currLn = currLn.replace(" ","")
        for c in range(grid_size):
            grid[r][c]=currLn[c] #placing letters in 2D list
    sys.stdin.readline()
    num_words = sys.stdin.readline() #reads number of words
    num_words = int(num_words.strip())
    wlist = [0]*num_words #1D list of zeroes
    for i in range(num_words):
        wlist[i]=sys.stdin.readline().strip() #putting words in 1D list
    return grid, wlist
            

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid
def find_word (grid, word):
    #list of locations found, if any, for each function
    locs = [horizontal_forward_find(grid,word), horizontal_backward_find(grid,word), 
    vertical_down_find(grid,word), vertical_up_find(grid,word), diag_rightdown_find(grid,word), 
    diag_leftdown_find(grid,word), diag_leftup_find(grid,word), diag_rightup_find(grid,word)]
    for loc in locs:
        if loc:
            return loc
    return (0,0)

#Search for the word from left to right, a row at a time
#Note: 1st 4 functions have similar code w/ similar functions, as commented here. 
def horizontal_forward_find(grid,word):
    curr_string = ''
    r = 0
    curr_ind=0
    while r < len(grid):
        loc = () #location
        c=0 #reset column index to 0 for each new row
        while c < len(grid[0]) and curr_ind < len(word):
            if grid[r][c] == word[curr_ind]:
                if len(curr_string)==0: #assign location the start of the word
                    loc = (r+1,c+1)
                curr_string+=grid[r][c]
                curr_ind+=1
                c+=1
                if curr_string == word:
                    return loc
            else:
                curr_ind = 0
                if len(curr_string)==0: #to avoid skipping a letter like the second C of CCAT for CAT
                    c+=1
                curr_string =''#reset while in the loop
        curr_string='' #reset while out of the loop in case of a letter still in the temp curr_string
        curr_ind = 0 #reset word index
        r+=1 #next row
    return   

#Search for the word from right to left, a row at a time
def horizontal_backward_find(grid,word):
    curr_string = ''
    r = 0
    curr_ind = 0
    while r < len(grid):
        loc = ()
        c=len(grid[0])-1 #reset to the last index for each new row
        while c > -1 and curr_ind < len(word):
            if grid[r][c] == word[curr_ind]:
                if len(curr_string)==0:
                    loc = (r+1,c+1)
                curr_string+=grid[r][c]
                curr_ind+=1
                c-=1
                if curr_string == word:
                    return loc
            else:
                curr_ind = 0
                if len(curr_string)==0:
                    c-=1
                curr_string =''
        curr_string=''
        curr_ind = 0
        r+=1
    return

#Search for the word downward, a column at a time
def vertical_down_find(grid,word):
    curr_string = ''
    c = 0
    curr_ind = 0
    while c < len(grid[0]):
        loc = ()
        r = 0
        while r < len(grid) and curr_ind < len(word):
            if grid[r][c] == word[curr_ind]:
                if len(curr_string) == 0:
                    loc = (r+1,c+1)
                curr_string += grid[r][c]
                curr_ind +=1
                r += 1
                if curr_string == word:
                    return loc
            else:
                curr_ind = 0
                if len(curr_string) == 0:
                    r += 1
                curr_string = ''
        curr_string=''
        curr_ind = 0
        c+=1
    return

#Search for the word upward, a column at a time
def vertical_up_find(grid,word):
    curr_string = ''
    c = 0
    curr_ind = 0
    while c < len(grid[0]):
        loc = ()
        r = len(grid)-1
        while r > -1 and curr_ind < len(word):
            if grid[r][c] == word[curr_ind]:
                if len(curr_string) == 0:
                    loc = (r+1,c+1)
                curr_string += grid[r][c]
                curr_ind +=1
                r -= 1
                if curr_string == word:
                    return loc
            else:
                curr_ind = 0
                if len(curr_string) == 0:
                    r -= 1
                curr_string = ''
        curr_string=''
        curr_ind = 0
        c+=1
    return

#Search for the word diagonally down and to the right, going by letter starting from top left
#The next 4 functions are for diagonals. They have similar parts to the verticals and horizontals, but also 
#their own functions similar to one another, commented under this diagonal function.
def diag_rightdown_find(grid,word):
    curr_string = ''
    r=0
    c=0
    curr_ind=0
    while r < len(grid):
        loc = ()
        x=r #set temp indices that can be reset to original starting location if the word was incompleted
        y=c
        while y < len(grid[0]) and x < len(grid) and curr_ind < len(word): #avoid out of bounds for temp indices and word index
            if grid[x][y] == word[curr_ind]:
                if len(curr_string)==0:
                    loc = (x+1,y+1)
                curr_string+=grid[x][y]
                curr_ind+=1
                x+=1 #diagonal: will increment both indices when finding a match
                y+=1
                if curr_string == word:
                    return loc
            else:
                x = r #reset the row to current searching row
                curr_ind = 0 #reset word index
                c+=1 #unlike vert. or hor., diag. search isn't skipped if column indexes in this situation
                y = c #y is "reset" to the next column over
                curr_string =''
        curr_string=''
        curr_ind = 0
        r+=1 #must increment to next row
        c=0 #and reset the column index
    return

#Search for the word diagonally down and to the left, going by letter starting from top right
def diag_leftdown_find(grid,word):
    curr_string = ''
    r=0
    c=len(grid[0])-1
    curr_ind=0
    while r < len(grid):
        loc = ()
        x=r
        y=c
        while y >-1 and x < len(grid) and curr_ind < len(word):
            if grid[x][y] == word[curr_ind]:
                if len(curr_string)==0:
                    loc = (x+1,y+1)
                curr_string+=grid[x][y]
                curr_ind+=1
                x+=1
                y-=1
                if curr_string == word:
                    return loc
            else:
                x = r
                curr_ind = 0
                c-=1
                y = c
                curr_string =''
        curr_string=''
        curr_ind = 0
        r+=1
        c=len(grid[0])-1
    return

#Search for the word diagonally up and to the left, going by letter starting from bottom right
def diag_leftup_find(grid,word):
    curr_string = ''
    r=len(grid)-1
    c=len(grid[0])-1
    curr_ind=0
    while r >-1:
        loc = ()
        x=r
        y=c
        while y > -1 and x > -1 and curr_ind < len(word):
            if grid[x][y] == word[curr_ind]:
                if len(curr_string)==0:
                    loc = (x+1,y+1)
                curr_string+=grid[x][y]
                curr_ind+=1
                x-=1
                y-=1
                if curr_string == word:
                    return loc
            else:
                x = r
                curr_ind = 0
                c-=1
                y = c
                curr_string =''
        curr_string=''
        curr_ind = 0
        r-=1
        c=len(grid[0])-1
    return

#Search for the word diagonally up and to the left, going by letter starting from bottom left
def diag_rightup_find(grid,word):
    curr_string = ''
    c=0
    r=len(grid)-1
    curr_ind=0
    while c < len(grid[0]):
        loc = ()
        x=r
        y=c
        while y <len(grid[0]) and x > -1 and curr_ind < len(word):
            if grid[x][y] == word[curr_ind]:
                if len(curr_string)==0:
                    loc = (x+1,y+1)
                curr_string+=grid[x][y]
                curr_ind+=1
                x-=1
                y+=1
                if curr_string == word:
                    return loc
            else:
                y = c
                curr_ind = 0
                r-=1
                x = r
                curr_string =''
        curr_string=''
        curr_ind = 0
        c+=1
        r=len(grid[0])-1
    return
    
def main():
  # read the input file from stdin
  word_grid, word_list = read_input()
  # find each word and print its location
  for word in word_list:
    location = find_word (word_grid, word)
    print(word + ": " + str(location))

if __name__ == "__main__":
  main()