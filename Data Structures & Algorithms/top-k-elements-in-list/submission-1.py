class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}                                   #count of occurence : no. that occurs
                                                     # 3 : [1,2] means 1 and 2 appear 3 times each
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:         
            count[i] = count.get(i, 0) + 1
        for n, c in count.items():                   #for number and count of number
            freq[c].append(n)                        #3 : [] -> 3 : [2]

        res = []
        for i in range(len(freq) -1, 0, -1):         #iterate right to left
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res

            