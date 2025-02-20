class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res=''
        i=len(num1)-1
        j=len(num2)-1
        carry=0
        while i>=0 or j>=0:
            n1=int(num1[i]) if i>=0 else 0
            n2=int(num2[j]) if j>=0 else 0
            tmp=n1+n2+carry
            carry=tmp//10
            #进1
            res=str(tmp%10)+res
            #0-9部
            i,j=i-1,j-1
        return '1'+res if carry else res