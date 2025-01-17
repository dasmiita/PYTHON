def mathlab(a1, b1, c1, a2, b2, c2):
    deter = a1 * b2 - a2 * b1
    
    if deter == 0:
        return "No unique solution"

    x = (b2 * c1 - b1 * c2) / deter
    y = (a1 * c2 - a2 * c1) / deter

    return x, y

a1 = int(input("Enter first coefficient of first equation = "))
b1 = int(input("Enter second coefficient of first equation = "))
c1 = int(input("Enter the answer of first equation = "))


a2 = int(input("Enter first coefficient of second equation = "))
b2 = int(input("Enter second coefficient of second equation = "))
c2 = int(input("Enter the answer of second equation = "))


sol = mathlab(a1, b1, c1, a2, b2, c2)
print("Solution:", sol)