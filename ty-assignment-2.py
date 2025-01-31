# SIMPLE DATA TYPES

name = "Trey"
print("name:", name, "type:", type(name))

has_license = True
print("has license:", has_license, "type:", type(has_license))

this_year = 2025
print("this year:", this_year, "type:", type(this_year))

next_year = 2026
print("next year:", next_year, "type:", type(next_year))
print(f"")

# MATHEMATICAL OPERATIONS

# ORIGINAL TAXES AND PRICE
purchase_price = 66666.66
provincial_tax = 7 # 7%
federal_tax = 5 # 5%

# TAX/PRICE CALCULATIONS
provincial_tax = purchase_price * (provincial_tax / 100)
federal_tax = purchase_price * (federal_tax / 100)
total_tax = provincial_tax + federal_tax
total = purchase_price + total_tax

# NON FORMATTED PRICE
print("purchase price:", purchase_price, "provincial tax:", provincial_tax, "federal tax:", federal_tax, "total:", total)

# FORMATTED PRICE
print(f"purchase price: ${purchase_price} provincial tax: ${provincial_tax:,.2f} federal tax: ${federal_tax:,.2f} total: ${total:,.2f}")
print(f"")

# LISTS

# List of integers
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(list))
print(list) 

list.insert(4, "Trey")
print(list)

list.remove(9)
print(list)

newlist = ["A", "B", "C"]
newnewlist = list + newlist
print(newnewlist)
print(f"")

# TUPLES

provinces = ('British Columbia', 'Manitoba', 'Alberta', 'Ontario')
print(type(provinces))
print(provinces)