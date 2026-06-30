# use a set 
# or convert a set to an array

# check through every num in the first array and if the num 
# in second array, add to the set

# return the set in an array form
class Solution(object):
    def intersection(self, nums1, nums2):
        uniq = set()
        numSet = set(nums2)
        for i in nums1:
            if i in nums2:
                uniq.add(i)
        return list(uniq)
        
 

# return list(set(nums1) & set(nums2))

