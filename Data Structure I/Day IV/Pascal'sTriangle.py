# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers 
# directly above it as shown

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        out = []
        for i in range(0,numRows+1):
            output = []
            C=1
            for j in range(1,numRows-i+1):
                C=C * (i - j) // j
                if C > 0:
                    output.append(C)
            out.append(output)
        return out





sol = Solution()
sol.generate(6)
