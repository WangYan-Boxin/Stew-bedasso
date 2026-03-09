import sys

sys.stdin = open("in.txt", "r")
sys.stdout = open("out.txt", "w")

Poblano = 1500
Mirasol = 6000
Serrano = 15500
Cayenne = 40000
Thai = 75000
Habanero = 125000

num_chili=int(input())
spiciness = 0
for i in range(num_chili):
    chili = input()
    if chili == "Poblano":
        spiciness += Poblano
    elif chili == "Mirasol":
        spiciness += Mirasol
    elif chili == "Serrano":
        spiciness += Serrano
    elif chili == "Cayenne":
        spiciness += Cayenne
    elif chili == "Thai":
        spiciness += Thai
    elif chili == "Habanero":
        spiciness += Habanero
print(spiciness)

