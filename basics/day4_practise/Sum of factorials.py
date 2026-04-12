#Sum of factorials:
n=int(input("Enter number:"))
i=n
sumd=0
while i>0:
    fact=1
    j=i
    while j>1:
        fact=fact*j
        j=j-1
    sumd=sumd+fact
    i=i-1
print("Sum of factorials of given number=",sumd)
