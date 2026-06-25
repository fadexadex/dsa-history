def maxSum(nums):
    maxNum = -1
 
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            l_arr_int = [int(val) for val in str(nums[i])]
            r_arr_int = [int(val) for val in str(nums[j])]
            
            total = nums[i] + nums[j]
            if max(l_arr_int) == max(r_arr_int) and total > maxNum:
                maxNum = total
    
    return maxNum 