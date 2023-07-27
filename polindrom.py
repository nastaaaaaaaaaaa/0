def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("лепсспел"))
print(is_palindrome("helloworld"))