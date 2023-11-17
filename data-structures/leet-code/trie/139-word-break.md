
## Word break
- Ref: https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150

### Approach
- trie
- This is partial solution.

```py
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.wordCount = 0


def insertWord(root, word):
    currentNode = root

    for c in word:
        if currentNode.children[ord(c)-ord("a")] is None:
            newNode = TrieNode()
            currentNode.children[ord(c)-ord("a")] = newNode

        currentNode = currentNode.children[ord(c)-ord("a")]
    currentNode.wordCount += 1


def findWord(root, word):
    currentNode = root

    for c in word:
        if currentNode.children[ord(c) - ord("a")] is None:
            return False
        currentNode = currentNode.children[ord(c) - ord("a")]

    if currentNode.wordCount == 1:
        return True
    return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = TrieNode()
        for word in wordDict:
            insertWord(trie, word)

        word = ""
        for c in s:
            word = word + c
            if findWord(trie, word):
                word = ""

        if word == "":
            return True
        return False


# trie = TrieNode()
# insertWord(trie, "ankit")
# print(findWord(trie,"ankit"))
# print(findWord(trie,"ank"))
# print(findWord(trie,"anka"))
sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))
print(sol.wordBreak("applepenapple", ["apple","pen"]))
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

# expected true
print(sol.wordBreak("aaaaaaa", ["aaaa", "aaa"]))

```