#  File: MagicSquare.py

#  Description:

#  Student's Name: Dao Ton-Nu

#  Student's UT EID: dt26435
 
#  Partner's Name: Kalab Alemu

#  Partner's UT EID: kga469

#  Course Name: CS 313E 

#  Unique Number: 52590

#  Date Created: 9/4/2021

#  Date Last Modified: 9/

import sys

# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square ( n ):
  square = [[0]*n for i in range(n)] # 2D list size nxn, filled with zeroes
  c = int(n/2) # middle column index - starting point
  r = n-1 # last row index
  nums = n*n
  for num in range(nums):
    square[r][c] = num+1
    if (r+1 > (n-1) and c+1 > (n-1)): #right corner OoB
      r-=1
    elif r+1 > (n-1): # if next place's row exceeds row limit, row OoB
      r=0
      c+=1
    elif c+1 > (n-1): # out of bounds (col)
      c=0
      r+=1
    elif (square[r+1][c+1]!=0): # if next place already has number
      r-=1
    else:
      r+=1
      c+=1
    num+=1
  return square

# Print the magic square in a neat format where the numbers
# are right justified. This is a helper function.
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
  for row in magic_square: #iterates over each row in square
    print(" ".join([str(pos) for pos in row])) # print row separated by spaces 
  return

# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# This is a helper function.
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square ( magic_square ):
  sum1 = sum(magic_square[0])

  for row in magic_square: # check that each row equals the same sum
    if sum(row) != sum1:
      return False

  for col in range(len(magic_square)): # check that each col equals same sum
    temp = 0
    for row in magic_square:
      temp+=row[col]
    if temp != sum1:
      return False

  temp1 = 0 #sum holder for right down diag
  temp2 = 0 #sum holder for left down diag
  c1=0 # col index for temp1
  c2= len(magic_square)-1 # col index for temp2
  for row in magic_square: #check that the diags equals same sum
    temp1+=row[c1]
    c1+=1
    temp2+=row[c2]
    c2-=1
  if temp1 != sum1 or temp2 != sum1:
    return False
  return True

# Input: square is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the magic square
#         if n is outside the range return 0
def sum_adjacent_numbers (square, n):
  sum_adj = 0
  r_of_n = -1
  c_of_n = -1

  r=0
  for row in square: # find indices for row, col of n in square
    if n in row:
      r_of_n = r
      c_of_n = row.index(n)
    r+=1
  if r_of_n == -1: #return 0 b/c we didn't find n in the square
    return 0

  for i in range(r_of_n-1, r_of_n+2): #loop thru the "square" around n
    for j in range(c_of_n-1, c_of_n+2):
      if -1 < i < len(square) and -1 < j < len(square): # check for in bounds
        sum_adj+=square[i][j]
  sum_adj-=n #subtract n from the sum of that mini-square

  return sum_adj

def main():
  # read the input file from stdin
  square_dim = int(sys.stdin.readline().strip())
  # create the magic square
  magic_square = make_square(square_dim)
  # print the sum of the adjacent numbers
  num = sys.stdin.readline().strip() #the first number below dimension
  while bool(num): # while num is not empty (checking for end of file)
    num = int(num)
    print(sum_adjacent_numbers(magic_square,num))
    num = sys.stdin.readline().strip()
  return

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()