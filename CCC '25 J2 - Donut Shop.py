import sys
sys.stdin = open("in.txt", "r")
sys.stdout = open("out.txt", "w")

D = int(input())
E = int(input())
while E > 0:
    sym = input()
    num = int(input())
    if sym == '+':
        D = D + num
    else:
        D = D - num
    E = E - 1
print(D)
