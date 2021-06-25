def isPalindrome(s):
    return s == s[::-1]
# Driver code
s = "san"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

    ##
    def pali(s):
        rev = ''.join(reversed(s))
        if(s==rev):
            return True
        return False
    pali("madam")

