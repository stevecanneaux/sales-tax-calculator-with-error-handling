#using simple functions
def calcsalestax(aPrice, aSalestax):
    total = aPrice+(aPrice * aSalestax/100)
    print("total cost: ", total)
item_price = input("item price? ")
item_sale_tax = input("tax price? ")
item_price_check = item_price
item_sale_tax_check = item_sale_tax
try:
    item_price_check = float(item_price)
except:
    item_price_check = -1
try:
    item_sale_tax_check = float(item_sale_tax)
except:
    item_sale_tax_check = -1
if item_price_check <= -1:
    print("please enter valid item price number")
elif item_sale_tax_check <= -1 :
    print("please enter a valid tax number")
else:
    calcsalestax(item_price_check, item_sale_tax_check)