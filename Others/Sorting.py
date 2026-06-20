import sys
sys.stdin = open("in.txt", "r")
sys.stdout = open("out.txt", "w")

N = int(input())
numbers = []

for i in range(N):
    num = int(input())
    numbers.append(num)

numbers.sort()

for num in numbers:
    print(num)