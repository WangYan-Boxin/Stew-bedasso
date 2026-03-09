s = []
for i in range(5):
    s.append(int(input()))
n = int(input())
s.sort()
f = (s[1] + s[2] + s[3]) * n
print(f)
