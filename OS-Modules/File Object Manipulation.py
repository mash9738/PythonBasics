# os.popen(): This method opens a pipe to or from command.
# The return value can be read or written depending on whether mode is ‘r’ or ‘w’.
# Syntax: os.popen(command[, mode[, bufsize]])

import os
fd = "mass.txt"
# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello Mahesh")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("hai Deepika")
file.close()
file = open(fd, 'r')
t = file.read()
print(t)

# File not closed, shown in next function.
