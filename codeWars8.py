def incrementer(nums):
    num = []
    count = 0
    for n in nums:
        count = count + 1
        num.append(int(repr(n + count)[-1]))
    return num

print(incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]))