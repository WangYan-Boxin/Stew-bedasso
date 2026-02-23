import sys
sys.stdin = open("in.txt","r")
sys.stdout = open("out.txt","w")
a=int(input())
b=int(input())
c=int(input())
total=91+a+3*b+c
print("The 1-3-sum is", total)