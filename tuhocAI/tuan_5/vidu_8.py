#chuyen ve mang 1 chieu
import numpy as np

arr=np.array([[3,4],[4,7]])
print(arr)
out=arr.flatten()
print(out)

a_arr=np.array([[2,4,5],[3,5,6]])
print('aarr \n ', a_arr)
b_arr=a_arr[:,1:3]
print('barr \n ',b_arr)

print('truoc luc a_aar',a_arr[0,1])
b_arr[0,0]=99
print('sau nay b_arr',a_arr[0,1])