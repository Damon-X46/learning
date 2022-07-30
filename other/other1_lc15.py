"""
    三数之和
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
    请你找出所有和为 0 且不重复的三元组。
"""
def threeSum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        if nums[i] > 0:
            break
        if i >= 1 and nums[i] == nums[i - 1]:   # 去重
            continue
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left != right and nums[left] == nums[left + 1]:
                    left += 1
                while left != right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result

aaa = threeSum([-1,0,1,2,-1,-4])
print(aaa)      # [[-1, -1, 2], [-1, 0, 1]]