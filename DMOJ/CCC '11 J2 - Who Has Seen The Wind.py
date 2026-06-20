import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

h = int(input())
m = int(input())

t = 1
altitude = -6*(t**4) + h*(t**3) + 2*(t**2) + t

while altitude > 0 and t < m:
    t = t + 1
    altitude = -6*(t**4) + h*(t**3) + 2*(t**2) + t

if altitude <= 0:
    print("The balloon first touches ground at hour:")
    print(t)
else:
    print("The balloon does not touch ground in the given time.")