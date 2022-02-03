

import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = x
      self.y = y
      self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      return ("({:.1f}, {:.1f}, {:.1f})".format(self.x, self.y, self.z)) 

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      return math.hypot(self.x - other.x, self.y - other.y,self.z-other.z)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      return ((self.x == other.x) and (self.y == other.y) and (self.z == other.z))

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
      self.center = Point(x,y,z)
      self.radius = radius

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
      return ("Center: {}, Radius: {:.1f}".format(self.center, self.radius))

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
      return 4 * math.pi * (self.radius**2)

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
      return (4/3.0) * math.pi * (self.radius ** 3)

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return self.center.distance(p) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
      dist_centers = self.center.distance(other.center)
      return (dist_centers + other.radius) < self.radius
  # determine if another Sphere strictly outside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_outside_sphere (self,other):
      dist_centers = self.center.distance(other.center)
      return (dist_centers - other.radius) > self.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      for i in range(len(a_cube.vertices)):
          if not self.is_inside_point(a_cube.vertices[i]):
              return False
      return True
  # determine if a Cube is strictly outside this Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_outside_cube (self,a_cube):
      for i in range(len(a_cube.vertices)): #check any vertices in sphere
          if self.is_inside_point(a_cube.vertices[i]):
              return False
      if self.is_inside_point(a_cube.center): #check if center of cube is in sphere
          return False
      if a_cube.is_inside_sphere(self): # check if sphere inside cube (since cube pts and center may all be outside sphere)
          return False
      return True 

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
      #cylinder as a box
      vertices = []
      xi = 1
      yi = 1
      zi = 1
      # all 8 vertices of box
      for i in range(2):
          for j in range(2):
              for k in range(2):
                  vertices.append(Point(a_cyl.center.x+xi*(a_cyl.radius),a_cyl.center.y+yi*(a_cyl.radius),a_cyl.center.z+zi*(a_cyl.height/2)))
                  zi*=-1
              yi*=-1
          xi*=-1
      #get vertices of box, iterate as points inside sphr
      for i in range(len(vertices)):
          if not self.is_inside_point(vertices[i]):
              return False
      return True

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
      if self.is_inside_sphere(other) or self.is_outside_sphere(other):
          return False
      return True

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
      if self.is_inside_cube(a_cube) or self.is_outside_cube(a_cube) or a_cube.is_inside_sphere(self):
          return False
      return True

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
      side = self.radius*2/math.sqrt(3)
      ccsb_cube = Cube(self.center.x,self.center.y,self.center.z, side)
      return ccsb_cube

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
      self.center = Point(x,y,z)
      self.side=side
      self.vertices = []
      xi = 1
      yi = 1
      zi = 1
      # all 8 vertices of cube - note that order of vertices will be 0-RBkTop, 1-RBkBot, 2-RFrntTop, 3-RFrntBot, 4-LBkTop, 5-LBkBot, 6-LFrntTop, 7-LBkBot
      for i in range(2):
          for j in range(2):
              for k in range(2):
                  self.vertices.append(Point(x+xi*(side/2),y+yi*(side/2),z+zi*(side/2)))
                  zi*=-1
              yi*=-1
          xi *= -1

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
      return ("Center: {}, Side: {:.1f}".format(self.center, self.side))

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
      return 6 * (self.side ** 2)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
      return self.side ** 3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
      xmax = self.center.x + self.side/2
      xmin = self.center.x - self.side/2
      ymax = self.center.y + self.side/2
      ymin = self.center.y - self.side/2
      zmax = self.center.z + self.side/2
      zmin = self.center.z - self.side/2
      return (xmin<p.x<xmax) and (ymin<p.y<ymax) and (zmin<p.z<zmax) 

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      dist_centers_x = abs(self.center.x - a_sphere.center.x)
      dist_centers_y = abs(self.center.y - a_sphere.center.y)
      dist_centers_z = abs(self.center.z - a_sphere.center.z)
      return ((dist_centers_x+a_sphere.radius) < self.side/2) and ((dist_centers_y+a_sphere.radius) < self.side/2) and ((dist_centers_z+a_sphere.radius) < self.side/2)

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
      for i in range(len(other.vertices)):
          if not self.is_inside_point(other.vertices[i]):
              return False
      return True
  # determine if another Cube is strictly outside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_outside_cube (self, other):
      for i in range(len(other.vertices)):
          if self.is_inside_point(other.vertices[i]):
              return False
      if self.is_inside_point(other.center):
          return False
      return True

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
      dist_centers_x = abs(self.center.x - a_cyl.center.x)
      dist_centers_y = abs(self.center.y - a_cyl.center.y)
      dist_centers_z = abs(self.center.z - a_cyl.center.z)
      return ((dist_centers_x+a_cyl.radius) < self.side/2) and ((dist_centers_y+a_cyl.radius) < self.side/2) and ((dist_centers_z+a_cyl.height/2) < self.side/2)

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
      if self.is_inside_cube(other) or (self.is_outside_cube(other) and other.is_outside_cube(self)) or other.is_inside_cube(self):
          return False
      return True

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
      l=0
      w=0
      h=0    
      if self.does_intersect_cube(other):
          # find rightmost cube, then compute length
          if (self.vertices[0].x > other.vertices[0].x) or ((self.vertices[0].x == other.vertices[0].x) and (self.vertices[4].x > other.vertices[0].x)):
              #self is rightmost so length = other max x - self min x
              l = other.vertices[0].x-self.vertices[4].x
          else:
              #other is rightmost so length = self max x - other min x
              l = self.vertices[0].x-other.vertices[4].x
          # find back-most cube (positive y), then compute width
          if (self.vertices[0].y > other.vertices[0].y) or ((self.vertices[0].y == other.vertices[0].y) and (self.vertices[2].y > other.vertices[0].y)):
              w = other.vertices[0].y-self.vertices[2].y
          else:
              w = self.vertices[0].y-other.vertices[2].y
          # find topmost cube, then compute height
          if (self.vertices[0].z > other.vertices[0].z) or ((self.vertices[0].z == other.vertices[0].z) and (self.vertices[1].z > other.vertices[0].z)):
              h = other.vertices[0].z-self.vertices[1].z
          else:
              h = self.vertices[0].z-other.vertices[1].z
      return l*w*h

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
      #half side cube is radius of sphere
      radius = self.side/2
      insc_sphr = Sphere(self.center.x, self.center.y, self.center.z, radius)
      return insc_sphr

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.center = Point(x,y,z)
      self.radius = radius
      self.height = height

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      return ("Center: {}, Radius: {:.1f}, Height: {:.1f}".format(self.center, self.radius, self.height))
      
  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
      return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius**2))

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
      return (math.pi * (self.radius ** 2) * self.height)

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
      # check if point's xy component distance from center is less than radius
      if not (math.hypot(self.center.x-p.x,self.center.y-p.y)) < self.radius:
          return False
      # check that p.z is bt self.z-(height/2) and self.z+(height/2)
      if not self.center.z-(self.height/2)< p.z <self.center.z+(self.height/2):
          return False
      return True

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      dist_centers_xy = math.hypot(self.center.x-a_sphere.center.x, self.center.y-a_sphere.center.y)
      dist_centers_z = abs(self.center.z - a_sphere.center.z)
      return ((dist_centers_xy + a_sphere.radius) < self.radius) and ((dist_centers_z + a_sphere.radius) < self.height/2 )
      
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      for i in range(len(a_cube.vertices)):
          if not self.is_inside_point(a_cube.vertices[i]):
              return False
      return True

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
      dist_centers_xy = math.hypot(self.center.x-other.center.x, self.center.y-other.center.y)
      dist_centers_z = abs(self.center.z - other.center.z)
      return ((dist_centers_xy + other.radius) < self.radius) and ((dist_centers_z + other.height/2) < self.height/2 )
  # determine if another Cylinder is strictly outside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_outside_cylinder (self, other): 
      dist_centers_xy = math.hypot(self.center.x-other.center.x, self.center.y-other.center.y)
      dist_centers_z = abs(self.center.z - other.center.z)
      return ((dist_centers_xy - other.radius) > self.radius) or ((dist_centers_z - other.height/2) > self.height/2 )

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
      if self.is_inside_cylinder(other) or self.is_outside_cylinder(other):
          return False
      return True

def main():
  # read data from standard input
  line = sys.stdin.readline()
  data = line.split()
  # read the coordinates of the first Point p
  x = float(data[0])
  y = float(data[1])
  z = float(data[2])
  # create a Point object 
  p = Point(x,y,z)
  # read the coordinates of the second Point q
  line = sys.stdin.readline()
  data = line.split()
  x = float(data[0])
  y = float(data[1])
  z = float(data[2])
  # create a Point object
  q = Point(x,y,z)
  # read the coordinates of the center and radius of sphereA
  line = sys.stdin.readline()
  data = line.split()
  x = float(data[0])
  y = float(data[1])
  z = float(data[2])
  r = float(data[3])
  # create a Sphere object 
  sphereA = Sphere(x,y,z,r)
  # read the coordinates of the center and radius of sphereB
  line = sys.stdin.readline()
  data = line.split()
  x = float(data[0])
  y = float(data[1])
  z = float(data[2])
  r = float(data[3])
  # create a Sphere object
  sphereB = Sphere(x,y,z,r)
  # read the coordinates of the center and side of cubeA
  line = sys.stdin.readline()
  data = line.split()
  x = float(data[0])
  y = float(data[1])
  z = float(data[2])
  s = float(data[3])
  # create a Cube object 
  cubeA = Cube(x,y,z,s)
  # read the coordinates of the center and side of cubeB
  line = sys.stdin.readline()
  data = line.split()
  x = float(data[0])
  y = float(data[1])
  z = float(data[2])
  s = float(data[3])
  # create a Cube object 
  cubeB = Cube(x,y,z,s)
  # read the coordinates of the center, radius and height of cylA
  line = sys.stdin.readline()
  data = line.split()
  x = float(data[0])
  y = float(data[1])
  z = float(data[2])
  r = float(data[3])
  h = float(data[4])
  # create a Cylinder object 
  cylA = Cylinder(x,y,z,r,h)
  # read the coordinates of the center, radius and height of cylB
  line = sys.stdin.readline()
  data = line.split()
  x = float(data[0])
  y = float(data[1])
  z = float(data[2])
  r = float(data[3])
  h = float(data[4])
  # create a Cylinder object
  cylB = Cylinder(x,y,z,r,h)
  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
  o = Point()
  print('Distance of Point p from the origin {} greater than the distance of Point q from the origin'.format('is' if p.distance(o)>q.distance(o) else 'is not'))  
  # print if Point p is inside sphereA
  print('Point p {} inside sphereA'.format('is' if sphereA.is_inside_point(p) else 'is not'))
  # print if sphereB is inside sphereA
  print('sphereB {} inside sphereA'.format('is' if sphereA.is_inside_sphere(sphereB) else 'is not'))
  # print if cubeA is inside sphereA
  print('cubeA {} inside sphereA'.format('is' if sphereA.is_inside_cube(cubeA) else 'is not'))
  # print if cylA is inside sphereA
  print('cylA {} inside sphereA'.format('is' if sphereA.is_inside_cyl(cylA) else 'is not'))
  # print if sphereA intersects with sphereB
  print('sphereA {} intersect sphereB'.format('does' if sphereA.does_intersect_sphere(sphereB) else 'does not'))
  # print if cubeB intersects with sphereB
  print('cubeB {} intersect sphereB'.format('does' if sphereB.does_intersect_cube(cubeB) else 'does not'))
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  print('Volume of the largest Cube that is circumscribed by sphereA {} greater than the volume of cylA'.format('is' if sphereA.circumscribe_cube().volume() > cylA.volume() else 'is not'))
  # print if Point p is inside cubeA
  print('Point p {} inside cubeA'.format('is' if cubeA.is_inside_point(p) else 'is not'))
  # print if sphereA is inside cubeA
  print('sphereA {} inside cubeA'.format('is' if cubeA.is_inside_sphere(sphereA) else 'is not'))
  # print if cubeB is inside cubeA
  print('cubeB {} inside cubeA'.format('is' if cubeA.is_inside_cube(cubeB) else 'is not'))
  # print if cylA is inside cubeA
  print('cylA {} inside cubeA'.format('is' if cubeA.is_inside_cylinder(cylA) else 'is not'))
  # print if cubeA intersects with cubeB
  print('cubeA {} intersect cubeB'.format('does' if cubeA.does_intersect_cube(cubeB) else 'does not'))
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  print('Intersection volume of cubeA and cubeB {} greater than the volume of sphereA'.format('is' if cubeA.intersection_volume(cubeB) > sphereA.volume() else 'is not'))
  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  print('Surface area of the largest Sphere object inscribed by cubeA {} greater than the surface area of cylA'.format('is' if cubeA.inscribe_sphere().area() > cylA.area() else 'is not'))
  # print if Point p is inside cylA
  print('Point p {} inside cylA'.format('is' if cylA.is_inside_point(p) else 'is not'))
  # print if sphereA is inside cylA
  print('sphereA {} inside cylA'.format('is' if cylA.is_inside_sphere(sphereA) else 'is not'))
  # print if cubeA is inside cylA
  print('cubeA {} inside cylA'.format('is' if cylA.is_inside_cube(cubeA) else 'is not'))
  # print if cylB is inside cylA
  print('cylB {} inside cylA'.format('is' if cylA.is_inside_cylinder(cylB) else 'is not'))
  # print if cylB intersects with cylA
  print('cylB {} intersect cylA'.format('does' if cylB.does_intersect_cylinder(cylA) else 'does not'))
  return

if __name__ == "__main__":
  main()
