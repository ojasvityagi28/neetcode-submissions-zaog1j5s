class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap = Counter(hand)
        length = 0
        hand.sort()
        for a in hand:
            if a - 1 not in hashmap or hashmap[a - 1] == 0:
                n = a
                size = 0
                while n in hashmap and hashmap[n] > 0 and size < groupSize:
                    hashmap[n] -= 1
                    n += 1
                    size += 1
                if size  % groupSize != 0:
                    return False
        for key in hashmap:
            if hashmap[key] != 0:
                return False
        return True
        
        
        