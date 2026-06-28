class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        opening = []
        for i,p in enumerate(s):
            if p == "(":
                opening.append(i)
            elif p == "*":
                star.append(i)
            else:
                if not opening and not star:
                    return False
                if opening:
                    opening.pop()
                elif star:
                    star.pop()
        while star and opening:
            if opening[-1] < star[-1]:
                opening.pop()
                star.pop()
            else:
                return False
        return not opening

        