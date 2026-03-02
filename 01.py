# 1. Initialize list1
list1 = ["C++", "Python", "Java"]

# 2. Assign list1 to list2 (This COPIES THE POINTER, not the data)
list2 = list1

print(f"Original list1: {list1}")
print(f"Original list2: {list2}")
print(f"Are they the same object in memory? {list1 is list2}")
print("-" * 30)

# 3. Modify list1
list1.append("Rust")

print("--- After list1.append('Rust') ---")
print(f"list1: {list1}")
print(f"list2: {list2}  <-- list2 changed too!")

# 4. Modify list2
list2.pop(0) # Remove "C++"

print("\n--- After list2.pop(0) ---")
print(f"list1: {list1}  <-- list1 reflects the change made to list2!")
print(f"list2: {list2}")