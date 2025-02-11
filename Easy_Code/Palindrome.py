class Solution:
    def isPalindrome(self, x):
      
        return str(x)==str(x)[::-1]
sol=Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121)) 
print(sol.isPalindrome(10)) 