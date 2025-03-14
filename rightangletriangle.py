print("right angle triangle with the help of star")
n=int(input("enter the numbers of rows"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()