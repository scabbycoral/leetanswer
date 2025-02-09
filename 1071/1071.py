# Python file for number 1071 
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1),len(str2)),0,-1):
            if len(str1)%i==0 and len(str2)%i==0:
                if str1[:i]*(len(str1)//i)==str1 and str1[:i]*(len(str2)//i)==str2:
                    return str1[:i]
        return ''
        
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length=math.gcd(len(str1),len(str2))
        if str1[:length]*(len(str1)//length)==str1 and str1[:length]*(len(str2)//length)==str2:
            return str1[:length]
        return ''
        
        
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length=math.gcd(len(str1),len(str2))
        if str1+str2==str2+str1:
            return str1[:length]
        return ''