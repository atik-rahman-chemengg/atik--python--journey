# Any number divisible by 3 or not
n=int(input("Enter number:"))
i=1
div=0
while(i<=n):
    if i%3==0:
        div=div+1
    i=i+1
print("Divisible number",div)
