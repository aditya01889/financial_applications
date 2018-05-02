import sys

cont = "y"

print("What would you like to do today?")
print("Please note, enter numbers only and in decimal form. e.g. 18% --> .18")

#BOND FUNCTION
def bond_in():
    while True:
        try:
            face_value = float(input("What is the face value of the bond? "))
            break
        except:
            print("Please enter a number.")
    while True:
        try:
            terms = int(input("How many years until maturity? "))
            break
        except:
            print("Please enter a whole number.")
    while True:
        try:
            coupon_rate = float(input("What is the coupon rate p/a? "))
            break
        except:
            print("Please enter a number.")
    while True:
        try:
            discount_rate = float(input("What is the discount rate p/a? "))
            break
        except:
            print("Please enter a number.")


    more_bond_options = input("Are the coupon and discount rates compounded semi-annually? Y/N ")

    if more_bond_options.lower() == "n":
        while True:
            try:
                coupon_rate_compound = int(input("How many times a year does the bond pay out? "))
                break
            except:
                print("Please enter a whole number.")
        while True:
            try:
                discount_rate_compound = int(input("How many times does the discount rate compound per year? "))
                break
            except:
                print("please enter a whole number.")
    else:
        print("You've selected Yes")
        coupon_rate_compound = 2
        discount_rate_compound = 2

    new_terms = terms*coupon_rate_compound
    effective_coupon = (coupon_rate/coupon_rate_compound)*face_value
    new_discount_rate = ((1 + (discount_rate/discount_rate_compound))**
                         (discount_rate_compound/coupon_rate_compound) - 1)

    first_calc = effective_coupon*((1-((1+new_discount_rate)**(new_terms*-1)))/new_discount_rate)
    sec_calc = face_value/(1+new_discount_rate)**new_terms
    bond_value = round(first_calc + sec_calc, 2)

    return (("\nTHE BOND IS WORTH ${:.2f}"
             .format(bond_value, effective_coupon, coupon_rate_compound, coupon_rate*face_value)))

#Equity Function
def equity_in():

    if eq_choice == "1":
        while True:
            try:
                last_dividend = float(input("What was the last dividend paid? "))
                break
            except:
                print("Please enter a number.")
        while True:
            try:
                div_gr_rate = float(input("What is the growth rate of the dividend? "))
                break
            except:
                print("Please enter a number.")
        while True:
            try:
                discount_rate = float(input("What is the discount rate? "))
                break
            except:
                print("Please enter a number.")

        if discount_rate < div_gr_rate:
            return "Error: Discount rate is less that growth rate"
        elif discount_rate - div_gr_rate == 0:
            return "Error: Discount Rate is == Growth Rate. Cannot Divide By 0"

        share_value = (last_dividend*(1+div_gr_rate))/(discount_rate - div_gr_rate)
        return("SHARE PRICE IS ${:.2f}".format(round(share_value, 2)))

    elif eq_choice == "2":
        first_stage_terms_list = []
        total_dividends = 0
        while True:
            try:
                first_stage_terms = int(input("How many periods in the first stage? "))
                break
            except:
                print("Please enter a whole number.")
        while True:
            try:
                div_gr_rate = float(input("What is the growth rate in the second stage? "))
                break
            except:
                print("Please enter a number.")
        while True:
            try:
                discount_rate = float(input("What is the discount rate? "))
                break
            except:
                print("Please enter a number.")

        if discount_rate < div_gr_rate:
            return "Error: Discount rate is less that growth rate"
        elif discount_rate - div_gr_rate == 0:
            return "Error: Discount Rate is == Growth Rate. Cannot Divide By 0."
        elif first_stage_terms = 0:
            return "Error: No terms in Stage 1."

        for term in range(1, first_stage_terms+1):
            term_div = float(input("What is the value of the dividend in period {}? ".format(term)))
            first_stage_terms_list.append(term_div)

        for i in range(1, len(first_stage_terms_list)+1):
            discounted_dividend = (first_stage_terms_list[i-1])/((1 + discount_rate)**i)
            total_dividends += discounted_dividend
            discounted_dividend = 0

        future_share_value = ((first_stage_terms_list[-1]*(1+div_gr_rate))/(discount_rate - div_gr_rate)/
            (1+discount_rate)**(len(first_stage_terms_list)))

        share_value = total_dividends + future_share_value

        return ("\nSHARE PRICE IS ${:.2f}".format(round(share_value, 2)))

"""
Functions Above
"""
while cont.lower() == "y":
    task = input("1. Bond Valuation\n2. Equity Valuation\n0. Exit\n")
    while not (task == "1") and not (task == "2") and not (task == "0"):
        task = input("Please enter 1 for Bond Valuation, 2 for Equity Valuation or 0 to Exit\n")

    if task == "1":
        print("You've chosen Bond Valuation\n")
        print(bond_in())
        cont = input("\nDo you want to do another valuation? Y/N ")
    elif task == "2":
        print("You've chosen Equity Valuation\n")
        eq_choice = input("1. Constant Growth Model\n2. Two-Stage DCF Model\n")
        print(equity_in())
        cont = input("\nDo you want to do another valuation? Y/N ")
    elif task == "0":
        break

print("\nHave a nice day!")
