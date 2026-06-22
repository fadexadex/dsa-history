def isPalindrome(self, s: str) -> bool:
        pali = ""
        for i in s:
            if i.isalnum():
                pali += i.lower()
        return pali == pali[::-1]