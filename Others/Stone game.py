s = 7
p = 1

while s > 0:
    print(f"Stones: {s} | Player {p}'s turn")
    take = int(input("Take 1 or 2: "))

    if take in [1, 2] and take <= s:
        s -= take
        if s == 0:
            print(f"Player {p} took the last stone and LOST!")
            break
        p = 3 - p  # 切换玩家：1 变成 2，2 变成 1
    else:
        print("Invalid move!")

# 胜负判定：p 为 1 时 3-p=2, p 为 2 时 3-p=1
print(f"Winner is Player {3 - p}!")