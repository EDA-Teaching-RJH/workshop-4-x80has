price= 75
coins= [50,20,10,5]
initial = 0

while price>0:
    pay= int(input("enter the coins insterted : "))
    if pay in coins:
        price=price-pay
        initial =initial+pay

if initial > price:
    print(f"change owned : {initial-75}")
