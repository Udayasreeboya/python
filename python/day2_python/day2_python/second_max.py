nums = [10, 20, 5, 30, 25]
first =nums[0] 
second = nums[1]

for i in nums:
    if i > first:
        second = first
        first = i
    elif i> second and i != first:
        second = i

print("Second largest:", second)
