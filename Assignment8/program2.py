class ParenthesesValidator:
    def __init__(self):
        self.opening_brackets = set(['(', '[', '{'])
        self.closing_brackets = set([')', ']', '}'])
        self.bracket_pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
    
    def is_valid(self, s):
        stack = []
        for c in s:
            if c in self.opening_brackets:
                stack.append(c)
            elif c in self.closing_brackets:
                if not stack:
                    return False
                if stack[-1] == self.bracket_pairs[c]:
                    stack.pop()
                else:
                    return False
        return not stack