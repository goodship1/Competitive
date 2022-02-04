class Node:
    def __init__(self, char):
        self.is_word = False
        self.char = char
        self.children = {}

class Trie:

    def __init__(self):
        self.root = Node('')
        

    def insert(self, word: str) -> None:
        temp = self.root
        for char in word:
            if char not in temp.children:
                temp.children[char] = Node(char)
            temp = temp.children[char]
        temp.is_word = True

    def search(self, word: str) -> bool:
        temp = self.root
        for char in word:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return temp.is_word
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for char in prefix:
            if char not in temp.children:
                return False
            temp = temp.children[char]
        return True
