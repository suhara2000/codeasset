import os
from shutil import copyfile


fone = open('demofile.txt','w')
fone.write('hello world')
fone.close()

copyfile("demofile.txt", "newfile.txt")

#read
ftwo = open('newfile.txt','r')
message = ftwo.read()
print(message)
ftwo.close()
os.remove("demofile.txt")