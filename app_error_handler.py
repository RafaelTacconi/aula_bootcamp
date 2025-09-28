

def get_valid_salary():
    """
    Returns a valid salary after repeatedly prompting the user for input until a non-negative number is entered.

    Raises:
        ValueError: If the user enters a non-numeric value for salary.
    """
    while True:
        try:
            salary = float(input("Enter your salary: "))
            if salary >= 0:
                return salary
            else:
                print("Salary must be a non-negative number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for salary.")

def get_valid_name():
    """
    Returns a valid name after repeatedly prompting the user for input until a non-empty string is entered.
    """
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Please try again.")
            
def get_valid_percentage():
    """
    Returns a valid bonus percentage after repeatedly prompting the user for input until a non-negative number is entered.

    Raises:
        ValueError: If the user enters a non-numeric value for percentage.
    """
    while True:
        try:
            perc_bonus = float(input("Enter your bonus percentage: "))
            if perc_bonus >= 0:
                return perc_bonus
            else:
                print("Bonus percentage must be a non-negative number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for bonus percentage.")

#calculo de bonus
BONUS = 1000
user_name = get_valid_name()
salary = get_valid_salary()
perc_bonus = get_valid_percentage()
bonus = BONUS + salary * perc_bonus 

print(f"Hello {user_name}. Your bonus is: {bonus}"  )  