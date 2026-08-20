class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        one = two = 0

        while one < len(abbr) and two < len(word):
            
            if abbr[one].isdigit():
                if abbr[one] == '0':
                    return False
                start = one
                while one < len(abbr) and abbr[one].isdigit():
                    one += 1
                two += int(abbr[start: one])

            elif one < len(abbr) and abbr[one].isalpha():
                if abbr[one] != word[two]:
                    return False
                one += 1
                two += 1

        return one == len(abbr) and two == len(word)
        return one == len(abbr) - 1 and two == len(word) - 1