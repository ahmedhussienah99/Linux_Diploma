

char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter a single character.")
else:
    ascii_value = ord(char)
    print(f"ASCII value of '{char}' is {ascii_value}")
