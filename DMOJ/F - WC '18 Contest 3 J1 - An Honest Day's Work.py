P = int(input())
B = int(input())
D = int(input())

num_badges = P // B

leftover_paint = P % B

total_money = (num_badges * D) + leftover_paint

print(total_money)