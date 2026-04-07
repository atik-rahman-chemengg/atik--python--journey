# First n even numbers add
n=int(input("How many even numbers you want to add:"))
i=1
sumd=0
count=0
while(count<n):
    if i%2==0:
        sumd=sumd+i
        count=count+1
    i=i+1
print("Sum of first even numbers:",sumd)
