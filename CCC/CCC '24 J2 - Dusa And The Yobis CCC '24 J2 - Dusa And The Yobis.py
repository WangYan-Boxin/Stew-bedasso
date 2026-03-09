import sys
sys.stdin = open("in.txt", "r")
sys.stdout = open("out.txt", "w")
D = int(input())
A = int(input())
while D > A:
    D += A
    A = int(input())
print(D)
