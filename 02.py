# 1. Setup: x and y are different boxes with same content. 
# z is just another pointer to the same memory address as x.
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x 

print(f"Initial x: {x} (ID: {id(x)})")
print(f"Initial z: {z} (ID: {id(z)})")
print(f"Initial y: {y} (ID: {id(y)})")
print("-" * 30)

# 2. THE CHANGE: We modify the list through the label 'z'
x.append("cherry")

print("--- After 'z.append(\"cherry\")' ---")

# x changed because it points to the same object as z
print(f"x is now: {x}") 

# z obviously changed
print(f"z is now: {z}") 

# y did NOT change because it's a different box in memory
print(f"y is still: {y}") 

# 3. Verification using the 'is' operator (Pointer comparison)
print("-" * 30)
print(f"Does x point to the same address as z? {x is z}") # Equivalent to: &x == &z in C++
print(f"Does x point to the same address as y? {x is y}")

print("")
print(x == y)