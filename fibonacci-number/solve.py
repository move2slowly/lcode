class Solution:
    def fib(self, n: int) -> int:
        num1 = 0
        num2 = 1
        if(n==0): return 0
        for i in range(n-1):
            temp = num1 
            num1 = num2
            num2 = temp+num2
        return num2
            
