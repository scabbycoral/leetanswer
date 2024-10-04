class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]%2==1:
                while j>i:
                    if nums[j]%2==0:
                        nums[i],nums[j]=nums[j],nums[i]
                        #print(nums)
                        j-=1
                        i+=1
                        #print(i,j)
                        break
                    else:
                        j-=1
                        #print('j',j)
            else:
                i+=1
                #print('i',i)
                
        return nums