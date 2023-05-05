# Time Complexity : O(n)
# Space Complexity: O(1)
class MinAndMax(object):

    def minAndMax(self, nums):

        if (nums == None or len(nums) == 0):
            return [-1, -1]

        oddLength = 0
        if len(nums) / 2 != 0:
            oddLength = 1

        finalMax = float('-inf')
        finalMin = float('inf')

        for i in range(0, len(nums) - 1, 2):
            if nums[i+1] > nums[i]:
                currentMax = nums[i+1]
                currentMin = nums[i]
            else:
                currentMax = nums[i]
                currentMin = nums[i + 1]

            if currentMax > finalMax:
                finalMax = currentMax
            if currentMin < finalMin:
                finalMin = currentMin

        if (oddLength):
            if nums[len(nums) - 1] > finalMax:
                finalMax = nums[len(nums) - 1]
            if nums[len(nums) - 1] < finalMin:
                finalMin = nums[len(nums) - 1]

        return [finalMin, finalMax]
