def is_palindrome(s):
    if len(s)<2:
     return True

    if s[0]!=s[-1]:
        return False
    return is_palindrome(s[1:-1])   #if the first and last characters match,it's palindrome.
print(is_palindrome("hello"))       #if the first and last characters don't match,it's not palindrome.
