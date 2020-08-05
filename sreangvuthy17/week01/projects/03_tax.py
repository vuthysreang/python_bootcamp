"""
    PROJECT 03: Tax Caculation
"""

# declaration the variable
program = True
running = True
# check loop condition
while running == True:
    # user input number of amount
    amount = input("Please enter your amount:\n>> ")
    # check the condition
    if amount.isdigit() == False or int(amount) < 0:
        # print output after above condition
        print("Number is incorrect, try again.")
    # check the condition
    elif amount.isdigit() == True and int(amount) >= 0:
        # check loop condition
        while program == True:
            # user input the number of rate
            rate = input("Please enter tax rate:\n>> ")
            # check the condition
            if rate.isdigit() == True and int(rate) >= 0 and int(rate) <= 99:
                # calculation TAX and NET
                tax = (float(amount) * float(rate)) / 100
                net = float(amount) - float(tax)

                # print output/Result
                print("===== ===== ===== =====")
                print("AMOUNT: " + str(amount) + "$")
                print("RATE: " + str(rate) + "%")
                print("===== ===== ===== =====")
                print("TAX: " + ('{:.2f}'.format(tax)) + "$")
                print("NET: " + ('{:.2f}'.format(net)) + "$")
                print("===== ===== ===== =====")
                # quit program
                exit()
            # check the other condition
            else:
                # print output
                print("Rate is incorrect, try again.")



