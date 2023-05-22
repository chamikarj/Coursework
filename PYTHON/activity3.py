month = input("enter your month").lower()
day = int(input("enter your day"))

if day == 1 and month == ("january" or "july"):
    print("holyday")
elif day == 25 and month == "december":
    print("holyday")

else:
    print("not holyday")
