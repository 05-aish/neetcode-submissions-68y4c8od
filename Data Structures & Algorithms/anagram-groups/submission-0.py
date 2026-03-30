class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26                    #initialize an array with 26 zeroes

            for c in s:                         #for character in a string
                count[ord(c) - ord("a")] += 1     #calculate ascii, act => 1a,1c,1t

            res[tuple(count)].append(s)                #res = {[1a,1c,1t] : ['cat']}

        return list(res.values())
        
        