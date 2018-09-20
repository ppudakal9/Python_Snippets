def palindrome(s):
    h = len(s) - 1
    l = 0
    while (h > 1):
        if s[l] != s[h]:
            return "Not a palindrome"
        l += 1
        h -= 1

    return "Is a Palindrome"

def isPalindrome(s):
    mid = len(s) // 2
    for i in range(0, mid):
        if s[i] != s[len(s) - i - 1]:
            return "Not a Palindrome"

    return "Is a palindrome"

def intPalindrome(num):
    if num < 0 or (num % 10 == 0 and num != 0) :
        return "Not a palindrome"

    reverse_num = 0
    while num > reverse_num:
        reverse_num = reverse_num * 10 + num % 10
        num = num // 10

    if num == reverse_num or num == (reverse_num // 10):
        return "Is a palindrome"



print(palindrome('-121'))
print(isPalindrome('-121'))
print(intPalindrome(121))
print(intPalindrome(-121))
print(intPalindrome(10))