from collections import Counter
def first_unique(s):
	char_count=Counter(s)	#Count frequency of each character
	for i, char in enumerate(s):
		if char_count[char]==1:
			return i
	return -1
print(first_unique("leetcode"))      
print(first_unique("loveleetcode"))  
print(first_unique("aabb"))  