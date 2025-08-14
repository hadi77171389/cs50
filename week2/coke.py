amount_due = 50
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    payment = input("insert coin: ")
    payment = int(payment)
    if payment in [25,5,10]:
        amount_due -= payment
    else:
        continue
print(f"Change Owed: {abs(amount_due)}")