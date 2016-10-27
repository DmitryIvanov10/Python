# Lesson3, Task4

# groceries list
grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']

# amount of items
n_items = []

# prohibited items
prohibited = ['wódka', 'piwo', 'wino']

# Ask user how many items is needed
for product in grocery:
    if product in prohibited:
        n_items.append(0)
    else:
        print ("Produkt %s: sztuk = " % product, end = '')
        n_items.append(eval(input()))
        
# Print the groceries list with amount of products
print ()
print("{:-^50}".format("Lista zakupów"), end="\n\n")

for i, item in enumerate(grocery):
    if item in prohibited:
        print(str(i+1) + ". " + item + ": " + 'zakazane')
    else:
        print(str(i+1) + ". " + item + ": " + str(n_items[i]))