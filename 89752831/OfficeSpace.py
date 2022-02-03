#  File: OfficeSpace.py

#  Description:

#  Student's Name: Dao Ton-Nu

#  Student's UT EID: dt26435
 
#  Partner's Name: Kalab Alemu

#  Partner's UT EID: kga469

#  Course Name: CS 313E 

#  Unique Number: 52590

#  Date Created: 9/21/2021

#  Date Last Modified: 9/24/2021

import sys

class Building (object):
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.office = [] # note that grid is y rows and x columns
      for i in range(y):
          row = []
          for j in range(x):
              row.append(0)
          self.office.append(row)

class Employee (object):
    def __init__(self, name, x1, y1, x2, y2):
        self.name = name
        self.cubicle_req = (x1, y1, x2, y2)

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
  return (rect[2]-rect[0])*(rect[3]-rect[1])

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  overlap_rect = [0,0,0,0]
  # 1st iteration: check if rectangles are horizontally separate
  # 2nd iteration: check if rectangles are vertically separate
  for i in range(2):
      if (rect1[i+2] <= rect2[i]) or (rect2[i+2] <= rect1[i]):
          return tuple(overlap_rect)
  # guarantees that (rect1[2] > rect2[0] or rect2[2] > rect1[0]) and (rect1[3] > rect2[1] or rect2[3] > rect1[1])
  
  # 1st iter: set x values
  # 2nd iter: set y values
  for i in range(2):
    if rect1[i+2] > rect2[i+2]: #rect1 max > rect2 max
      overlap_rect[i+2] = rect2[i+2]
    else: #rect 1 max <= rect2 max
      overlap_rect[i+2] = rect1[i+2]
    if rect1[i] < rect2[i]: # rect1 min < rect2 min
      overlap_rect[i] = rect2[i]
    else: # rect1 min is >= rect2 min aka rect1 b/t rect2
      overlap_rect[i] = rect1[i]

  return tuple(overlap_rect)

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
  cnt = 0
  for i in range(len(bldg)):
      for j in range(len(bldg[0])):
          if bldg[i][j] == 0:
              cnt += 1
  return cnt

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
  cnt = 0
  for i in range(len(bldg)):
      for j in range(len(bldg[0])):
          if bldg[i][j] > 1:
              cnt += 1
  return cnt

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
  cnt = 0
  for r in range(len(bldg) - rect[3], len(bldg) - rect[1]): # y2 to y1 (rmbr grid 0,0 in left corner)
      for c in range(rect[0], rect[2]): #x1 to x2
          if bldg[r][c] == 1:
              cnt += 1 
  return cnt

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
  new_office = office
  for request in cubicles:
    for r in range(len(office) - request[3], len(office) - request[1]): # y2 to y1 (rmbr grid 0,0 in left corner)
      for c in range(request[0], request[2]): #x1 to x2
          new_office[r][c]+=1
  return new_office

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases
  return "all test cases passed"

def main():
  # read the data
  line = sys.stdin.readline()
  data = line.split()
  office_x = int(data[0])
  office_y = int(data[1])
  officespace = Building(office_x, office_y)
  num_employees = int(sys.stdin.readline().strip())
  employees = []
  for i in range(num_employees): # making list of Employees
      line = sys.stdin.readline()
      data = line.split()
      name = data[0]
      x1 = int(data[1])
      y1 = int(data[2])
      x2 = int(data[3])
      y2 = int(data[4])
      curr_employee = Employee(name, x1, y1, x2, y2)
      employees.append(curr_employee)
  cubicles = []
  for worker in employees:
      cubicles.append(worker.cubicle_req)
  # run your test cases
  officespace.office = request_space(officespace.office, cubicles)
  '''
  print (test_cases())
  '''

  # print the following results after computation

  # compute the total office space
  print('Total', area((0, 0, office_x, office_y)))
  # compute the total unallocated space
  print('Unallocated', unallocated_space(officespace.office))
  # compute the total contested space
  print('Contested', contested_space(officespace.office))
  # compute the uncontested space that each employee gets
  for worker in employees:
      print(worker.name, uncontested_space(officespace.office, worker.cubicle_req))

if __name__ == "__main__":
  main()