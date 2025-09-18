# Operators Activity 1: Basic Operators in Python ( Arithmetic, Comparison, Logical, Membership, Identity, Bitwise ) (Lumagod)
# This script demonstrates the use of various operators in Python:

# --- Arithmetic Example ---
x = float(input("Enter first number (x): "))
y = float(input("Enter second number (y): "))

print("\nArithmetic:")
print("x + y =", x + y)      # Adds the two numbers
print("x * y =", x * y)      # Multiplies the two numbers

# --- Comparison Example ---
print("\nComparison:")
print("x == y:", x == y)     # Checks if the numbers are equal
print("x > y:", x > y)       # Checks if x is greater than y

# --- Logical Example ---
a = bool(int(input("\nEnter 1 for True or 0 for False (a): ")))
b = bool(int(input("Enter 1 for True or 0 for False (b): ")))

print("\nLogical:")
print("a or b:", a or b)     # True if at least one is True
print("not a:", not a)       # Reverses the value of a

# --- Membership Example ---
fruits = ["apple", "banana", "cherry"]
check = input("\nEnter a fruit to check: ")

print("\nMembership:")
print(f"'{check}' in fruits:", check in fruits)  # Checks if the input is in the list
print(f"'{check}' not in fruits:", check not in fruits)  # Checks if the input is not in the list

# --- Identity Example ---
print("\nIdentity:")
num1 = int(input("Enter a number (num1): "))
num2 = int(input("Enter another number (num2): "))
print("num1 is num2:", num1 is num2)  # Checks if num1 and num2 are the same object
print("num1 is not num2:", num1 is not num2)  # Checks if num1 and num2 are not the same object

# --- Bitwise Example ---
print("\nBitwise:")
bit_a = int(input("Enter an integer (bit_a): "))
bit_b = int(input("Enter another integer (bit_b): "))
print("bit_a & bit_b (AND):", bit_a & bit_b)  # Bitwise AND
print("bit_a | bit_b (OR):", bit_a | bit_b)   # Bitwise OR
print("bit_a ^ bit_b (XOR):", bit_a ^ bit_b)  # Bitwise XOR
print("~bit_a (NOT):", ~bit_a)                # Bitwise NOT
print("bit_a << 1 (Left Shift):", bit_a << 1) # Left shift
print("bit_a >> 1 (Right Shift):", bit_a >> 1) # Right shift
# End of Operators Activity 1
# This script demonstrates the use of various operators in Python.