class Solution:
    def removeVowels(self, S: str) -> str:
        list_of_vowels = ['a', 'e', 'i', 'o', 'u']
        new_string = ""
        for s in S:
            if s in list_of_vowels:
                pass
            else:
                new_string.append(s)
        return new_string

sol = Solution.removeVowels("leetcode")
print (sol)