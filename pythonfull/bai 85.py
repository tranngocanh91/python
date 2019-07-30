import os
path = 'anhlaVIP.txt'
if os.path.isfile(path):
    print('It is a file')
elif os.path.isdir(path):
    print('it is a directory ')
else:
    print(' File ^^')
