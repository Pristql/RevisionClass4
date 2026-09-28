print("ATM Cash Dispenser")
total100=total50=total20=total10=total5=total1=0
customers_served=0
total_dispensed=0
serving=True
while serving:
    name=input("Enter customer name")
    amount=int(input(f"Hello {name}! Enter withdrawal amount: "))
    if amount<=0:
        print("Invalid amount. Please enter a positive number")
        continue
    print(f"Dispensing {amount} units for {name}: ")
    remaining=amount
    idx=1
    while idx<=6:
        if idx==1: value=100
        elif idx==2: value=50
        elif idx==3: value=20
        elif idx==4: value=10
        elif idx==5: value=5
        else: value=1
        count=remaining//value
        if count>0:
            print(f"{count}x{value}-unit note(s)= {count*value}")
            remaining-=count*value
            if value==100: total100+=count
            elif value==50: total50+=count
            elif value==20: total20+=count
            elif value==10: total10+=count
            elif value==5: total5+=count
            else: total1+=count
        idx+=1
    customers_served+=1
    total_dispensed+=amount
    print(f"Transaction complete, {name}?")
    again=input("Next customer? (yes/no): ").strip().lower()
    if again !="yes":
        serving=False
print("Daily denomination report!")
for slot in range(1, 7):
    if slot==1: value,total=100, total100
    elif slot==2: value, total=50, total50
    elif slot==3: value, total=20, total20
    elif slot==4: value, total=10, total10
    elif slot==5: value, total=5, total5
    else: value, total=1, total1
    if total>0:
        print(f"{value}-unit notes dispensed: {total} ", end="")
        for note in range(total):
            print("=", end="")
        print()
print(f"Customers served: {customers_served}")
print(f"Total dispensed: {total_dispensed}")
print("ATM session closed. Goodbye!")