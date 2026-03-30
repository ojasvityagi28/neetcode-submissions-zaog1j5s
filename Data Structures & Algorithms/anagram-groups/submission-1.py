class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary=defaultdict(list)
        for word in strs:
            sorted_str=''.join(sorted(word))
            dictionary[sorted_str].append(word)
        return list(dictionary.values())


        
        
        