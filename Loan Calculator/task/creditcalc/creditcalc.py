import math

print("What do you want to calculate?")
print("type 'n' for number of monthly payments,")
print("type 'a' for annuity monthly payment amount,")
print("type 'p' for loan principal")

questionType = str(input())
# what is the number of monthly payments for this client?
if questionType == 'n':
    print("Enter the loan principal:")
    loanPrincipal = int(input())
    print("Enter the monthly payment:")
    monthlyPayment = int(input())
    print("Enter the loan interest:")
    rawInterest = float(input())
    i = rawInterest / (12 * 100)
    base = 1 + i
    x = (monthlyPayment / (monthlyPayment - i * loanPrincipal))
    n = math.log(x, base)
    months = math.ceil(n)
    monthsToYears = math.floor(months / 12)
    monthsBalance = months % 12
    if monthsToYears == 1 and monthsBalance == 0:
        print("It will take 1 year to repay this loan!")
    if monthsToYears == 0:
        print(f"It will take {monthsBalance} months to repay this loan")
    else:
        print(f"It will take {monthsToYears} years and {monthsBalance} months to repay this loan")
# what is the $ of payments monthly aka annuity
if questionType == 'a':
    print("Enter the loan principal:")
    loanPrincipal = int(input())
    print("Enter the number of periods:")
    n = int(input())
    print("Enter the loan interest:")
    rawInterest = float(input())
    i = rawInterest / (12 * 100)
    monthlyPayment = loanPrincipal * (i * pow((1 + i),n))/ (pow((1 + i), n) - 1)
    print(f"Your monthly payment = {math.ceil(monthlyPayment)}!")

# what is the loan principal
if questionType == "p":
    print("Enter the annuity payment:")
    monthlyPayment = float(input())
    print("Enter the number of periods:")
    n = float(input())
    print("Enter the loan interest:")
    rawInterest = float(input())
    i = rawInterest / (12 * 100)
    loanPrincipal = monthlyPayment / (i * ((i + 1) ** n) / (((1 + i) ** n)-1 ))

    print(f"Your loan principal = {loanPrincipal}")
