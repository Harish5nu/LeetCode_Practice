def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Pointer to track position of unique elements
    unique_index = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[unique_index] = nums[i]
            unique_index += 1

    return unique_index

# Example usage
nums = [1, 1, 2, 2, 3, 3, 4]
length = remove_duplicates(nums)
print(f"New length: {length}")
print(f"Updated array: {nums[:length]}")  # Output: New length: 4, Updated array: [1, 2, 3, 4]
