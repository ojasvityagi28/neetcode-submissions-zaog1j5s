class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n , 0)
        
        list1 = [[] for i in range(len(nums) + 1)]

        for n in count:
            index = count[n]
            list1[index].append(n)

        res = []

        for i in range(len(list1) - 1 , 0 , -1):
            for num in list1[i]:
                res.append(num)
                if len(res) == k:
                    return res
    
        



        