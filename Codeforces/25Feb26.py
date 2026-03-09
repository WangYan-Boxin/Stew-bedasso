import sys
sys.stdin = open("../CCC/in.txt", "r")
sys.stdout = open("../CCC/out.txt", "w")

t = int(input())
for i in range(t):
    b = int(input())
    a = b-1
    print(a)
