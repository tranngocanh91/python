from os import listdir
from os.path import isfile , join
friend_list= [ f for f listdir("/codefofun/wesooldhwee") if isfile(join("/codefofun/wesooldhwee",f))]
print(friend_list)