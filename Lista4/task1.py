# Lesson4, Task1

# Create a dictionary for products with prices
products = {
    'banana': 2.5,
    'jam': 4.2,
    'eggs': 4,
    'milk': 2.3,
    'flour': 1.8
}

# Function to calculate average price
def calcAverage(products):
    return sum(price for key, price in products.items()) / len(products) 

# Print products with prices
for product, price in products.items():
    print (product + ": " + str(price))
print ()

# Calculate average price
print ("The average price is %.2f zloty." % calcAverage(products))
print ()

# Add new product
products['tea'] = 5.5

# Calculate new average price
print ("The new average price is %.2f zloty." % calcAverage(products))
print ()

# Delete a product
del products['tea']

# Calculate average price again
print ("The average price is %.2f zloty." % calcAverage(products))