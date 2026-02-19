W1 = input()
W2 = input()
W3 = input()
W4 = input()
W5 = input()
W6 = input()
win = (W1 + W2 + W3 + W4 + W5 + W6).count("W")
if win >= 5:
    print("1")
elif 5 > win >= 3:
    print("2")
elif win >= 1:
    print("3")
else:
    print("-1")
