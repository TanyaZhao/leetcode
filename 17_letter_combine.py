class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mapping = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }

        def recursive(letter, remainder):

            if len(remainder) == 0:
                letter_combine.append(letter)
            else:
                for letter_i in mapping[remainder[0]]:
                    recursive(letter+letter_i, remainder[1:])

        letter_combine = []

        if digits:
            recursive("", digits)
        return letter_combine

solution = Solution()
print(solution.letterCombinations("234"))