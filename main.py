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
  tax_rate = tax_dict[state]
  return tax_rate
# We need price of an item


def get_item():
  item_name = input("What item are you buying?")
  price = float(input("What is the price of your item?"))
  return item_name, price

def calculate_tax(price, tax_rate):
  sales_tax = price * tax_rate 
  total = price + sales_tax
  return total, sales_tax

def receipt():
  print(f"You purchased {item_name}")
  print(f"The price of your item is $ {price}")
  print(f"You paid ${sales_tax: .2f} in sales tax")
  print(f"The total cost is {total: .2f}")

item_name, price = get_item()
tax_rate = set_tax_rate()
total, sales_tax = calculate_tax(price, tax_rate) 
receipt()
