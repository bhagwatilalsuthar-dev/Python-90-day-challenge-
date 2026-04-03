#          ###NumPy ####
import numpy as np
myNumpy= np.array([5,6,7,3,2,2])
# print(np.sum(myNumpy))
# print(np.mean(myNumpy))


import numpy as np
arr=np.array([5,10,15,20,25,30])
# print(arr[:3])
# print(arr[1:5])
# print(arr[-3:])
even= arr[arr%2==0]
# print(even)

#2D array#
import numpy as np
arr=np.array([[10,20,30],
             [40,50,60],
             [70,80,90]])
# print(arr.shape)
# print(arr[1,1])
# print(arr[-1])
# print(arr[:,1])


##Matrix Addition
import numpy as np
a=np.array([[1,2],
          [3,4]])
b=np.array([[5,6],
           [7,8]])
# c=a+b
# print(c)
c=np.dot(a,b)
# print(c)





import numpy as np
a=np.array([[2,4],
 [6,8]])
cb=np.dot(a,a)
# print(a)
# print(cb)



#fINDING MISSING VALUES WITH Numpy

#Import Numpy 
import numpy as np
arr=np.array([10,20,np.nan,40,np.nan,60])
missing=np.isnan(arr) #missing value
print("Total Missing Value:",np.sum(missing))