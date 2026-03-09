s = int(input())
x = int(input())
clothing_size = ((s + 2) * 3 + 16)
if x >= clothing_size:
    print("Yes it fits!")
else:
    print("No, it's too small :(")
