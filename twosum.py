#method or function
def two_sum(nums, target):
    #hashmap or equivalent
    num_map = {}
    #for to iterate values of given array
    for i, num in enumerate(nums):
        #to find difference to know the matching number
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)