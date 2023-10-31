class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        k=len(original)
        res=[]
        if k==m*n:
            for i in range(0,k,n):
                res.append(original[i:i+n])

        return res

        