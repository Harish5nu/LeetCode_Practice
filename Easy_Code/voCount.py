def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)  # Count vowels in String

# Example usage
s = "Hello Worlds...."
print(count_vowels(s))  # Output: 3 (e, o, o)
