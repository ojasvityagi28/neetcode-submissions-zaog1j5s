class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        t = total // k
        nums.sort(reverse=True)                  
        if nums[0] > t:
            return False
        buckets = [0] * k                        

        def bt(i):                               
            if i == len(nums):
                return True                      
            seen = set()
            for b in range(k):
                if buckets[b] + nums[i] > t:     
                    continue
                if buckets[b] in seen:           
                    continue
                seen.add(buckets[b])
                buckets[b] += nums[i]            
                if bt(i + 1):
                    return True
                buckets[b] -= nums[i]            
            return False                         

        return bt(0)





# class Solution:
#     def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
#         total = sum(nums)
#         subset_sum = total//k
#         dp = {}
#         used = set()
#         if total % k != 0: 
#             return False

#         def dfs(curr_sum, k):

#             if k == 0:
#                 return True
            
#             key = frozenset(used)
#             if key in dp:
#                 return dp[key]

#             dp[key] = False

#             for j in range(len(nums)):
#                 if j in used:
#                     continue
#                 else:
#                     used.add(j)
#                     if curr_sum + nums[j] < subset_sum:
#                         if dfs(curr_sum + nums[j], k):
#                             dp[key] = True

#                     elif curr_sum + nums[j] == subset_sum:
#                         if dfs(0 , k - 1):
#                             dp[key] = True

#                     used.remove(j)
#                     if dp[key]:
#                         return True

            
#             return dp[key]
        
#         return dfs(0 , k)




        