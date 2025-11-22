# @author: yprakash

import heapq

arr = [4, 6, 7, 1]
heapq.heapify(arr)
print(arr)
heapq.heappush(arr, 3)
print(arr)
while arr:
    print(heapq.heappop(arr))
