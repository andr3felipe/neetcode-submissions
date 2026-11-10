class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {"}":"{", ")":"(", "]":"["}


        for character in s:
            if character in dictionary:
                if stack and stack[-1] == dictionary[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        return True if not stack else False