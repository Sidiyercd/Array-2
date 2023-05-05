# Time Complexity: O(n)
# Space Complexity: O(1)
class FindDisappearedNumbers(object):

    def findDisappearedNumbers(self, nums):

        if (nums == None or len(nums) == 0):
            return []

        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result
