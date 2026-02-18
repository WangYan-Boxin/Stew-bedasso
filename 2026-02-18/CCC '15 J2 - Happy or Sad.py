a = input()
p = a.count(":-)")
t = a.count(":-(")
if p + t == 0:
    print("none")
elif p == t:
    print("unsure")
elif p > t:
    print("happy")
else:
    print("sad")
