#calculo de bonus
BONUS = 1000
user_name = input("Enter your name: ")
salary = float(input("Enter your salary: "))
perc_bonus = float(input("Enter your bonus percentage: "))
bonus = BONUS + salary * perc_bonus 

print(f"Hello {user_name}. Your bonus is: {bonus}"  )   