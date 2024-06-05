import numpy as np 

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]]) 

addition = np.add(matrix1, matrix2)
substraction = np.subtract(matrix1, matrix2)
multiplication = np.dot(matrix1, 2)
transponation = np.transpose(matrix1)


print(f"{addition} \n\n {substraction} \n\n {multiplication} \n\n {transponation}")