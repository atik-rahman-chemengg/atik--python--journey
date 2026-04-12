# Palindrome number:
n=int(input("Enter number:"))
i=n
rev=0
while i>0:
    digit=i%10
    rev=rev*10+digit
    i=i//10
if rev==n:
    print("Palindrome number")
else:
    print("Not Palindrome")
