#Reverse the given number:
n=int(input("Enter number you want to reverse:"))
i=n
rev=0
while i>0:
    digit=i%10
    rev=rev*10+digit
    i=i//10
print("Reverse number=",rev)
