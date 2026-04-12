#Counting even digits
#Sum of even digits
#Printing even digits
n=int(input("Enter number:"))
count=0
sumd=0
while n>0:
    digit=n%10
    if digit%2==0:
        count=count+1
        sumd=sumd+digit
        print("Even digits=",digit)
    n=n//10
print("Even numbers=",count)
print("Sum of even digits=",sumd)
  
