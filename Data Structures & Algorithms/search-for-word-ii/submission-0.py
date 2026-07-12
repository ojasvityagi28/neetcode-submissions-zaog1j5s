class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False

    def add_word(self, word):
        for c in word:
            if c not in self.children:
                self.children[c] = TrieNode()
            self = self.children[c]
        self.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.add_word(word)
        rows , cols = len(board) , len(board[0])
        res = []
        visited = set()

        def dfs(r , c , node , word):
            if (r < 0 or r >= rows 
                or c < 0 or c >= cols
                or (r,c) in visited  
                or board[r][c] not in node.children
            ):
                return 
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.append(word)
                node.isWord = False
            
            dfs(r + 1 , c , node , word)
            dfs(r - 1 , c , node , word)
            dfs(r , c + 1 , node , word)
            dfs(r , c - 1 , node , word)

            visited.remove((r,c))
        
        for r in range(rows):
            if len(res) == len(words):
                return res
            for c in range(cols):
                dfs(r , c , root , "")
        return res
        
        