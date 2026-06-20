burger = [0, 461,431,420,0]
side = [0,100,57,70,0]
drink = [0,130,160,118,0]
dessert = [0,167,266,75,0]

burger_choice = int(input())
side_choice = int(input())
drink_choice = int(input())
dessert_choice = int(input())

calories = (burger[burger_choice] + drink[drink_choice] + side[side_choice] + dessert[dessert_choice])
print(f"Your total Calorie count is {calories}.")