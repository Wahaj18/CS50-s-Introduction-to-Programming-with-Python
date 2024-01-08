def main():
    amount_due = 50
    while True:

        print("Amount Due:", amount_due)
        input_amount = int(input("Insert Coin:"))
        if(input_amount == 25 or input_amount == 10 or input_amount == 5):
            amount_due -= input_amount
            if(amount_due>0):
                print("Amount Due:", amount_due)
            else:
                print("Change Owed:", abs(amount_due))
                break
        else:
            continue

main()




