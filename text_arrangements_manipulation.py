#manipulate_text_arrangements.py
#Prog01: Display Only Non-Duplicates
user_numbers = [float(input(f"Number {index + 1}: "))
for current_number in user_numbers:
    if user_numbers.count(current_number) == 1:
    	print(current_numbers)
    
#Prog02: Unique Entries Only (First Occurrences)
user_numbers = [float(input(f"Number {index + 1}: ")) for index in range(10)]
seen_numbers = []
for current_number in user_numbers:
    if current_number not in seen_numbers:
        print(current_number)
        seen_numbers.append(current_number)
        
#Prog03: Real-time Duplicate Checker
history_list = []
while True:
    user_input = input("Enter a number: ")
    if not user_input.replace('.', '', 1).isdigit():
        break
    
    current_number = float(user_input)
    if current_number in history_list:
        print("Duplicate")
    else:
        print("Unique")
    history_list.append(current_number)
     
#Prog04: Track Lowest Value
lowest_number = None
while True:
    user_input = input("Enter a number: ")
    if not user_input.replace('.', '', 1).isdigit():
        break
        
    current_number = float(user_input)
    if lowest_number is None or current_number < lowest_number:
        lowest_number = current_number

if lowest_number is not None:
    print(f"Lowest: {lowest_number}")
        
#Prog05: Continuous Sort
collected_numbers = []
while True:
     user_input = input("Enter a number: ")
     
     if not user_input.replace('.', '', 1).isdigit():
        break
    
    collected_numbers.append(float(user_input))
    collected_numbers.sort()
    print(f"Sorted list: {collected_numbers}")