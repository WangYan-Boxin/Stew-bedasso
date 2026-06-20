targetWord = "interesting"
target = list(targetWord)
user = ["_"] * len(target) #create a list of _ with the same length as target
print(*user)
lives = 7
running = True
while running == True:
   choice = input()
   if choice in target: #check if something appears in a list
       print("good")
       for i in range(len(target)):
           if target[i] == choice:
               user[i] = choice
       if "_" not in user:
           print("You win!")
           running = False       #check if the user won the game
   else:
       print("bad choice.", lives-1, "lives left")
       lives -= 1
       if lives == 0:
           print("you lost!")
           running = False
   print(user)