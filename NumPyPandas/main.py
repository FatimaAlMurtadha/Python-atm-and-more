import numpy as np

import timeit

arr1 = np.array([1, 2, 3, 4])
print("One dimentional array ", arr1, " Index 2 N 3 -- ",arr1[2]) # 3

print("="*20)

arr2 = np.array([[1,2,5],[3,4,6]])
print("2 dim array ", arr2, " Index [R,C]--- N 4 --- ", arr2[1,1])
print(arr2[0,1]) # 2

print("="*20)
print()
print("         ATTRIBUTES: ")
print()
print("1- Dimentins:             ",arr2.ndim) # 2
print("2- Data Type:             ",arr2.dtype) # int64
print("3- Elements counts/ size  ",arr2.size) # 6
print("4- Count Rows and Columns ",arr2.shape) # (2,3)

print()
print()
arr3 = np.zeros((3,2))
arr4 = np.ones((2,3))
arr5 = np.full((2,2), 5)
arr6 = np.eye(3,4,2)
arr7 = np.arange(0,20,2) # from 0 to < 20 by 2 steps
reshaped = arr2.reshape(3,2)
flattened = arr2.flatten() 

print("="*20)
print()

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
print("5- Arange function ",arr7) # [ 0  2  4  6  8 10 12 14 16 18] - arr2.reshape(3,2)
print()
print("6- Reshape function ",reshaped) #  [[1 2] [5 3] [4 6]]
print()
print("7- Change to a normal array   ",flattened)
print()


print("="*20)
print()
# Module Random
arr8 = np.random.rand(2,3) # float 0 to < 1 
arr9 = np.random.randn(3,3) # positive infinity -> negative infinity -- +3 to -3 => float
arr10 = np.random.randint(10, 200, (2,3)) # 2 rows and 3 columns

print("        Random medule: ")
print()
print("1- random      ",arr8)
print()
print("2- random n    ",arr9)
print()
print("3- random int  ",arr10)
print()


# Seed for testing -- we need specific numbers
# np.random.seed(100)
# print(np.random.rand(2,3))



print("="*20)
print()
print("          Some opposite functions ")
arr11 = np.array([[1,2,3,4],[5,6,7,8]])
# arange - linspace
print(np.arange(1,10,2)) # the end is not included -- jump 2 steps
print(np.linspace(10,100,8)) # start + end + how many elements 8 
                             # the end is included
                             # More accurate
print(np.linspace(10,100,10,endpoint=False)) # the end not included

# flatten - transport
print("Flatten: ", arr11.flatten())
print("Before: ",arr11,"Tranpose: ", arr11.T) # the row be columns and the opposite is true
                                            # before (2,4) T (4,2)
# indexing - slicing
print( "Index R/C                        " ,arr11[0,1]) # R0 / C1 -- 2
print( "Slice every second C on both     " ,arr11[:,1]) # all R / C1 -- "2, 6"
print( "Slice all R/C with R index 1     " ,arr11[1,:]) # R1 / all C "5, 6, 7, 8"
print("All R/C on both" , arr11[:, :]) # alla rader , alla kolumner

# mathmatical operatiuons
arr12 = np.array([1,2,3,4])
arr13 = np.array([5,6,7,8])
print()
print("="*20)
print()
arr_1 = arr12 +arr13
arr_2 = arr12 * arr13
arr_3 = arr12 ** arr13
print("          Math Operations ")
print()
print("Sum:                  ", arr_1, "Shape: ", arr_1.shape) # [ 6  8 10 12]
print("Multiplacation:       ", arr_2, "Shape: ", arr_2.shape) # [ 5 12 21 32]
print("Power:                ", arr_3, "Shape: ", arr_3.shape) # [    1    64  2187 65536]
print("Square root:          ", np.sqrt(arr12)) # الجذر التربيعي [1.         1.41421356 1.73205081 2.        ]

# aggregation function
arr14 = np.array([[1,2], [3,4]])


print()
print("="*20)
print()
print("          Aggregation Functions ")
print()
print("Sum:             ", np.sum(arr14)) # 10
print("Average:         ", np.mean(arr14)) # 2.5
print("Minimum:         ", np.min(arr14)) # 1
print("Maximum:         ", np.max(arr14)) # 4

# sort
arr15 = np.array([3,2,1,0, 1, 8,8,7,4,9])
print("Sort one dim:       ", np.sort(arr15)) # [0 1 1 2 3 4 7 8 8 9]
print("Unique:             ", np.unique(arr15)) #  [0 1 2 3 4 7 8 9]


print()
arr17 = np.array([[1,2],[3,4]])
arr18 = np.array([[5,6]])
arr19 = np.concatenate((arr17,arr18),axis=0) # vertical R != R 
print("Concatination:       ", arr19)       

# vstack - hstack
arr20 = np.vstack((arr17,arr18)) # C match NOT R
print()
print( "Vertical must C match:         ",arr20) #  [[1 2] [3 4] [5 6]]

arr21 = np.hstack((arr17,arr17)) # R must match
print("Horizantal must R match:        ", arr21) #  [[1 2 1 2] [3 4 3 4]]
print()

# view - copy
print()
print("="*20)
print()
print("          VIEW    ")

arr22 = np.array([1,2,3])
print("Before the view:          ",arr22) # [1 2 3]
arr23 = arr22.view()
print("The view:                 ", arr23) # [1 2 3]

# change the view
arr23[0] = 100
print("The original now is        ", arr22) # [100   2   3]
print("The view now:              ", arr23) # [100   2   3]

print()
print("="*20)
print()
print("          COPY    ")
arr24 = np.array([1,2,3])
arr25 = arr24.copy()

arr25[0] = 100
print("The original:         ", arr24) # [1 2 3]
print("The copy:             ", arr25) # [100   2   3]
print("The original now is:  ", arr24) # did not change [1 2 3]

print()
print("="*20)
print()
print("          SEARCH    ")
arrS = np.array([1,2,3,4,5,4,4,4])
ind = np.where(arrS == 4) 
print(ind) # N 4 is located on index 3, 5,6,7
print()

print("*"*50)

lista = [1,2,3,4,5]
arr = np.array([1,2,3,4,5])
print(lista) # with commas
print(arr) # w/o commas

print(arr.shape) #  (5,) No columns 
print(arr.dtype) # int64
print("="*8)

arr2d= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d.shape) # (3,3)

print("="*8)

print(arr2d[0])   # first rad [1 2 3]
print(arr2d[:,0]) # fist column [1 4 7]
print(arr2d[1:, 1:])  # [[5 6] [8 9]]
print("="*8)

print()
print()
print()


print("="*8)

print("rad 0, alla columner = forsta rad      ",arr2d[0, :]) # rad 0, alla columner = forsta rad [1 2 3]
print("alla rader , kolumn 2                  ",arr2d[:, 2]) # alla rader , kolumn 2 -- [3 6 9]
print() # alla rader , kolumn 0 = forsta kolumn

print("="*8)

n = 1_000_000
data = list(range(n))
arr = np.arange(n)
tid_lista = timeit.timeit(lambda: [x**2 for x in data], number=10)
print(f"lista: {tid_lista:.3f} s for 10 korningar") # lista: 0.968 s for 10 korningar

tid_array = timeit.timeit(lambda: arr**2, number=10)
print(f"Numpy Array: {tid_array:.3f} s for 10 korningar") # 0.029 s for 10 korningar

print()
print()