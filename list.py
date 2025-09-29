"""
Start with nums = [3, 5, 7, 9, 11]
Append 13 in place (one line).
Remove the first element in place (one line, no slicing).
Insert 0 at index 2 in place.
Print the final list and its id before and after all ops (must be same id).
Commit with message “Step 1: in-place only”.
"""

nums = [3, 5, 7, 9, 11]
print(id(nums))
nums.append(13)
del nums[0]
nums.insert(2, 0)
print(nums)
print(id(nums))