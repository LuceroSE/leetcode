def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    print(right)

    while left <= right:
        middle = left + ((right - left) // 2)
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
        print("indices are ", left, "and", right)
    return -1
        
