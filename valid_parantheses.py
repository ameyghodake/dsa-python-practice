# Logic: if any one of these (,{,[ found in the string then count should be increased by 1
# if any one of these found ),},] then count should descreased by 1
# if all paratheses are balanced then count will be 0 in the end hence return true


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        round_count = 0
        curly_count = 0
        square_count = 0

        for i, char in enumerate(s):
            if char == "(":
                round_count = round_count + 1

            elif char == ")":
                round_count = round_count - 1
                if round_count < 0:
                    return False

        for i, char in enumerate(s):
            if char == "{":
                curly_count = curly_count + 1

            elif char == "}":
                curly_count = curly_count - 1
                if curly_count < 0:
                    return False

        for i, char in enumerate(s):
            if char == "[":
                square_count = square_count + 1

            elif char == "]":
                square_count = square_count - 1
                if square_count < 0:
                    return False

        return curly_count == 0 or round_count == 0 or square_count == 0


obj = Solution()
print(obj.isValid("(]"))
