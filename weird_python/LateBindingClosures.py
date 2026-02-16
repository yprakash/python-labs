# The lambda does not capture the current value of i. It captures the variable i itself (a reference).
# The list comprehension finishes first. After the loop, i == 4 (last value from range(5)).
# So all lambdas effectively behave like: lambda x: x * 4
# Why this happens?
# Python closures capture variables by name, not by value.
# The value is looked up when the function is called, not when it is created.
# This is called late binding.
def main():
    funcs = [lambda x: x * i for i in range(5)]
    print([f(3) for f in funcs])  # [12, 12, 12, 12, 12]

# Correct way (freeze value at definition time)
# funcs = [lambda x, i=i: x * i for i in range(5)]
# Because i=i creates a new local default parameter for each lambda, capturing the current value.
# Alternative (cleaner, more explicit)
# def make_func(i):
#     return lambda x: x * i
#
# funcs = [make_func(i) for i in range(5)]
if __name__ == "__main__":
    main()
