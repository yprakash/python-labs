# @author: yprakash

# Calculate the mean of a dataset. The data come in a stream of successive measurements of the parameter
# under analysis, and you need your function to retain the previous measurements between calls.
from math import sqrt


def mean():
    sample = []

    def inner_mean(number):
        sample.append(number)
        return sum(sample) / len(sample)
    return inner_mean


def standard_deviation():
    n = 0
    mean = 0
    power_sum = 0

    def std(x):
        nonlocal n, mean, power_sum
        n += 1
        new_mean = mean + (x - mean) / n
        power_sum += (x - mean) * (x - new_mean)
        mean = new_mean

        if n > 1:
            return n, mean, sqrt(power_sum / (n - 1))
        return n, mean, 0
    return std


sample_std = standard_deviation()
sample_mean = mean()
stream = [100, 105, 101, 98]
for n in stream:
    print(sample_mean(n), sample_std(n))
