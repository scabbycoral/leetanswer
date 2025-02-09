A=[100,113,110,85,105,102,86,63,81,101,94,406,101,79,94,90,97]
B=[]
for i in range(len(A)):
    if i!=0:
        B.append(A[i]-A[i-1])
def maximum_subarray(A, low, high):
    if low == high:
        return low, high, A[low]  # Base case: only one element
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = maximum_crossing_subarray(A, low, mid, high)
        print(left_sum,right_sum,cross_sum,low,mid,high)
        #通过分治法，将情况分成三个情况，结果出现在mid左，结果出现在mid右，结果的左在mid左右在mid右
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def maximum_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    left_low = mid
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            #这里不需要中断判断，因为只要sum加过任意一个复数，就一定比left_sum小
            #直到加了一个可以掩盖所有复数的A[i]，才可以继续更新位置
            left_sum = sum
            left_low = i
    
    right_sum = float('-inf')
    sum = 0
    right_high = mid
    for i in range(mid + 1, high + 1):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            right_high = i
    
    return left_low, right_high, left_sum + right_sum

low, high, max_sum = maximum_subarray(B, 0, len(B) - 1)
print(f"Maximum subarray is from index {low} to {high} with sum {max_sum}")
