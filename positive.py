List1 = []

n = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, n+1):
    value = int(input("Please enter the Value of %d Element : " %i))
    List1.append(value)

print("\nPositive Numbers in this List are : ")
for j in range(n):
    if(List1[j] >= 0):
        print(List1[j], end = '   ')
