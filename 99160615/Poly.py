#  File: Poly.py

#  Description:

#  Student Name: Kalab Alemu 

#  Student UT EID: kga469 

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:
import sys
class Link (object):
  def __init__(self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    link_new = Link(coeff, exp, next = None)
    if self.first == None:
      self.first = link_new
      return 
    
    elif self.first.exp < link_new.exp:
      link_new.next = self.first
      self.first = link_new  
      return
    
    elif self.first.exp == link_new.exp:
      self.first.coeff = self.first.coeff + link_new.coeff
      if self.first.coeff == 0:
        self.first = self.first.next
      return
    
    else:    
      curr = self.first
      while link_new.exp <= curr.exp:
        if curr.next == None:
          curr.next = link_new
          return
        if link_new.exp == curr.next.exp:
          curr.next.coeff += link_new.coeff
          if curr.next.coeff == 0:
            curr.next = curr.next.next
          return
        if link_new.exp > curr.next.exp:
          link_new.next = curr.next
          curr.next = link_new
          return
        elif link_new.exp < curr.next.exp:
          curr = curr.next

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    new_poly = LinkedList() 
    curr = self.first
    while curr is not None:
      new_poly.insert_in_order(curr.coeff, curr.exp)
      curr = curr.next   
    curr = p.first      
    while curr is not None:
      new_poly.insert_in_order(curr.coeff, curr.exp)
      curr = curr.next         
    return str(new_poly)

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    first_curr = self.first
    second_curr = p.first
    final_poly = LinkedList()
    while second_curr is not None:
      while first_curr is not None:
        exp_prod = first_curr.exp + second_curr.exp        
        coeff_prod = first_curr.coeff*second_curr.coeff
        final_poly.insert_in_order(coeff_prod, exp_prod)
        first_curr = first_curr.next
      first_curr = self.first
      second_curr = second_curr.next
    return str(final_poly)

  # create a string representation of the polynomial
  def __str__ (self):
    curr = self.first
    str_output = str()
    str_output = str_output + str(curr)
    if curr.next is not None:
      while curr.next is not None:
        str_output = str_output + ' + ' + str(curr.next)
        curr = curr.next
    return str_output

def main():
  
  # read data from file poly.in from stdin
  line = sys.stdin.readline()
  strip_line = line.strip()
  n1 = int(strip_line)

  # create polynomial p
  p = LinkedList()
  for idx in range(n1):
      line = sys.stdin.readline()
      line_strip = line.strip() 
      coeffexp = line_strip.split(' ')
      p.insert_in_order(int(coeffexp[0]), int(coeffexp[1]))

  # create polynomial q
  null = sys.stdin.readline()
  line = sys.stdin.readline()
  striped_line = line.strip()
  n2 = int(striped_line)
  q = LinkedList()
  for idx in range(n2):
      line = sys.stdin.readline()
      line_strip = line.strip()
      coeffexp = line_strip.split(' ')
      q.insert_in_order(int(coeffexp[0]), int(coeffexp[1]))
    
  # get sum of p and q and print sum
  print(p.add(q))
  # get product of p and q and print product
  print(p.mult(q))
if __name__ == "__main__":
  main()