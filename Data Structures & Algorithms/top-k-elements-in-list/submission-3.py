class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap= defaultdict(int)
        for c in nums:
            hashmap[c]+=1

        sorted_frequencies= sorted(hashmap.items(),key=lambda x:x[1],reverse=True)

        item=[item[0] for item in sorted_frequencies[:k]]
        return item
        
            

        