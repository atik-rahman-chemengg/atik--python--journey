#Armstrong number:
n=int(input("Enter number you want to check for armstrong:"))
i=n
count=0
while(i>0):
    count=count+1
    i=i//10
i=n
sumd=0
while(i>0):
    digit=i%10
    j=1
    mul=1
    while(j<=count):
        mul=mul*digit
        j=j+1
    sumd=sumd+mul
    i=i//10
if(sumd==n):
    print("Armstrong number")
else:
    print("Not")
