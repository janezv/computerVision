import numpy as np

mylist = [1, 2, 3]
print(type(mylist))

# pretvori v list
print("***********************************")
myarray = np.array(mylist)
print(myarray)
print(type(myarray))

# kreiraj array
print("***********************************")
ar1 = np.arange(0, 10, 2)
print(ar1)
arn = np.zeros(shape=(10, 5))
print(arn)
aro = np.ones((2, 4))
print(aro)

# kreiraj array
print("***********************************")
np.random.seed(101)
arr = np.random.randint(0, 100, 10)
print(arr)
arr2 = np.random.randint(0, 100, 10)
print(arr2)

print(arr.max())
print(arr.argmax())
print(arr.min())
print(arr.argmin())
print(arr.mean())
print(arr.shape)
print(arr.reshape(5, 2))


# indexing
print("***********************************")
mat = np.arange(0, 100).reshape(10, 10)
print(mat)
print(mat.shape)
print("**row=0; col= 1**")
row = 0
col = 1
print(mat[row, col])
# print 46
print(mat[4, 6])
# slicr
print(mat[:, 1].reshape(10, 1))
print(mat[0:3, 0:3])
mat[0:3, 0:3] = 3
print(mat)
mynewmat = mat.copy()
mynewmat[0:6, :] = 999
print(mat)
print(mynewmat)
