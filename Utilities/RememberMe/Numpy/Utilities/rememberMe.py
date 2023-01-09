import numpy
import numpy as np

# array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
#                   32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64])
array1 = np.arange(1, 65)

# ******* a.) resape v 2 dimenzjonalno matriko


# ******* b.) resape v 3 dimenzjonalno matriko


# ******* e.) Naredi "kvadratast" slice iz 2D matirke


# ******* d.) izpiši element iz 3 dimenzjonalne matrike


# ***********************************************************************************************************************************************************
# REŠITVE
# ***********************************************************************************************************************************************************

# ******* a.) resape v 2 dimenzjonalno matriko   (produkt - zmnožek mora očigledno biti enak številu elementov matrike)
arrayA = array1.reshape(16, 4)
print("Matrika reshape(16, 4): ")
print(arrayA)


# ******* b.) resape v 3 dimenzjonalno matriko
arrayB = array1.reshape(2, 4, 8)
print("reshape v 3 demenzijoalno matriko: ")
print(arrayB)

# ******* c.) izpiši element iz 2 dimenzjonalne matrike
print("Poljubni element v 2Dimenizjonalni matriki:", arrayA[9, 0])


# ******* d.) izpiši element iz 3 dimenzjonalne matrike
print("Poljubni element v 3Dimenizjonalni matriki:", arrayB[1, 1, 4])


# ******* e.) Naredi "kvadratast" slice iz 2D matirke
# https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
print("slice iz 2D Matrike:")
print(arrayA[2:4, 1:3])
