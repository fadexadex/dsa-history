# left = 0, right = len(nums)- 1
# while left < right:
    
# target - left
# is target - left = right
# No: left += 1


# sum = left + right
# if sum = target
# return index left + 1, index righht + 1

# if sum > target:
# right - 1
# if sum < target
# left + 1


def twoSum(self, numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum > target:
            right-=1
        else:
            left+=1


# OR

# seen = {}
# for i, num in enumerate(nums):
#     comp = target - num
#     if comp in seen:
#         return[seen[comp] + 1, i+1]
#     seen[num] = i
