class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        count = [0]*(len(strs)-1)
        wrd = strs[0]
        for j in range(1, len(strs)):
            if len(wrd) > len(strs[j]):
                print('in loop1')
                for k in range(len(strs[j])):
                    if wrd[k] == strs[j][k]:
                        count[j-1] += 1
                    else:
                        break
            if len(wrd) < len(strs[j]) or len(wrd) == len(strs[j]):
                print('in loop 2')
                for k in range(len(wrd)):
                    if wrd[k] == strs[j][k]:
                        count[j-1] += 1
                    else:
                        break    
        print(count)
        if 0 in count: return ""
        return strs[0][0:min(count)]