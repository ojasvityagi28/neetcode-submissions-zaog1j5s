class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {2 : "abc" , 3 : "def" , 4 : "ghi",
        5 : "jkl" , 6 : "mno" , 7 : "pqrs",
        8 : "tuv" , 9 : "wxyz" }

        res = []
        def dfs(i , comb):
            if i == len(digits):
                res.append(comb)
                return
            values = hashmap[int(digits[i])]
            for j in values:
                dfs(i + 1 , comb + j)
        dfs(0 , "")
        return res

        