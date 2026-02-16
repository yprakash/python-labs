a = [1, 2, 3]  # a is a list (mutable)
b = a  # points to the same list object in memory as a
a += [4]  # Using the += operator with a mutable object like a list modifies the original object in place.
print(b)  # Output: [1, 2, 3, 4]

s = "hello"  # s is a string (immutable)
t = s  # When we create t, it points to the same string object in memory as s
print(t is s)  # returns True
s += " world"
# However, using the += operator with an immutable object like a string creates a new object,
# rather than modifying the original object in place.
print(t)  # Output: "hello"
