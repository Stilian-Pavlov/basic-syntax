number=float(input())

if number==0:
    print("zero")

elif 0<number<1:
    print("small positive")

elif 1<number<1_000_000:
    print("positive")
elif number>=1_000_000:
    print("large positive")

elif -1<number<0:
    print("small negative")
elif -1_000_000<=number<=-1:
    print("negative")
else:
    print("large negative")