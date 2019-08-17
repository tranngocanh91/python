text='geeks for geeks '
print(text.split())
text1='geeks, for,geeks '
print(text1.split(','))
text2= 'geeks, for, geeks, pawan'
print(text2.split(',',0))

line='001,jonh,12-06-1998'
info = line.split(',')
print(info)

line1=['001','jonh','12-06-1998']
info2= (',').join(line1)
print(info2)