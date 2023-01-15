# In MATLAB, there is a handy function called reshape which 
# can reshape an m x n matrix into a new one with a different 
# size r x c keeping its original data.

# You are given an m x n matrix mat and two integers 
# r and c representing the number of rows and the number of columns
#  of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of 
# the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and 
# legal, output the new reshaped matrix; Otherwise, 
# output the original matrix.



class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        x,y = len(mat),len(mat[0])
        if x*y != r*c:
            return mat
        newList = []
        for i in range(x):
            for j in range(y):
                newList.append(mat[i][j])
        
        newer2 = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for i in range(r):
            for j in range(c):
                newer2[i][j] = newList[k]
                print("k,i,j",k,i,j)
                k +=1
            
        return newer2



sol = Solution()
#mat = [[1,2],[3,4],[1,2],[3,4],[1,2],[3,4],[1,2],[3,4],[1,2],[3,4]]
mat = [[1,2],[3,4]]
sol.matrixReshape(mat,1,4)

