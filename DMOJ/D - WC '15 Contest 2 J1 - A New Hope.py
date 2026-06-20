N = int(input())
sentence = "A long time ago in a galaxy "
for i in range(N):
    if i == N-1:
        sentence = sentence + "far"
    else:
        sentence = sentence + "far,"
sentence = sentence + "away..."
print(sentence)