class Solution:
    def hammingWeight(self, n: int) -> int:
        numOneBits = 0
        while(n>0):
            numOneBits +=1
            n &=(n-1)
        return numOneBits
