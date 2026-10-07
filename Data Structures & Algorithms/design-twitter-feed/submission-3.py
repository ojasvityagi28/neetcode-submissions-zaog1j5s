class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet_map = {}
        self.follow_map = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet_map:
            self.tweet_map[userId] = []
        self.tweet_map[userId].append([self.time , tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        res = []

        following = self.follow_map.get(userId, set())
        following.add(userId)

        for followingId in following:
            if followingId not in self.tweet_map:
                continue
            # get all the last tweets
            index = len(self.tweet_map[followingId]) - 1
            time , tweet_id = self.tweet_map[followingId][index]
            max_heap.append([time, tweet_id, followingId , index])

        heapq.heapify_max(max_heap)

        while max_heap and len(res) < 10:
            time, tweet_id, followingId , index =heapq.heappop_max(max_heap)
            res.append(tweet_id)

            if index - 1 >= 0:
                time , tweet_id = self.tweet_map[followingId][index - 1]
                heapq.heappush_max(max_heap ,[time, tweet_id, followingId , index - 1] )
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            self.follow_map[followerId] = set()
        self.follow_map[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            return None
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
