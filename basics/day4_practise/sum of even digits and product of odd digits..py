# sum of even digits and product of odd digits:
i=int(input("Enter digit you want to get sum and product:"))
sum=0
mul=1
while(i>0):
    digit=i%10
    if digit%2==0:
        sum=sum+digit
    else:
        mul=mul*digit
    i=i//10
print("Sum of even digits=",sum)
print("Product of odd digits=",mul)
