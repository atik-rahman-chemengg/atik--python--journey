# sum of digits cubes:
n=int(input("Enter number"))
sum=0
while(n>0):
    i=n%10
    sum=sum+i*i*i
    n=n//10
print("Sum of squares=",sum)
