class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome_between(left: int, right:int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left_pointer , right_pointer = 0, len(s) -1
        while left_pointer < right_pointer:
            if s[left_pointer] != s[right_pointer]:
                skip_left_pointer = palindrome_between(left_pointer + 1, right_pointer)
                skip_right_pointer = palindrome_between(left_pointer, right_pointer - 1)
                return skip_left_pointer or skip_right_pointer
            left_pointer += 1
            right_pointer -= 1
        return True