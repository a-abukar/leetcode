def twoSum(nums, target):
    """
    Finds two numbers in `nums` that add up to `target` and returns their indices.
    
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}  # create an empty dictionary
    for i, num in enumerate(nums):  # loop over numbers with their indices
        complement = target - num  # calculate the complement (how far the number is away from the target)
        if complement in dict:  # check if complement is in the dictionary
            return [dict[complement], i]  # Return indices of the complement and current number
        dict[num] = i  # store the number with its index in the dictionary. So if 2 is the number at index 0, then the dict will be {2:0}
        print(dict) # prints current state of the dictionary
    return []

# print(twoSum([2, 11, 7, 15], 9))  # Expected output: [0, 1]
print(twoSum([3, 2, 4], 6))       # Expected output: [1, 2]
# print(twoSum([3, 3], 6))          # Expected output: [0, 1]


