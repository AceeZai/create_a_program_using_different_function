#Prog01: Smallest Number
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
print(min(first_number, second_number))

# Prog02: Inequality Check
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
if first_number != second_number:
    print("Not Equal")

# Prog03: Simple Subtraction
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
print(first_number - second_number)

# Prog04: Floor Division
dividend = int(input("Enter first number: "))
divisor = int(input("Enter second number: "))
print(dividend // divisor)

# Prog05: Modulo Operation
dividend = int(input("Enter first number: "))
divisor = int(input("Enter second number: "))
print(dividend % divisor)

# Prog06: Cumulative Subtraction
numbers_list = [float(input(f"Number {index + 1}: ")) for index in range(10)]
result = numbers_list[0] - sum(numbers_list[1:])
print(result)

# Prog07: Count Even Entries
evens_count = 0
for count in range(10):
    user_input = int(input(f"Number {count + 1}: "))
    if user_input % 2 == 0:
        evens_count += 1
print(evens_count)

# Prog08: Odd Numbers (While Loop)
current_value = 0
while current_value <= 100:
    if current_value % 2 != 0:
        print(current_value)
    current_value += 1

# Prog09: Filtered Sequence
for current_number in range(101):
    if current_number % 5 != 0:
        print(current_number)

# Prog10: Range of Numbers
start_number = int(input("Enter first number: "))
end_number = int(input("Enter second number: "))

for middle_number in range(min(start_number, end_number) + 1, max(start_number, end_number)):
    print(middle_number)
