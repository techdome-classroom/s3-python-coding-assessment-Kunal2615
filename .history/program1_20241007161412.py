class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in bracket_map:  # If it's an opening bracket
                stack.append(bracket_map[char])  # Push the corresponding closing bracket onto the stack
            else:
                # If it's a closing bracket, check for a match
                if not stack or stack.pop() != char:
                    return False

        # If the stack is empty, all brackets were matched
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))       # Output: True
print(solution.isValid("()[]{}"))   # Output: True
print(solution.isValid("(]"))       # Output: False







    



  

