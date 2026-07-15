class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        adjlist = defaultdict(list)
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        def replace(word : str):
            for i in range(len(word)):
                for j in range(26):
                    if word[i] != alphabet[j]:
                        new_word = word[:i] + alphabet[j] + word[i + 1:]
                        if new_word in wordset:
                            adjlist[word].append(new_word)
        
        q = deque([beginWord])
        steps = 0
        if beginWord in wordset:
            wordset.remove(beginWord)
        while q:
            length = len(q)
            steps +=1
            for a in range(length):
                word = q.popleft()
                if word == endWord:
                    return steps
                replace(word)

                for next_word in adjlist[word]:
                    wordset.remove(next_word)
                    q.append(next_word)
        return 0

        