#to check whether a system of linear equations has a solution or not 
import copy
import numpy as np

def con(A,B):
    AB = copy.deepcopy(A)
    for i in range (0,len(A)):
        AB[i].append(B[i])
    print("augmented matrix constructed = ",AB)
    ra = np.linalg.matrix_rank(A)
    rab = np.linalg.matrix_rank(AB)
    print ("rank of problem matrix = ", ra)
    print ("rank of augmented matrix = ", rab)

    if(ra!=rab):
        print("system is inconsistent as no solution exists!")
    elif(ra == rab ==len(A)):
        print("system is consistent as unique solution exists!")
    elif(ra == rab != len(A)):
        print("system is consistent as infinite solutions exist!")

A = [[1, 2, -1], [-2, 2, 3], [2, 0, 4]]
B = [6, 3, 4]
con(A,B)
