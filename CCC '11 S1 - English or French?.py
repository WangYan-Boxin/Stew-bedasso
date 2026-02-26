import sys
sys.stdin = open("in.txt","r")
sys.stdout = open("out.txt","w")

n=int(input())
t=0
s=0
for i in range(n):
    sentence=input().lower()
    t += sentence.count("t")
    s += sentence.count("s")
if t > s:
    print("English")
else:
    print("French")
