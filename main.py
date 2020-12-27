import time, random, emailPull, os
# from emailPull import Read
# import ReadEmail from emailPull

def TextHandler(subject, content):
   if subject.lower() == 'add':
      f.write(content)
      f.write('\n')
   elif subject.lower() == 'push':
      #TODO push to screen now
      print('TODO push to screen now')
   else:
      print('Not a valid Email Subject')

#Find messagesTo.txt file path in working directory
cwd = os.getcwd()
notedir = cwd + "\messagesTo.txt"

f = open(notedir, 'a') #append to end of file
g = open(notedir, 'r') #read from beginning of text file

emails = emailPull.ReadEmail()
# print(emails)
for y in emails:
#    print(y[0])
#    print(y[1])
   TextHandler(y[0], y[1])

# for x in g:
#    print(x)
#    time.sleep(2)

# print(g.readline()) #print first line

# f.write("\n" + input("input message to add to list: "))



      
f.close
g.close
