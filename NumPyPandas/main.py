import numpy as np

arr1 = np.array([1, 2, 3, 4])
print("One dimentional array ", arr1, " Index 2 N 3 -- ",arr1[2])

print("="*20)

arr2 = np.array([[1,2,5],[3,4,6]])
print("2 dim array ", arr2, " Index [R,C]--- N 4 --- ", arr2[1,1])
print(arr2[0,1])

print("="*20)
print()
print("         ATTRIBUTES: ")
print()
print("1- Dimentins:             ",arr2.ndim)
print("2- Data Type:             ",arr2.dtype)
print("3- Elements counts        ",arr2.size)
print("4- Count Rows and Columns ",arr2.shape)

print("="*20)
print()
arr3 = np.zeros((3,2))
arr4 = np.ones((2,3))
arr5 = np.full((2,2), 5)
arr6 = np.eye(3,4,2)
arr7 = np.arange(0,20,2) # from 0 to < 20 by 2 steps
arr8 = np.random.rand(2,3) # float 0 -> 1 
reshaped = arr2.reshape(3,2)
flattened = arr2.flatten() 


print("        FUNCTIONS WITH NUMPY: ")
print()
print("1- Zeroes:         ",arr3)
print()
print("2- Ones:           ",arr4)
print()
print("3- Custom number   ",arr5)
print()
print("4- Eye function    ",arr6)
print()
print("5- Arange function ",arr7)
print()
print("6- random function ",arr8)
print()
print("7- Reshape function ",reshaped)
print()
print("8- Change to a normal array   ",flattened)
print()








print("="*20)
print()


print("="*20)
print()



print("="*20)
print()





























































""" import numpy as np
import timeit

lista = [1,2,3,4,5]
arr = np.array([1,2,3,4,5])
print(lista)
print(arr)

print(arr.shape)
print(arr.dtype)
print("="*8)

arr2d= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d.shape)

print("="*8)

print(arr2d[0])   # first rad
print(arr2d[:,0]) # fist column
print(arr2d[1:, 1:])  # 8 , 9
print("="*8)

print()
print()
print()
print(arr2d[:, :]) # alla rader , alla kolumner

print("="*8)

print(arr2d[0, :]) # rad 0, alla columner = forsta rad
print(arr2d[:, 2]) # alla rade , kolumn 0 = forsta raden
print() # alla rader , kolumn 0 = forsta kolumn

print("="*8)

n = 1_000_000
data = list(range(n))
arr = np.arange(n)
tid_lista = timeit.timeit(lambda: [x**2 for x in data], number=10)
print(f"lista: {tid_lista:.3f} s for 10 korningar")

tid_array = timeit.timeit(lambda: arr**2, number=10)
print(f"lista: {tid_array:.3f} s for 10 korningar")

print()
print()
"""