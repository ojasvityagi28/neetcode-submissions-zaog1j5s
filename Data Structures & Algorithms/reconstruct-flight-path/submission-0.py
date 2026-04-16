class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjlist = { src : [] for src, dest in tickets}
        tickets.sort(reverse = True)

        for src, dest in tickets:
            adjlist[src].append(dest)

        res = []
        def dfs(src):
            while src in adjlist and adjlist[src]:
                dest = adjlist[src].pop()
                dfs(dest)
            res.append(src)

        dfs("JFK")
        return res[::-1]
