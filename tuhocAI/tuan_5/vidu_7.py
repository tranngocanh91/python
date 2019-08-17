#tao ma tran duong cheo

import numpy as np

arr4=np.eye(8)

print(arr4)

arr5=np.random.random((3,4))

print(arr5)

arr6 =np.arange(10)
print(arr6)
out=np.where(arr6<5,arr6,10*arr6)
print(out)