import sys
sys.stdin = open("in.txt","r")
sys.stdout = open("out.txt","w")
#提交答案时不要包括这上面的
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a>b>c>d:
    print("Fish Diving")
elif a<b<c<d:
    print("Fish Rising")
elif a==b==c==d:
    print("Fish At Constant Depth")
else:
    print("No Fish")