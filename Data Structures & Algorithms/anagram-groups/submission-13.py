class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i,string in enumerate(strs):
            sorted_string = str(sorted(string)) 
            if sorted_string in dic:
                temp = dic[sorted_string] 
                temp.append(string)
                dic[sorted_string] = temp
            else:
                dic[sorted_string] = [string]
 
        return list(dic.values())
            