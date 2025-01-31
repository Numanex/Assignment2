# SIMPLE DATA TYPES

# USING THE PRINT FUNCTION
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

# LIST OF INTEGERS
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(list))
print(list) 

# INSERTING MY NAME
list.insert(4, "Trey")
print(list)

# REMOVING 9 FROM THE LIST
list.remove(9)
print(list)

newlist = ["A", "B", "C"]
newnewlist = list + newlist
print(newnewlist)
print(f"")

# TUPLES

provinces = ('British Columbia', 'Manitoba', 'Alberta', 'Ontario')
print(type(provinces)) #SHOWING THE DATA TYPE
print(provinces)
print(f"")

# DICTIONARIES

coins = { 
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25
}
print(type(coins)) # SHOWING THE DATA TYPE
print(coins)

# CHANGING THE VALUE TO A WHOLE NUMBER
coins['nickel'] = 5
coins['dime'] = 10
coins['quarter'] = 25
print(coins)

# ADDING LOONIE AND TOONIE TO THE DICTIONARY
coins.update({'loonie': 100, 'toonie': 200})
print(coins)
print(f"")

# SETS

twos = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print(type(twos))
print(twos)

fives = {5, 10, 15, 20}
print(fives)

# ADDING THE TWO SETS TOGETHER
newset = twos | fives
print(newset)
intersect = twos.intersection(fives)
print(intersect)

# FIRST SET
difference = twos.difference(fives) # GIVES THE DIFFERENCE
print(difference)

# SECOND SET
difference = fives.difference(twos) # GIVES THE DIFFERENCE
print(difference)