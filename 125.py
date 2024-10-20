class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        start_index = 0
        end_index = len(s) - 1

        while start_index < end_index:
            while not s[start_index].isalnum() and start_index < end_index:
                start_index = start_index + 1

            while not s[end_index].isalnum() and start_index < end_index:
                end_index = end_index - 1

            if s[start_index].lower() != s[end_index].lower():
                return False 
            
            start_index = start_index + 1
            end_index = end_index - 1
            
        return True
        

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome(".,"))