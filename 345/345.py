# Python file for number 345 
class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j=0,len(s)-1
        major="aeiouAEIOU"
        s=list(s)
        while i<j:
            while i<len(s) and s[i] not in major:
                i+=1
            while j>0 and s[j] not in major:
                j-=1
            if i<j:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return ''.join(s)
        
#道理一样，只不过更好理解
class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j=0,len(s)-1
        major="aeiouAEIOU"
        s=list(s)
        while i<j:
            while i<len(s) and s[i] not in major:
                i+=1
            while j>0 and s[j] not in major:
                j-=1
            if i>=j:
                break
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return ''.join(s)
        
#道理一样，写在一个循环里
class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j=0,len(s)-1
        major="aeiouAEIOU"
        s=list(s)
        while i<j:
            if s[i] not in major:
                i+=1
            elif s[j] not in major:
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return ''.join(s)