# @author: yprakash

# You have a list you know is sorted. You are given a new number, and you want to find
# the first index which element is greater than or equal to the new number.

import bisect

arr = [1, 1, 2, 3, 4, 5, 5, 5, 5, 9]
x = 5

print(bisect.bisect_left(arr, x))
print(bisect.bisect_right(arr, x))
