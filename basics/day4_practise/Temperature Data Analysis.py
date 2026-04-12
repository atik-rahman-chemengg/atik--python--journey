#Temperature Data Analysis:
n=int(input("Enter number of temperature readings:"))
t=float(input("Enter temperature:"))
max_temp=t
min_temp=t
total=t
count_warning=0
if t>100:
    count_warning=count_warning+1
i=1
while i<n:
    t=float(input("Enter temperature:"))
    total=total+t
    if t>max_temp:
        max_temp=t
    if t<min_temp:
        min_temp=t
    if t>100:
        count_warning=count_warning+1
    i=i+1
avg=total/n
print("Highest temperature=",max_temp)
print("Lowest temperature=",min_temp)
print("Average temperature=",avg)
print("Warning count=",count_warning)
