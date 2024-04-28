from typing import List, Optional
import time

# Trie node class with attributes:
# Children - to store children nodes, keyed by characters
# isFinish - to indicate if the node marks the end of a word
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.isFinish: bool = False

# Main data structure - prefix tree (trie)
class Trie:

    # Initializing Trie with an empty root node
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    # Insertion
    # Casting word to lowercase, adding following characters (if necessary)
    # to the children of the previous node, and marking the last character
    # of the word as the end of the word
    def insert(self, word: str) -> None:
        word = word.lower()
        current_node: TrieNode = self.root
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
        current_node.isFinish = True

    # Searching for the words with the given prefix
    # Casting prefix to lowercase and searching for the prefix in the trie
    def words(self, prefix: str) -> List[str]:
        prefix = prefix.lower()
        words_with_prefix: List[str] = self.words_with_prefix(prefix)
        return words_with_prefix

    # Searching for the prefix in the trie
    # Checking if the prefix in the trie exists
    # If yes, searching for all suffixes with the given prefix
    # else, returning an empty list
    def words_with_prefix(self, prefix: str, index = 0, current_node: Optional[TrieNode] = None) -> List[str]:
        if current_node is None:
            current_node = self.root
        if index == len(prefix):
            return ["".join((prefix,word)) for word in self.collect_suffixes(current_node)]
        else:
            first_char = prefix[index]
            if first_char in current_node.children:
                return self.words_with_prefix(prefix, index + 1,  current_node.children[first_char])
            else:
                return []

    # Appending all suffixes from the given node
    def collect_suffixes(self, current_node: TrieNode, prefix: str = "") -> List[str]:
        words: List[str] = []
        if current_node.isFinish:
            words.append(prefix)
        for char, node in current_node.children.items():
            words.extend(self.collect_suffixes(node, "".join((prefix,char))))
        return words