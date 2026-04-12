#Strong number:
n=int(input("Enter number:"))
i=n
total=0
while i>0:
    digit=i%10
    fact=1
    j=digit
    while j>1:
        fact=fact*j
        j=j-1
    total=total+fact
    i=i//10
if total==n:
    print("Strong number")
else:
    print("Not strong")
