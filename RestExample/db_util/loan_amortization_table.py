

from loans import computeMonthlyPayment, interestAccrued, remainingBalance



# pmt = computeMonthlyPayment(10000 ,.10 ,20)
# print("payment " ,pmt)
# print("bal after 21", remainingBalance(21, 10000 ,.10 ,pmt))

initial_balance = 10000
annual_interest_rate = .10
number_of_months_in_term = 20
monthly_payment = computeMonthlyPayment(initial_balance,annual_interest_rate, number_of_months_in_term)
# print(monthly_payment)

header_template = "{:>6}  {:>10} {:>10} {:>10} {:>10}"
header = header_template.format("Month", "Bal", "Interest", "Pmt", "Rem Bal")
print(header)

for m in range(1,number_of_months_in_term+1):
    balance = remainingBalance(m,initial_balance, annual_interest_rate,monthly_payment)
    interest = interestAccrued(m,initial_balance, annual_interest_rate,monthly_payment)
    # (balance, interest) = balance_and_interest(m,initial_balance, annual_interest_rate,monthly_payment)
    balance_after_payment_and_interest = balance - monthly_payment + interest
    row_template = "{:6}  {:10.2f} {:10.2f} {:10.2f} {:10.2f}"
    row = row_template.format(m, balance, interest, monthly_payment, balance_after_payment_and_interest)
    print(row)

