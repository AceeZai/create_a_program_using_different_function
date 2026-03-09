# Prog01: rstrip()
text_input = input("Enter text: ")
index_pos = len(text_input) - 1
while index_pos >= 0 and text_input[index_pos] == " ":
    index_pos -= 1
print(f"Result: '{text_input[:index_pos + 1]}'")

# Prog02: removesuffix()
text_input = input("Enter text: ")
suffix_input = input("Enter suffix: ")
suffix_size = len(suffix_input)
print(f"Result: {text_input[:-suffix_size] if text_input[-suffix_size:] == suffix_input else text_input}")

# Prog03: upper()
text_input = input("Enter text: ")
upper_output = ""
for char_item in text_input:
    ascii_val = ord(char_item)
    upper_output += chr(ascii_val - 32) if 97 <= ascii_val <= 122 else char_item
print(f"Result: {upper_output}")

# Prog04: islower()
text_input = input("Enter text: ")
all_lower_check = True
for char_item in text_input:
    if 65 <= ord(char_item) <= 90:
        all_lower_check = False
        break
print(f"Result: {all_lower_check}")

# Prog05: startswith()
text_input = input("Enter text: ")
prefix_input = input("Enter prefix: ")
match_found = text_input[:len(prefix_input)] == prefix_input
print(f"Result: {match_found}")

# Prog06: rjust()
text_input = input("Enter text: ")
width_input = int(input("Enter width: "))
padding_size = width_input - len(text_input)
print(f"Result: '{(' ' * padding_size) + text_input if padding_size > 0 else text_input}'")

# Prog07: zfill()
text_input = input("Enter text: ")
width_input = int(input("Enter width: "))
padding_size = width_input - len(text_input)
print(f"Result: {('0' * padding_size) + text_input if padding_size > 0 else text_input}")

# Prog08: count()
text_input = input("Enter text: ")
char_target = input("Enter char: ")
total_count = 0
for char_item in text_input:
    if char_item == char_target:
        total_count += 1
print(f"Result: {total_count}")

# Prog09: index()
text_input = input("Enter text: ")
char_target = input("Enter char: ")
found_at = -1
for current_pos in range(len(text_input)):
    if text_input[current_pos] == char_target:
        found_at = current_pos
        break
print(f"Result: {found_at}")

# Prog10: rindex()
text_input = input("Enter text: ")
char_target = input("Enter char: ")
last_at = -1
for current_pos in range(len(text_input) - 1, -1, -1):
    if text_input[current_pos] == char_target:
        last_at = current_pos
        break
print(f"Result: {last_at}")