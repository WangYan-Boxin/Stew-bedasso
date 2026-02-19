V = int(input())
n = input()
p = n.count("A")
q = n.count("B")
if p > q:
    print("A")
elif p < q:
    print("B")
else:
    print("Tie")