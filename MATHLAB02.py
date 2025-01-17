def mathfun():
    #solving for 2 linear systems 
    a1, b1, c1 = 1, 2, 3
    a2, b2, c2 = 2, 4, 6

    # Calculate determinants
    d = (a1 * b2 - b1 * a2)
    d1 = (c1 * b2 - b1 * c2)
    d2 = (a1 * c2 - a2 * c1)

    if d != 0:
        x = d1 / d
        y = d2 / d
        return x, y
    elif d == 0 and d1 == 0 and d2 == 0:
        return "Infinite solutions exist"
    else:
        return "No solution exists"

result = mathfun()
if result == "Infinite solutions exist" or result == "No solution exists":
    print(result)
else:
    x = result[0]
    y = result[1]
    print("x =", x)
    print("y =", y)