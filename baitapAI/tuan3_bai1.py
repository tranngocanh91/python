filepath='taofilename.txt'
filehandle=open(filepath,'r')
data=filehandle.read()
print(type(data))
print('========')
print(data)
filehandle.close()