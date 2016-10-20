# Lesson2, Task5

# create an oath and print it
oath = "\
wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście: \n\
- zdobywać wiedzę i umiejętności, \n\
- postępować zgodnie z prawem, tradycją i dobrymi obyczajami akademickimi, \n\
- dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.\
"
print (oath)
print ()

# start an oath with a capital letter
oath = list(oath)
oath[0] = oath[0].upper()
oath = "".join(oath)

# calculate amount of letters 'i' and conjunctions 'i'
print ("Amount of letters 'i': %i" % oath.count("i")) 
print ()
print ("Amount of conjunctions 'i': %i" % oath.count(" i ")) 
print ()

# check wheather the word 'Uniwersytet' is in the oath
word = "Uniwersytet"
if word in oath:
    print ("There is a word '%s' in the oath." % word)
else:
    print ("There is no word '%s' in the oath." % word)
print ()

# create lists of words and strings from oath
listOfWords = oath.split()
listOfStrings = oath.split('\n')

# delete all '-' from the words list
while '-' in listOfWords:
    listOfWords.remove('-')

# delete signs ',', '.' and ':' from the words in words list
for i in range(len(listOfWords)):
    listOfWords[i] = listOfWords[i].replace(',', '')
    listOfWords[i] = listOfWords[i].replace('.', '')
    listOfWords[i] = listOfWords[i].replace(':', '')

# print results
print (oath)
print()
print (listOfWords)
print()
print (listOfStrings)