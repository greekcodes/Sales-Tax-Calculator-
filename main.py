# We need sales tax rate
# To Do
# 1: Add all 50 states + Puerto Rico
# 2: Grab the tax rate from the s=dictionary using its abbreviation
# 3: Return that tax rate for use elsewhere in our code

def set_tax_rate():
  state = input("Enter the abbreviation for your state:\n")
  tax_dict = {"NJ":0.066, 
              "DE":0.00,
              "OR":0.00
              
             
             
             }
# We need price of an item

def get_item():
  item_name = input("What item are you buying?")
  price = float(input("What is the price of your item?"))
  return item_name, price
  