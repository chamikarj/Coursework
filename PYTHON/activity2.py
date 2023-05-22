# exercise 01 01
x = int(input("enter number : "))
if x % 2:
    print(" odd number")
else:
    print("even number")

print("...........................")

# 02
x = {"january": 1, "july": 1, "december": 3}
i = x.keys
j = x.values

month = input("enter month : ").lower()
day = int(input("enter day : "))

if month in x and day in x.values():
    print("its bank holy day")
else:
    print("its not bank holy day")
