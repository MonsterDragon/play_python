import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# nums = numsq.numsify(nums)
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(4, nums))
print(sorted(nums)[-3:])
print(sorted(nums)[:-4:-1])
