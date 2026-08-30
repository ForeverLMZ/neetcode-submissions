class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        biggest = 0
        for num in nums:
            if (num - 1) in set_nums:
                continue
            end = False
            counter = 1
            while end != True:
                if counter + num not in set_nums:
                    end = True
                    if counter > biggest:
                        biggest = counter
                    counter = 1
                else:
                    counter += 1
        return biggest
