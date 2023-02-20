number=int(input())
count=1
for i in range(number):
    num=int(input())
    if num %2==0:
        continue
    else:
        print(f"{num} is odd!")
        count-=1
        break
if count==1:
    print("All numbers are even.")
