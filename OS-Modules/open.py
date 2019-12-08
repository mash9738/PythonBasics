import os
print(os.name)

# Function os.getcwd(), returns the Current Working Directory(CWD) of the file used to execute the code
print(os.getcwd())
# To print absolute path on your system
print(os.path.abspath('.'))

# To print files and directories in the current directory
# on your system
print(os.listdir('.'))

# os.error: All functions in this module raise OSError in the case of invalid or
# inaccessible file names and paths, or other arguments that have the correct type,
# but are not accepted by the operating system. os.error is an alias for built-in OSError exception.
filename = 'mass'
try:
    # If the file does not exist,
    # then it would throw an IOError
    f = open(filename, 'rU')
    text = f.read()
    print(text)
    f.close()

# Control jumps directly to here if
# any of the above lines throws IOError.
except IOError:
    # print(os.error) will <class 'OSError'>
    print('Problem reading: ' + filename)

# In any case, the code then continues with
# the line after the try/except

