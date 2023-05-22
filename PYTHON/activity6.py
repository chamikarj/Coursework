vovel = ("a", "e", "i", "o", "u")
word = input("enter name: ")
if word[0] in vovel and word[-1] in vovel:
    print("both side has vovels")
elif word[0] in vovel:
    print("First letter")
elif word[-1] in vovel:
    print("Last letter")
else:
    print("no vovel")
