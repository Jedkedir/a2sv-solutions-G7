class Solution:
    def isValid(self, s: str) -> bool:
        lookup={
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []
        for ch in s:
            if ch in lookup:
                if stack == []:
                    return False
                if stack[-1] == lookup[ch]:
                    stack.pop()
                else:
                    return False
            elif ch =='(' or ch=='[' or ch=='{':
                stack.append(ch)
            else:
                continue
        return not stack