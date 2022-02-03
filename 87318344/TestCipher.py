#  File: TestCipher.py

#  Description:

#  Student's Name: Dao Ton-Nu

#  Student's UT EID: dt26435
 
#  Partner's Name: Kalab Alemu

#  Partner's UT EID: kga469

#  Course Name: CS 313E 

#  Unique Number: 52590

#  Date Created: 9/10/2021

#  Date Last Modified: 

import sys

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ): 
  rail_fence = [['-']*len(strng) for i in range(key)] #initialize the matrix with " - "

  row = -1
  direction = 1

  for col in range(len(strng)):
    row+=1*direction #will go up if direction negative, down if positive
    rail_fence[row][col] = strng[col]
    if row >= key - 1: #reaches last row, switch to up direction
      direction = -1
    if row < 1: #reaches first row, switch to down direction
      direction = 1

  encoded_str =''

  #turn matrix to string
  for rows in rail_fence: 
    for cols in rows:
      encoded_str+=cols

  encoded_strng = ''

  if strng.isalpha():
    encoded_strng = filter_string(encoded_str)
  else: #case for when strng has punctuation/symbols
    for char in encoded_str:
      if char != '-':
        encoded_strng += char

  return encoded_strng

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):

  #make a matrix like in encode
  rail_fence = [['-']*len(strng) for i in range(key)] #initialize the matrix with " - "

  row = -1
  direction = 1

  for col in range(len(strng)): #putting 'a' where chars of strng will go
    row+=1*direction #will go up if direction negative, down if positive
    rail_fence[row][col] = 'a'
    if row >= key - 1: #reaches last row, switch to up direction
      direction = -1
    if row < 1: #reaches first row, switch to down direction
      direction = 1
  
  str_i = 0
  for r in range(key): #replaces all 'a' with the next char of strng
      for c in range(len(strng)):
        if rail_fence[r][c] != '-':
          rail_fence[r][c] = strng[str_i]
          str_i+=1

  decoded_text=''
  row=-1
  direction = 1
  #loop through again using the direction changing loop to read decoded text
  for col in range(len(strng)):
    row+=1*direction #will go up if direction negative, down if positive
    decoded_text+=rail_fence[row][col] 
    if row >= key - 1: #reaches last row, switch to up direction
      direction = -1
    if row < 1: #reaches first row, switch to down direction
      direction = 1

  return decoded_text

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
  letters = ''
  for char in strng: 
    if char.isalpha(): #checks if current char is a letter
      letters+=char
  return letters.lower()

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
  new_start = ord(p) #start at pass letter
  shift = ord(s) - ord('a') #plain text char then will give how many letters to shift
  new_place = new_start + shift
  if new_place > ord('z'): #if greater than z, the remainder restarts at 'a'
    new_place = new_place-ord('z')+ord('a')-1
  letter = chr(new_place)
  return letter	

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
  shift = ord(s)-ord(p)
  if shift < 0: #if shift goes negative, go back to subtract from z
    shift+=26
  letter_place = ord('a') + shift
  letter = chr(letter_place)
  return letter	

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
  encoded_text = ''
  p_ind = 0 #index for pass phrase
  for i in range(len(strng)):
    if p_ind>=len(phrase): #checks if at end of pass phrase
      p_ind=0 #reset index for pass phrase
    encoded_text+=encode_character(phrase[p_ind],strng[i])
    p_ind+=1
  return encoded_text

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
  #should mirror encode, but with the decoder
  decoded_text = ''
  p_ind = 0 #index for pass phrase
  for i in range(len(strng)):
    if p_ind>=len(phrase): #checks if at end of pass phrase
      p_ind=0 #reset index for pass phrase
    decoded_text+=decode_character(phrase[p_ind],strng[i])
    p_ind+=1
  return decoded_text	

def main():
  # read the plain text from stdin
  plain_text = sys.stdin.readline().strip()
  # read the key from stdin
  key = int(sys.stdin.readline().strip())
  # encrypt and print the encoded text using rail fence cipher
  print(rail_fence_encode(plain_text,key))
  # read encoded text from stdin
  encoded_text = sys.stdin.readline().strip()
  # read the key from stdin
  key = int(sys.stdin.readline().strip())
  # decrypt and print the plain text using rail fence cipher
  print(rail_fence_decode(encoded_text, key))
  # read the plain text from stdin
  plain_text = sys.stdin.readline().strip()
  # read the pass phrase from stdin
  pass_phrase = sys.stdin.readline().strip()
  # encrypt and print the encoded text using Vigenere cipher
  print(vigenere_encode(plain_text,pass_phrase))
  # read the encoded text from stdin
  encoded_text = sys.stdin.readline().strip()
  # read the pass phrase from stdin
  pass_phrase = sys.stdin.readline().strip()
  # decrypt and print the plain text using Vigenere cipher
  print(vigenere_decode(encoded_text,pass_phrase))
  return

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()