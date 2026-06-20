# import sys
# sys.stdin = open("in.txt", "r")
# sys.stdout = open("out.txt", "w")

word = input()

if word == word[::-1]:
    print("The word is a palindrome")
else :
    print("The word is not a palindrome")