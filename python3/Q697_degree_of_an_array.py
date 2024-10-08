#
# Difficulty Level: EASY
#
# Given a non-empty array of non-negative integers nums, the degree of this array is
# defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums,
# that has the same degree as nums.
#

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_count = Counter(nums)

        # Find the highest occurence in nums list
        max_count = max(num_count.values())
        if max_count == 1:
            return 1
        
        m = len(nums)
        sub = []

        # Add numbers in sub list which has the highest occurence in nums list
        for num, count in num_count.items():
            if count == max_count:
                sub.append(num)
        
        # Find the longest subarray for each number in sub list
        for i in range(len(sub)):
            target = sub[i]
            start, end = 0, 0
            
            # Find the index of the first occurence of current number in nums list
            for j in range(m):
                if nums[j] == target:
                    start = j
                    break

            # Find the index of the last occurence of current number in nums list
            for j in range(m-1, -1, -1):
                if nums[j] == target:
                    end = j
                    break

            # Add the subarray length in sub list
            sub[i] = (end - start) + 1

        # Return the smallest subarray length in sub list
        return min(sub)