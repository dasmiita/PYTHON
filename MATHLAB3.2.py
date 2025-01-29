A = [[4, 1], 
     [1, 3]]
b = [15, 10]  
x = [0] * len(b)
tol = 1e-6
max_iterations = 100  

# Gauss-Seidel Iteration
for j in range(max_iterations):
    y = x[:]  # Copy list

    for i in range(len(b)):
        sum1 = sum(A[i][j] * y[j] for j in range(i))
        sum2 = sum(A[i][j] * x[j] for j in range(i + 1, len(b)))
        y[i] = (b[i] - sum1 - sum2) / A[i][i]  

    if max(abs(y[i] - x[i]) for i in range(len(b))) < tol:
        break
    
    x = y  

print("Solution:", x)
