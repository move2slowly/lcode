import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        mid = len(s)//2 
        
        if(len(s)%2!=0):
            left = mid-1
            right = mid+1
            for i in range(mid):
                if(s[left]!=s[right]):
                    return False
                left-=1
                right+=1 
        else:
            left = mid-1
            right = mid
            for i in range(mid):
                if(s[left]!=s[right]):
                    return False
                left-=1
                right+=1 
        return True
