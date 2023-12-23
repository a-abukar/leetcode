# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, the task is to find indices of the two numbers such that they add up to `target`. It is assumed that each input has exactly one solution, and the same element cannot be used twice. The answer can be returned in any order.

### Examples
1. Input: `nums = [2,7,11,15]`, `target = 9`
   Output: `[0,1]`
   Explanation: nums[0] + nums[1] == 9, we return [0, 1].
2. Input: `nums = [3,2,4]`, `target = 6`
   Output: `[1,2]`
3. Input: `nums = [3,3]`, `target = 6`
   Output: `[0,1]`

### Constraints
- 2 <= `nums.length` <= 10^4
- -10^9 <= `nums[i]` <= 10^9
- -10^9 <= `target` <= 10^9
- Only one valid answer exists.

## Approach
Used a hash map to track the indices of elements, and as soon the complement equals the difference in the target and the current num, it will print both their indices. Given that the dictionary holds the complement value.

## Solution
- [solution.py](./solution.py)
