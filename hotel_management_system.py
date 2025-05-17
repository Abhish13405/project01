menu={"burger":40,
      'pasta':50,
      'pizza':40,
      'salad':70,
      'coffee':80
}
# greet masage
print("welcome to my abhi cafe")
# show the items
print("burger:rs40\npasta:rs50\npizza:rs40\nsalad:rs70\ncoffee:rs70")
order_total=0
item_1=input("enter the name of item you want to order=")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1} has been  added to your order")
    print("total amount of order",+order_total)

else:
    print(f"ordered item {item_1} is not avaialable yet")
    another_order=input("Do you want to add another item? (yes/no)")
    if another_order== "yes":
     item_2=input("enter the name of  second item =")
     if item_2 in menu:
        order_total+=menu[item_2]
     print(f"item {item_2} has been added to order")
    else: 
       print(f" orderd item {item_1} is not avialable ")
    print("total amount of order",+order_total)
