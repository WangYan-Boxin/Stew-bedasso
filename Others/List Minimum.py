n = int(input())

numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

while len(numbers) > 0:

    smallest = min(numbers)

    print(smallest)

    numbers.remove(smallest)