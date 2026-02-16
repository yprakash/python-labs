# Python Integers are cached, meaning that they are objects that are already created as the interpreter starts.
# So, when one assigns the number 10 to the variable a, the interpreter simply reuses that object.
# This has some interesting implications when using the identity operator `is`.
# However, if you compare any numbers using the identity operator that are not in the range of -5 to 256, then you will get a different result:

a = 10
b = 10
print(a is b)  # Output: True

c = 300
d = 300
print(c is d)  # Usually False, But this is an implementation detail, not guaranteed by the language.

c = int("300")
d = int("300")
print(c is d)  # Output: False, Now Python constructs them separately at runtime.

# c == d   # Correct for numeric comparison
# Use `is` only for: None, singletons (e.g., True, False)

# Small integers are guaranteed to be interned (Cached) in CPython.
# Larger integers may be reused depending on compiler optimizations.
# Never rely on `is` for numeric comparison.
