# sum of cubes of numbers
n=int(input("Enter number:"))
i=1
sumd=0
while(i<=n):
    sumd=sumd+i*i*i
    i=i+1
print("Sum of cubes=",sumd)
