import math


#
# Compute some parameters in terms of the others
#

def computeMonthlyPayment(initBalance, annualRate, numberOfMonths):
    mrate = annualRate / 12
    payment_num = initBalance * mrate
    payment_denom = 1 - (1 + mrate) ** (-numberOfMonths)
    payment = payment_num / payment_denom
    return payment


def computeInitialBalance(annualRate, numberOfMonths, monthlyPayment):
    monthly_rate = annualRate / 12
    factor = 1 - (1 + monthly_rate) ** (-numberOfMonths)
    return monthlyPayment * factor / monthly_rate


def computeNumberOfMonths(initial_balance, annual_rate, monthly_payment):
    monthly_rate = annual_rate / 12
    a = initial_balance * monthly_rate / monthly_payment
    b = 1 - a
    c = 1 / b
    # 1 > a is necessary for this to work
    # monthly_payment > initial_balance * monthly_rate
    return math.log(c) / math.log(monthly_rate + 1)


def computeAnnualInterestRate(initial_balance, number_of_months, monthly_payment):
    i_low = 0
    i_hi = number_of_months * monthly_payment / initial_balance
    eps = 1e-10
    while math.fabs(i_hi - i_low) > eps:
        i_mid = (i_low + i_hi) / 2
        mp = computeMonthlyPayment(initial_balance, i_mid, number_of_months)
        if mp < monthly_payment:
            i_low = i_mid
        else:
            i_hi = i_mid
        print(i_low, i_mid, i_hi)
    return i_mid


#
# check parameter validity
#


def check_ib_ar_mp(initial_balance, annual_rate, monthly_payment):
    if initial_balance <= 0 or annual_rate <= 0 or monthly_payment <= 0:
        return False
    return monthly_payment > annual_rate * initial_balance / 12


def check_ib_nm_mp(initial_balance, number_of_months, monthly_payment):
    if initial_balance <= 0 or number_of_months <= 0 or monthly_payment <= 0:
        return False
    return initial_balance <= number_of_months * monthly_payment


#
# Compute in terms of all the parameters
#


def remainingBalance(m, initBalance, annualRate, monthlyPayment):
    """
    Balance at the end of month 'm' before adding interest accrued or subtracting payment.
    :param m:           Month number, at least 1
    :param initBalance:   Initial balance on the loan, positive
    :param annualRate:   Annual interest rate as a decimal, positive
    :param monthlyPayment: Monthly payment, positive
    :return: Balance at the end of month 'm' before adding interest accrued or subtracting payment.
    """
    if m == 1:
        return initBalance
    else:
        bal = remainingBalance(m - 1, initBalance, annualRate, monthlyPayment)
        # intrst = interestAccrued(m-1,initBalance,annualRate,monthlyPayment)
        intrst = bal * annualRate / 12
        return bal + intrst - monthlyPayment


def interestAccrued(m, initBalance, annualRate, monthlyPayment):
    """
    Computes the interest accrued during month 'm' on a loan
    :param m:           Month number, at least 1
    :param initBalance:   Initial balance on the loan, positive
    :param annualRate:   Annual interest rate as a decimal, positive
    :param monthlyPayment: Monthly payment, positive
    :return: interest accrued during month 'm'
    """
    return remainingBalance(m, initBalance, annualRate, monthlyPayment) * annualRate / 12


# def balance_and_interest(m,initBalance,annualRate,monthlyPayment):
#     """
#     Computes the interest accrued during month 'm' on a loan and
#     the balance (before adding interest and subtracting the payment) and
#     returns the pair of values
#     :param m:           Month number, at least 1
#     :param initBalance:   Initial balance on the loan, positive
#     :param annualRate:   Annual interest rate as a decimal, positive
#     :param monthlyPayment: Monthly payment, positive
#     :return: Pair of balance and interest accrued
#     """
#     if m == 1:
#         bal = initBalance
#     else:
#         bal = remainingBalance(m-1, initBalance, annualRate, monthlyPayment)
#     intrst = bal * annualRate / 12
#     return (bal + intrst - monthlyPayment,intrst)


if __name__ == "__main__":
    ib = 10000
    ar = .10
    nm = 20
    pmt = computeMonthlyPayment(10000, .10, 20)
    # print("payment ",pmt)
    # print("bal after 21", remainingBalance(21, 10000,.10,pmt))
    #
    # nm2 = computeNumberOfMonths(ib, ar, pmt)
    # print("number of months", nm2)
    # print("differ from actual", nm2-nm)
    #
    # ib2 = computeInitialBalance(ar, nm, pmt)
    # print("init bal", ib2)
    # print("differ from actual", ib2-ib)

    ar2 = computeAnnualInterestRate(ib, nm, pmt)
    print("annual rate:", ar2)

    ib = 10000
    nm = 20
    pmt = 500
    ar2 = computeAnnualInterestRate(ib, nm, pmt)
    print("annual rate:", ar2)
