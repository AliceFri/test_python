"""
Tire树，

查询是否出现过该字符串， 出现过几次
查询有多少个字符串 以 某某字符串为前缀
"""


class TrieNode:
    def __init__(self):
        self.pas = 0
        self.end = 0
        self.next = {}  # "a": TrieNode


class TireTree:
    def __init__(self):
        self.startNode = TrieNode()
        self.nullword = 0

    def insert(self, word):
        if not word:
            self.nullword += 1
            return
        node = self.startNode
        node.pas += 1
        for w in word:
            if w not in node.next:
                node.next[w] = TrieNode()
            node.next[w].pas += 1
            node = node.next[w]
        node.end += 1

    def search(self, word):
        """
        搜索出现了几次, 前缀几次
        """
        if not word:
            return self.nullword, self.nullword
        node = self.startNode
        for w in word:
            if w not in node.next:
                return 0, 0
            node = node.next[w]
        return node.end, node.pas

    def delete(self, word):
        """
        删除 word
        """
        if not word:
            self.nullword = max(0, self.nullword - 1)
            return
        # 先检测在不在
        iexist, ipre = self.search(word)
        if not iexist:
            return
        node = self.startNode
        node.pas -= 1
        for w in word:
            node.next[w].pas -= 1
            if node.next[w].pas == 0:
                del node.next[w]
                return
            node = node.next[w]
        node.end -= 1


if __name__ == "__main__":
    t = TireTree()
    t.insert("aab")
    t.insert("a")
    print(t.search("a"))
    t.delete("aab")
    print(t.search("a"))
    t.delete("a")
    print(t.search("a"))
