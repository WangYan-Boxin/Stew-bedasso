import pygame

print("select the Game level: Eazy, Medium, Hard")
print("Or game will start as Medium")
top = 100
level = input().lower()
if level == "eazy":
    top = 10
if level == "medium":
    top = 100
if level == "hard":
    top = 1000

import random
x = random.randint(1, top)
print("Enter your guess")
y = int(input())
n = 1

while x != y:
    if x > y:
        print("My number is greater than:", y)
    elif x < y:
        print("My number is smaller than:", y)
    n = n + 1
    y = int(input())
else:
    print("Congratulation, it is the right number")
    print(f"You use {n} times to win")
