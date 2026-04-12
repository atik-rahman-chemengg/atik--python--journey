# sum of digits:
i=int(input("Enter digit you want to sum:"))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("Sum of digits=",sum)
