class Solution:
    def is_palindrome(self, text):
        cleaned_str = ''.join(char.lower() for char in str(text) if char.isalnum())
        return cleaned_str == cleaned_str[::-1]