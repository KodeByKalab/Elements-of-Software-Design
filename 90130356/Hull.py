#  File: Hull.py

#  Description:

#  Student's Name: Dao Ton-Nu

#  Student's UT EID: dt26435
 
#  Partner's Name: Kalab Alemu

#  Partner's UT EID: kga469

#  Course Name: CS 313E 

#  Unique Number: 52590

#  Date Created: 9/24/2021

#  Date Last Modified: 9/26/2021

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  determinant = p.x*q.y + q.x*r.y + r.x*p.y - p.y*q.x - q.y*r.x - r.y*p.x
  # left turn: det > 0
  # straigt: det = 0
  # right: det < 0
  return determinant

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  n = len(sorted_points)

  upper_hull = []
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])
  for i in range(2, n):
      upper_hull.append(sorted_points[i])
      uh_ind = len(upper_hull) - 1
      while (len(upper_hull) >= 3) and (det(upper_hull[uh_ind-2], upper_hull[uh_ind-1], upper_hull[uh_ind]) > 0): # do not make a right turn <- det > 0
          upper_hull.pop(uh_ind-1)
          uh_ind -= 1
  
  lower_hull = []
  lower_hull.append(sorted_points[n-1]) # last point
  lower_hull.append(sorted_points[n-2]) # second to last point
  for i in range(n-3, -1, -1):
      lower_hull.append(sorted_points[i])
      lh_ind = len(lower_hull) - 1
      while (len(lower_hull) >= 3) and (det(lower_hull[lh_ind-2], lower_hull[lh_ind-1], lower_hull[lh_ind]) > 0): # do not make a right turn <- det > 0
          lower_hull.pop(lh_ind-1)
          lh_ind -= 1
  # remove duplicate points
  lower_hull.pop(0)
  lasti = len(lower_hull)-1
  lower_hull.pop(lasti)
  
  convex_hull = []
  convex_hull.extend(upper_hull)
  convex_hull.extend(lower_hull)

  return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  #FIXME
  det = 0
  last_ind = len(convex_poly)-1
  # first half of det
  for i in range(last_ind):
      det += convex_poly[i].x * convex_poly[i+1].y
  det += convex_poly[last_ind].x * convex_poly[0].y
  # second half of det
  for i in range(last_ind):
      det -= convex_poly[i].y * convex_poly[i+1].x
  det -= convex_poly[last_ind].y * convex_poly[0].x
  area = (1/2)*abs(det)
  return area

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  pointslist = [] # for the convex test
  # testing out determinant's 3 outcomes
  p = Point(3,4)
  pointslist.append(p)
  q = Point(2,7)
  pointslist.append(q)
  r = Point(8,3)
  pointslist.append(r)
  assert det(p,q,r) < 0
  p = Point(5,6)
  pointslist.append(p)
  q = Point(5,7)
  pointslist.append(q)
  r = Point(5,8)
  pointslist.append(r)
  assert det(p,q,r) == 0
  p = Point(5,5)
  pointslist.append(p)
  q = Point(6,-2)
  pointslist.append(q)
  r = Point(7,0)
  pointslist.append(r)
  assert det(p,q,r) > 0
  # finding convex hull
  pointslist_sorted = sorted(pointslist)
  hull = convex_hull(pointslist_sorted)
  for pt in hull:
    print(pt)
  # area of that hull
  print(area_poly(hull))
  # Test2 for hull and area
  pointslist = [Point(3,6), Point(3,7), Point(-6, 8), Point(2,0), Point(2,4), Point(1,-4), Point(-2,3), Point(-10, 10), Point(9,3), Point(2,5), Point(2,-14)]
  pointslist_sorted = sorted(pointslist)
  hull = convex_hull(pointslist)
  for pt in hull:
    print(pt)
  # area of that hull
  print(area_poly(hull))
  # Test3 for hull and area
  pointslist = [Point(1,4), Point(-3,8), Point(-6, 8), Point(2,3), Point(2,4), Point(1,-4), Point(-2,3), Point(-5, 6), Point(8,3), Point(3,-5), Point(2,-1)]
  pointslist_sorted = sorted(pointslist)
  hull = convex_hull(pointslist)
  for pt in hull:
    print(pt)
  # area of that hull
  print(area_poly(hull))
  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  '''
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  '''
  # get the convex hull
  convx_hull = convex_hull(sorted_points) 
  # run your test cases
  '''
  print (test_cases())
  '''
  # print your results to standard output

  # print the convex hull
  print('Convex Hull')
  for point in convx_hull:
      print(point)
  # get the area of the convex hull
  ch_area = area_poly(convx_hull)
  # print the area of the convex hull
  print('\nArea of Convex Hull = {:.1f}'.format(ch_area))

if __name__ == "__main__":
  main()