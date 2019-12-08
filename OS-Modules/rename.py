# os.rename(): A file old.txt can be renamed to new.txt, using the function os.rename().
# The name of the file changes only if, the file exists and user has
# sufficient privilege permission to change the file.

import os
fd = 'mass.txt'
file = os.rename(fd, 'new.txt')

