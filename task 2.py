st = input("enter a string ")
pos = int(input("enter the index "))

if len(st)==0:
    print("Empty String")
elif pos<len(st):
    print(st[pos])
else:
    print("i out of range")