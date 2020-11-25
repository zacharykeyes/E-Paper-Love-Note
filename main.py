import time, random

location = "Python\ScreenAnniversary\messagesToMollie.txt"

f = open(location, 'a') #append to end of file
g = open(location, 'r') #read from beginning of text file

for x in g:
   print(x)
   time.sleep(2)

# print(g.readline()) #print first line

# f.write("\n" + input("input message to add to list: "))

f.close
g.close