#Program 1
#Ask for name with leading spaces. ex; ____ Acee Zai Mendez
full_name = input("Enter your full name: ")
#Use lstrip.(), this function removes spaces in the beginning of a string
clean_name = full_name.lstrip()
#Print clean_name
print(clean_name)

#Program 2
#Ask for numbers 0-1000
num_input = int(input("Enter a number (0-1000): "))
num_sixdigit = f"{num_input:06}"
print(num_sixdigit)

#Program 3
#Input mixed lower and uppercase names
full_name = input("Please enter your full name in mixed lower and uppercasing style: ")
#Use upper() function
uppercase_name = full_name.upper()
print(uppercase_name)

#Program 4
#Use the code from upper but use lower() function
full_name = input("Please enter your full name in mixed lower and uppercasing style:  ")
lowercase_name = full_name.lower()
print(lowercase_name)

#Program 5
#A program to convert incorrect casing to proper casing
incorrect_casing = input("Please enter your name with incorrect casing: ")
#Use title() function (Converts the first character of every word in a string to uppercase and the remaining characters to lowercase, returning a new, title-cased string.)
proper_casing = incorrect_casing.title()
print(proper_casing)

#Program 6
#This program will reverse your original casing style.
original_name = input("Enter your name in different casing styles: ")
reverse_casing = ''.join([c.lower() if c.isupper() else c.upper() for c in full_name])
print(reverse_casing)

#Program 7 
#Count the number of words
input_words = input("Enter a sentence: ")
#len function couns the number of elements 
word_count = len(statement.split())
print(word_count)

#Program 8
#Will count the number of characters in a name
full_name = input("Enter your full name: ")
character_count = len(full_name)
print(character_count)

#Program 9
#Convert name's casing style into Pascal casing style
incorrect_casing_name = input("Enter your full name in incorrect casing: ")
pascal_name = ''.join([word.capitalize() for word in full_name.split()])
print(pascal_name)

#Program 10
#Convert name's casing style into Snake casing style
incorrect_casing_name = input("Enter your full name in incorrect casing: ")
snake_name = '_'.join([word.lower() for word in full_name.split()])
print(snake_name)

