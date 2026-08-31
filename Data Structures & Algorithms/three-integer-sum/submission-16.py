class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        n = len(nums)

        for i in range(n):
            first_num = nums[i]
            if first_num > 0:
                break

            if i > 0 and first_num == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            target = 0 - first_num

            while left < right:
                total = nums[left] + nums[right]

                if total == target:
                    answer.append([first_num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return answer