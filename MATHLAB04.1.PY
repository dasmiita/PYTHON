#to check whether a system of linear equations has a solution or not 
import copy
import numpy as np
#problem matrix 
A = [[1, 2, -1], [-2, 2, 3], [2, 0, 4]]
B = [6, 3, 4]
print("problem matrix = ", A)
print("constant matrix = ", B)
# Constructing the augmented matrix in one way
""" AB = [row + [B[i]] for i, row in enumerate(A)]
for row in AB:
    print(row)"""
#constructing the augmented matrix in another way
AB = copy.deepcopy(A)
for i in range (0,len(A)):
    AB[i].append(B[i])
print("augmented matrix constructed = ",AB)
ra = np.linalg.matrix_rank(A)
rab = np.linalg.matrix_rank(AB)
print ("rank of problem matrix = ", ra)
print ("rank of augmented matrix = ", rab)
if(ra!=rab):
    print("no solution exists!")
elif(ra == rab ==len(A)):
    print("unique solution exists!")
elif(ra == rab != len(A)):
    print("infinite solutions exist!")



