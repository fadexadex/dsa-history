def search(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid

        # left half [lo..mid] is sorted
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # right half [mid..hi] is sorted
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1