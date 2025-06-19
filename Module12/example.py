import numpy as np
from numpy.ma.core import array

#create a 2d array
arr_2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)

element=arr_2d[1,2]
print(element)

#dimensions
dimensions=arr_2d.ndim
print(dimensions)

#seperate array
sub_array=arr_2d[:2,:2] #selects the first two rows and first two columns
print(sub_array)

sub_array2=arr_2d[-4:,-4:] #slices the last 4 elements of each row
print(sub_array2)

sum = np.sum(arr_2d)
print(sum)

avg = np.mean(arr_2d)
print(avg)