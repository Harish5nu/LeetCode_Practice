def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)  # Count vowels in string

# Example usage
s = "Hello World"
print(count_vowels(s))  # Output: 3 (e, o, o)
