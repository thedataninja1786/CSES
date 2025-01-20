class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root

        for l in word:
            if l not in ptr.children:
                ptr.children[l] = Node()
            ptr = ptr.children[l]
        
        ptr.end_of_word = True


    def search(self, word: str) -> bool:
        ptr = self.root
        for l in word:
            if l not in ptr.children:
                return False
            ptr = ptr.children[l]
        return ptr.end_of_word
                    
    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for l in prefix:
            if l not in ptr.children:
                return False
            ptr = ptr.children[l] 
        return True

