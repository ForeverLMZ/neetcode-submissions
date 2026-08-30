class Solution:
    def encode(self, strs: List[str]) -> str:
        answer = ''
        for string in strs:
            answer = answer + str(len(string))+ '#' +string
        return (answer)
    def decode(self, s):
        answer = []
        index = 0
        while index < len(s):
            j = index
            while s[j] != '#':
                j += 1
            length = int(s[index:j])
            answer.append(s[j+1 : j+1+length])
            index = j + 1 + length
        return answer
