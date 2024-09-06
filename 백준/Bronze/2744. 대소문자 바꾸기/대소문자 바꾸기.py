text = input()
upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_cases = "abcdefghijklmnopqrstuvwxyz"

for char in text:
    if char in upper_cases:
        print(char.lower(), end='')
    elif char in lower_cases:
        print(char.upper(), end='')