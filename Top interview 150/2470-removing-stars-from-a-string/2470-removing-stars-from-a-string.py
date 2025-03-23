class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for k, v in enumerate(s):
            stack.append(v)
            if stack[-1] != "*":
                continue
            elif stack[-1] == "*":
                stack.pop()
                stack.pop()
        
        return "".join(stack)