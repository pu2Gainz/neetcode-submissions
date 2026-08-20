class Solution:
    def isPalindrome(self, s: str) -> bool:
        pre = 0
        post = len(s) - 1

        while pre < post:
            # print(s[pre], s[post])
            while pre < post and not self.alphaNum(s[pre]):
                pre += 1
            while pre < post and not self.alphaNum(s[post]):
                post -= 1
            if s[pre].lower() != s[post].lower():
                return False
            pre += 1
            post -= 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
        