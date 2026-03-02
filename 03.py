# 1. The "False" string
string_fake_false = "False"

# 2. An actual empty string
string_empty = ""

print(f"Is the string '{string_fake_false}' truthy?")
if string_fake_false:
    print("-> Yes, because it is not empty.")
else:
    print("-> No.")

print(f"\nIs the string '{string_empty}' truthy?")
if string_empty:
    print("-> Yes.")
else:
    print("-> No, because it is empty.")

# Using the bool() constructor to see the raw boolean value
print("\n--- Raw Boolean Conversions ---")
print(f"bool('False')   => {bool('False')}")
print(f"bool('0')       => {bool('0')}")
print(f"bool(' ')       => {bool(' ')} (Even a single space is True!)")
print(f"bool('')        => {bool('')}")