a3=int(input())
a2=int(input())
a1=int(input())
b3=int(input())
b2=int(input())
b1=int(input())
a_total=a3*3+a2*2+a1*1
b_total=b3*3+b2*2+b1*1
if a_total>b_total:
    print("A")
if b_total>a_total:
    print("B")
if a_total==b_total:
    print("T")