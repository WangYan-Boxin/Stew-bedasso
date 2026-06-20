import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

#for loop
# n=int(input())
# highest_bid = -1
# winner = ""
#
# for i in range(n):
#     name = input()
#     bid = int(input())
#
#     if bid > highest_bid:
#         highest_bid = bid
#         winner = name
#
# print(winner)

#while loop
n=int(input())
count=0
highest_bid = -1
winner = ""

while count<n:
    name = input()
    bid = int(input())
    if bid>highest_bid:
        highest_bid = bid
        winner = name
    count+=1
print(winner)