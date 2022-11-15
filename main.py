#        Name:Ashley Jagai 
# Course Info: CSC111 - Fall 2021
# Description: Submission for Assignment 02
#        Date: October 2,2021

# YOUR CODE HERE



check_email= input( "email: ")

prefix = check_email
if prefix >= "a" or prefix <= "Z":
  print("starts with a letter: ",prefix)
# elif prefix <= "Z":
#   print("starts with a letter: ",prefix)
# elif prefix >= "1":
#   print("does not start with a letter!")



has_at = check_email.find ("@")
if has_at >= 0:
  print("Has @")
else:
  print("rewrite email with @")


# li = check_email.split("@")



#########################################  TASK 2  ##################################################

str_stats = str(input("Enter a sentence: "))
cap = 0
# How many words

wlen = str_stats.split()
wlen = (len(wlen))
print ("Amount of words: ", wlen)



#Capitalize percentage

cword = ''.join(str_stats.split())
# print (cword)

cword

repeat = len(cword)
# print (repeat)

if cword >= "A":
  cap += 1

if cword <= "Z":
  cap+= 1
# print (cap)


  


clen = len(str_stats[::])
# print (clen)
cap = 0 
()

if str_stats[::] >= 'A':
  cap+=1

elif str_stats[::] <= 'Z':
  cap+=1

print ("Amount of capital letters:", cap)







# # REFERENCES
# # https://www.w3schools.com/python/ref_string_isupper.asp
