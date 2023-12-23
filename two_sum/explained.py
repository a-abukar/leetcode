def twoSum(nums, target):
    prevMap = {}  # Create an empty dictionary to store numbers and indices

    for i, num in enumerate(nums):
        print(f"Current number: {num}, at index: {i}")
        diff = target - num
        print(f"Needed number to reach target: {diff}")

        if diff in prevMap:
            print(f"Found the needed number {diff} at index {prevMap[diff]}")
            return [prevMap[diff], i]

        prevMap[num] = i
        print(f"Storing the number {num} at index {i} in the dictionary")

    print("No two numbers add up to the target")
    return []

# Example usage
print(twoSum([2, 11, 7, 15], 9))  # Expected to return [0, 2]
