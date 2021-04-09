# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变
# 化后可能得到：
#
#  若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
#  若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
#
#
#  注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2],
# ..., a[n-2]] 。
#
#  给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,3,5]
# 输出：1
#
#
#  示例 2：
#
#
# 输入：nums = [2,2,2,0,1]
# 输出：0
#
#
#
#
#  提示：
#
#
#  n == nums.length
#  1 <= n <= 5000
#  -5000 <= nums[i] <= 5000
#  nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
#
#
#
#
#  进阶：
#
#
#  这道题是 寻找旋转排序数组中的最小值 的延伸题目。
#  允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
#
#  Related Topics 数组 二分查找
#  👍 338 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 暴力解法
        return min(nums)

        '''
        1. 旋转排序后的数组可以拆分两个部分nums1,nums2,并且nums1里面的任意一个元素>=nums2里面的任意一个元素；所以考虑二分法
        2. left,right指针在数组两端，mid为二分的中点(向下取整)
            2.1 当nums[mid] > nums[right]时，left=mid+1
            2.2 nums[mid] < nums[right] 时, right=mid
            2.3 当 nums[mid] == nums[right] 时, 难区分mid的位置。
                如[1,0,1,1,1] 和 [1,1,1,0,1] ，在 left = 0, right = 4, mid = 2 时，无法判断 mid 在哪个排序数组中
                采用right=right-1解决问题
                此操作不会使最小值丢失：假设 nums[right] 是最小值，有两种情况：
                若 nums[right] 是唯一最小值：那就不可能满足判断条件 nums[mid] == nums[right]，因为 mid < right（left != right 且 mid = (left + right) // 2 向下取整）；
                若 nums[right] 不是唯一最小值，由于 mid < right 而 nums[mid] == nums[right]，即还有最小值存在于 [left,right−1] 区间，因此不会丢失最小值。
        '''
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1
        return numbers[left]
# leetcode submit region end(Prohibit modification and deletion)
