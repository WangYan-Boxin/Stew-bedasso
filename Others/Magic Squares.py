import sys
sys.stdin = open("../DMOJ/in.txt", "r")

mat = []
list_col = []

for i in range(4):
   row = [int(x) for x in input().split()]
   mat.append(row)

for c in range(4):
    column_data = []
    for r in range(4):
        column_data.append(mat[r][c])
    list_col.append(column_data)





all_answers = []

for i in range(4):
    row_sum = sum(mat[i])
    all_answers.append(row_sum)

for i in range(4):
    col_sum = sum(list_col[i])
    all_answers.append(col_sum)

is_magic = True
standard = all_answers[0]
for ans in all_answers:
    if ans != standard:
        is_magic = False
        break

if is_magic:
    print("magic")
else:
    print("not magic")





# # 1. 一行代码读取 4x4 矩阵
# mat = [[int(x) for x in input().split()] for _ in range(4)]
#
# # 2. 一行代码算出 8 个和并去重
# unique_sums = set([sum(row) for row in mat] + [sum(col) for col in zip(*mat)])
#
# # 3. 一行代码输出结果 (这叫三元表达式)
# print("magic" if len(unique_sums) == 1 else "not magic")