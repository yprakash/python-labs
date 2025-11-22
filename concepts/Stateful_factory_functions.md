# Stateful Factory Functions in Python

Stateful factory functions create and return inner functions that
**retain state across multiple calls** without using classes, global
variables, or external state containers.\
They rely on Python's closure mechanism: the ability of an inner
function to capture and persist variables from its enclosing scope.

This pattern is powerful for building small, focused components that
behave like lightweight objects.
------------------------------------------------------------------------
## Why Stateful Factory Functions?
Use cases include:
- Processing **streaming data** 
- Maintaining **rolling aggregates** (mean, variance, etc.) 
- Implementing **accumulators**, **counters**, or **memoization**
- Creating **function instances** with persistent configuration or memory

Unlike classes, factory functions offer:
- Less boilerplate
- Localized encapsulation
- Natural functional style
- Explicit control over state access via closures

------------------------------------------------------------------------
## Understanding Closures
A closure forms when:
1. A function defines an inner function
2. The inner function uses variables from the outer function
3. The outer function returns the inner function

The returned inner function carries the captured state with it.

------------------------------------------------------------------------
# Example: Mean and Standard Deviation From a Stream

The code below processes a stream of numerical measurements.\
The mean and standard deviation must be updated incrementally, retaining prior values.

## Mean Using a Stateful Factory Function
``` python
def mean():
    sample = []                      # state

    def inner_mean(number):
        sample.append(number)        # mutating state
        return sum(sample) / len(sample)

    return inner_mean                # returning the closure
```
### How it works
-   `mean()` returns `inner_mean`
-   `inner_mean` closes over the `sample` list
-   Each call accumulates new data into `sample`
-   No global variables, no classes

------------------------------------------------------------------------
## Standard Deviation With Incremental Update (Welford's Algorithm)
``` python
def standard_deviation():
    n = 0
    mean = 0
    power_sum = 0

    def std(x):
        nonlocal n, mean, power_sum  # modifying outer-scope variables
        n += 1
        new_mean = mean + (x - mean) / n
        power_sum += (x - mean) * (x - new_mean)
        mean = new_mean

        if n > 1:
            return n, mean, sqrt(power_sum / (n - 1))
        return n, mean, 0

    return std
```
### Key Concepts
-   **`nonlocal`** enables the inner function to modify outer-scope variables
-   State evolves on each call:
    -   `n`: number of observations
    -   `mean`: incremental running mean
    -   `power_sum`: sum used for variance
-   Efficient: no list storage, constant memory

------------------------------------------------------------------------
## Using the Factories
``` python
sample_std = standard_deviation()
sample_mean = mean()

stream = [100, 105, 101, 98]

for n in stream:
    print(sample_mean(n), sample_std(n))
```
### What happens
-   `sample_mean` and `sample_std` are *stateful function instances*
-   Each holds its own private state
-   Every iteration updates both statistics incrementally

------------------------------------------------------------------------
## Why Not Use a Class?
Both implementations could be rewritten using a class:
``` python
class Mean:
    def __init__(self):
        self.sample = []

    def __call__(self, x):
        self.sample.append(x)
        return sum(self.sample) / len(self.sample)
```
However, factory functions offer: - Shorter, more expressive definitions
- Less syntactic overhead
- Natural functional style
- Encapsulation without additional namespaces

Use factory functions when the state is small and tied tightly to a single operation.

------------------------------------------------------------------------
## Summary
Stateful factory functions in Python: - Use **closures** to persist state between calls
- Provide a lightweight alternative to classes
- Offer a clean, functional approach to streaming computations
- Allow precise control over mutability and encapsulation

This example shows how they can elegantly implement rolling statistics
on a data stream without external state management.\
Use this pattern to build concise, high-performance stateful components in pure Python.
