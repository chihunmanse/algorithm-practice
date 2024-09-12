class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braket_mapping = {")" : "(", "}" : "{", "]" : "["}

        for braket in s:
            if braket in braket_mapping.values():
                stack.append(braket)
            else:
                if stack and stack[-1] == braket_mapping[braket]:
                    stack.pop()
                else:
                    return False

        return not stack