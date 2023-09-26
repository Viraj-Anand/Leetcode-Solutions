class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    
        n=len(matrix)

        left,right=matrix[0][0],matrix[n-1][n-1]

        while left<right:
            i=0
            j=n-1
            mid=left+(right-left)//2
            count=0
            while i<n and j>=0:
                if matrix[i][j]<=mid:
                    count+=j+1
                    i+=1
                else:

                    j-=1

            if count<k:
                left=mid+1
            else:
                right=mid

        return left


        