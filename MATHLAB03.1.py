#LET X = [11,22,33] MULTIPLY IT BY 3 
x = [11,22,33]
num = 3
res = [y* num for y in x]
print("Multiplying each element by 3 we get = ", res)

#how to find the numbers of elements in the list 
print("number of elemets in the list are =", len(x))

#copying values in a new list 
a = [1,3,4]
b = []
b=a
print(b)

#matrices 
c = [[4,1,2],[3,5,1],[1,1,3]]
d = [1,4,8]
print(len(c))
print(len(d))
#print(sum(c)) - error bcz elements in c are also lists and we cant give them int ka kaam
print(sum(d))

x = [1.0]*5
print(x)
z = [1, 5, 6, 7]  

for i in range(len(z)):  
    print(f"z[{i}] = {z[i]}") 