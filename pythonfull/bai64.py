import os.path, time
print (("time.ctime() : %s") % time.ctime(os.path.getmtime("anhlaVIP.txt")))