# Coded by MJ. LI from Singapore Polytechnic (D.EEE), Royal Melbourne Institute of Tech (B.BUS MGMT) #
# Buy me a coffee? Send $USDT to ERC20 @ 0x250870A148EAbcE8F1C5AC4D55E48983f73fFb77 #
# DO NOT CHANGE THIS COMMENT, YOUR COFFEE FUNDS ARE APPRECIATED, THANK YOU. #

import time
import sys

def progressbar(it, prefix="", size=60, out=sys.stdout):
    count = len(it)
    start = time.time() # time estimate start
    def show(j):
        x = int(size*j/count)
        # time estimate calculation and string
        remaining = ((time.time() - start) / j) * (count - j)        
        mins, sec = divmod(remaining, 60) # limited to minutes
        time_str = f"{int(mins):02}:{sec:03.1f}"
        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count} Est wait {time_str}", end='\r', file=out, flush=True)
    show(0.1) # avoid div/0 

    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

print(f"> Welcome to HDB Public housing payment structure calculator done by MJ. LI")

calculator = 0
while calculator == 0:

    print(f"> What is your monthly individual/spouse combined income before CPF deduction?" )
    mth_income = float(input(">$"))
    print(f" ")

    if mth_income > 14000:
        print(f"> You are not eligible for public housing due to EXCEEDING the INCOME CEILING" )
        print(f"")
        print(f"> Do you want to recalculate? 'yes' or 'no'")
        recalculate = input(">").lower()
        print(f" ")
        if recalculate == "yes":
            continue
        elif recalculate == "no":
            break

    else:
        print(f"> What is the price of the property?")
        t_property_cost = float(input(">$"))
        print(f" ")

        print(f"> How many years of installment are you going to take?")
        years = float(input(">"))
        print(f" ")

        print(f"> Which loan are you going to take? HDB or bank? reply with 'hdb' or 'bank'")
        interest_type = str(input(">").lower())
        print(f" ")

        if interest_type == "hdb":
            interest_rate = float(2.6)

        elif interest_type == "bank":
            print(f"> What was the interest rate % quoted from the Banks?")
            interest_rate = float(input(">"))
            print(f" ")
        
        t_months = 12 * years
        max_loan = float(mth_income * 0.3 * t_months)

        t_down_payment = float(t_property_cost * 0.2)
        principal_loan = float(t_property_cost - t_down_payment)
        if max_loan < principal_loan:
            t_downpayment = float((principal_loan - max_loan) + t_down_payment)

        else:
            t_downpayment = float(t_down_payment)

        cash_payment = float(t_downpayment * 0.25)
        cpf_payment = float(t_downpayment * 0.75)

        principal = float(t_property_cost-t_downpayment)
        m_installment = float(principal_loan*(1+(interest_rate/100))**years / (12*years))
        m_cpf = float(0.2 * mth_income)
        m_deducted_cash = round(m_installment - m_cpf, 2)
        if m_deducted_cash < 0:
            m_cpf = round(m_installment + m_deducted_cash, 2)
            m_deducted_cash = 0

        if mth_income < m_installment:
            m_deducted_cash = 0
            t_down_payment = round(t_down_payment + principal_loan - m_cpf * 12 * years, 2)

        elif mth_income > m_installment:
            print(f"> Would you be willing to cover the remaining monthly mortgage OUT-OF-POCKET? 'yes' or 'no'?")
            pocket = input(">").lower()

            if pocket == "no":
                m_deducted_cash = 0
                t_down_payment = t_down_payment + principal_loan - m_cpf * 12 * years

            elif pocket == "yes":
                m_deducted_cash = m_deducted_cash

        print(f" ")

        for i in progressbar(range(100), "Calculating: ", 40):
            time.sleep(0.01)

        print(f"> Your complete down payment WITHOUT utilizing CPF Savings: ")
        print(f"> ${t_down_payment}/-")
        print(f" ")

        for i in progressbar(range(100), "Calculating: ", 40):
            time.sleep(0.01)
        
        print(f"> If using CPF Savings partially for the down payment, cash payment reduced to 5%: ")
        print(f"> ${cash_payment}/-")
        print(f" ")

        print(f"> The outstanding 15% down payment payable using CPF Savings: ")
        print(f"> ${cpf_payment}/-")
        print(f" ")

        for i in progressbar(range(100), "Calculating: ", 40):
            time.sleep(0.01)
        
        print(f"> Your monthly CPF Savings deduction for the next {years} years:")
        print(f"> ${m_cpf}/-")
        print(f" ")

        print(f"> Your monthly OUT-OF-POCKET expenses for the next {years} years: ")
        print(f"> ${m_deducted_cash}/-")
        print(f" ")

        leftover_cash = round(mth_income - m_deducted_cash - m_cpf, 2)
        print(f"> Your surplus in bank account each month after covering your HDB mortgage from your income: ")
        print(f"> ${leftover_cash}/-")
        print(f" ")

        print(f"> Do you want to recalculate? 'yes' or 'no' ")
        recalculate = input(">").lower()
        print(f" ")
        if recalculate == "yes":
            continue
        elif recalculate == "no":
            break