# product of digits
i=int(input("Enter digit you want to get product:"))
mul=1
while(i>0):
    mul=mul*(i%10)
    i=i//10
print("Products of digits=",mul)
