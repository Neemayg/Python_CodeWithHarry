# S1 is a set of integers and strings
S1 = {1, 3, 5, 5, 5, 5, 'Neeraj', 33}

# S2 is a set of integers
S2 = {4, 5, 6, 4, 4, 5, 4, 6, 4}

# Print the type of S1 (Correct way to call type())
print(type(S1))

# Add an element to S1
S1.add(11)
print(S1)

# Remove an element from S1
S1.remove(5)
print(S1)

# Clear all elements from S1 (Corrected: No arguments passed to clear())
S1.clear()
print(S1)

# Perform set intersection and print
print(S1.intersection(S2))

# Perform set union and print
print(S1.union(S2))

# Check if a set is a subset of another and print
print({3, 5}.issubset(S1))
print({4, 5}.issubset(S2))
