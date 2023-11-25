class Solution:
    def climbStairs(self, n: int) -> int:
        num1 = 0
        num2 = 1
        for i in range(n):
            temp = num1
            num1 = num2
            num2 = temp + num2
        return num2ls

