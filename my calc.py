monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

savings = monthly_income - monthly_expenses

if savings >= 10000:
    fun_money = savings * 0.4
elif savings <10000:
    fun_money = savings * 0.2
else:
    fun_money = input("Your savings are insufficient")


print("Your monthly fun money is: $" + str(fun_money))