"""
    四数之和
    给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
    请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]]（若两个四元组元素一一对应，则认为两个四元组重复）：
        0 <= a, b, c, d < n
        a、b、c 和 d 互不相同
        nums[a] + nums[b] + nums[c] + nums[d] == target
"""
def fourSum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:            # 去重
            continue
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:     # 去重
                continue
            left = j + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
    return result

aaa = fourSum([1,0,-1,0,-2,2], 0)       # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(aaa)