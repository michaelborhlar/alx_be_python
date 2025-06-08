"""
PERSONAL EARNINGS CALCULATOR
Concepts
- Variables 
- Inputs
- Operators(+,-,/)
- Assignment
- Data types
- Formating

WHAT IT WILL DO (Pseudocode)
1. Ask for personal info
2. Ask for salary and months worked
3. Calculate total earnings
4. Calculate bonus
5. Calcualte net income
6. Average weekly income
7. Balance
8. Print summary
"""


"""
UPDATED ALGORITHM
1. While user wants to enter an employee:
2. Get inputs (name, salary, etc)
3. Compute net income
4. Use if-elif-else to clasify income level
5. Use a loop to deduct 3 expenses from net income
6. Show remaining balance and weekly distribution
7. Ask to stop or continue

UPDATED PSEUDOCODE
WHILE user wants to enter emplyee:
    Get employee details
    Caculate earnings and net income

    IF net income > 1,000,000:
        print "Higher earner"
    ELSE IF net income > 500, 000:
        print "Average earner"
    ELSE:
        print "Low earner"
    
    FOR 3 expense items:
        Ask for name and amount
        Subtract from the net income
    
    Show remianing balance
    Show weekly breakdown
    Ask if another employee should be entered
"""
NUMBER_OF_WEEKS = 4

def get_employee_details():
    name = input("Enter employee's name: ")
    age = input("Enter age: ")
    job = input("Enter job title: ")
    return {"name":name, "age":age,  "job":job}

def get_salary_details():
    salary = float(input("Enter your monthly salary: "))
    months = int(input("How many months have you worked: "))
    bonus_percent = float(input("Enter your performance bonus (%): "))
    return salary, months, bonus_percent

def calculate_net_income(salary, months, bonus_percent):
    total_earnings = salary * months
    bonus_amount = (bonus_percent / 100) * total_earnings
    net_income =  total_earnings + bonus_amount
    return total_earnings, bonus_amount, net_income

def classify_earner(net_income):
    if net_income > 1_000_000:
        return "High earner"
    elif net_income > 500_000:
        return "Average earner"
    else:
        return "Low earner"

def get_expenses():
    expenses = []
    expenses_names = set()

    for i in range(3):
        name =  input(f"  Expense #{i + 1} name: ")
        amount = float(input(f" Amount for {name}: "))
        expenses.append({"name":name, "amount": amount})
        expenses_names.add(name)
    return expenses, expenses_names

def deduct_expenses(net_income, expenses):
    for exp in expenses:
        net_income -= exp["amount"]
    return net_income

def calculate_weekly_distribution(net_income, months):
    total_weeks =  months * NUMBER_OF_WEEKS
    weekly_income = net_income // total_weeks
    balance =  net_income % total_weeks
    return weekly_income, balance

def print_summary(employee):
    d = employee['details']
    s = employee['salary']
    e = employee['earnings']

    print("\n--- Earnings Summary ---")
    print(f"Name: {d['name']}")
    print(f"Age: {d['age']}")
    print(f"Job: {d['job']}")
    print(f"Monthly Salary: {s[0]}")
    print(f"Months worked: {s[1]}")
    print(f"Total earnings (Before bonus): {e[0]}")
    print(f"Bonus Percentage: {s[2]}")
    print(f"Bonus Amount: {e[1]}")
    print(f"Net total income: {employee['earner_type']}")
    print(f"Aproximate weekly income: {employee['weekly_income']}")
    print(f"Balance: {employee['balance']}")
    print(f"Expenses: {[exp['name'] for exp in employee['expenses']]}")

add_more = "yes"
employees = []

while add_more.lower() == 'yes':
    details = get_employee_details()
    salary, months, bonus_percent = get_salary_details()
    total_earnings, bonus_amount, net_income = calculate_net_income(salary, months, bonus_percent)
    earner_type = classify_earner(net_income)

    expenses, exp_names = get_expenses()
    net_income = deduct_expenses(net_income, expenses)
    weekly_income, balance = calculate_weekly_distribution(net_income, months)

    employee = {
        "details": details,
        "salary": (salary, months, bonus_percent),
        "earnings": (total_earnings, bonus_amount, net_income),
        "earner_type": earner_type,
        "expenses": expenses,
        "expense_names":exp_names,
        "weekly_income": weekly_income,
        "balance": balance
    }

    employees.append(employee)
    print_summary(employee)

    add_more = input("\n Do you want to add another employee? (yes/no): ")

print("\n All employee data entered. Session completed")







