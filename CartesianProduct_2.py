class letter_combinations:
    def __init__(self):
        self.dict_char = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']
                     }

    def letterCombinations(self, digits):
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits or digits == "":
            return []
        else:
            res = []
            n = len(digits)
            self.helper(res, "", digits, mapping, n)
            return res

    def helper(self, res, curr, digits, mapping, length):
        if digits == "":
            res.append(curr)
            return
        else:
            char_mapping = mapping[digits[0]]
            for char in char_mapping:
                self.helper(res, curr + char, digits[1:len(digits)], mapping, length)


obj = letter_combinations()
print(obj.letterCombinations("23"))