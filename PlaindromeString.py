import re
class Solution:
    # solution 2
    def is_palindrome(self, text:str)->bool:
        cleaned_str = re.sub(r'[^a-zA-Z0-9]','',text)
        return cleaned_str.lower() == cleaned_str[::-1].lower()

    # solution 1
    """
    def is_palindrome(self, text:str)->bool:       
        string_list = list(text)       
        alphanumeric_list = [char for char in string_list if char.isalnum()]       
        alphanumeric_string = ''.join(alphanumeric_list).lower()
        reverse_string = ''.join(alphanumeric_list[::-1])        
        if alphanumeric_string == reverse_string:
            return True
        else:
            return False 
            
    """       

Obj = Solution()
print(Obj.is_palindrome("A man, a plan, a canal: Panama"))