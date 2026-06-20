A = int(input())
C = int(input())

if A == 3 and C >= 95:
    M = "absolutely"
elif A == 1 and C <= 50:
    M = "fairly"
else:
    M = "very"

print(f"C.C. is {M} satisfied with her pizza.")