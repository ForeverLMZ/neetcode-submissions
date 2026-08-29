class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = {}
        for num in nums:
            if num in keys:
                keys[num] += 1
            else:
                keys[num] = 1
            
        sorted_keys = sorted(keys,key = lambda x: keys[x], reverse = True)  
        return sorted_keys[:k]


