from typing import List, Optional
import time

class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.isFinish: bool = False


class Trie:

    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        word = word.lower()
        current_node: TrieNode = self.root
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode()
            current_node = current_node.children[character]
        current_node.isFinish = True

    def words(self, prefix: str) -> List[str]:
        prefix = prefix.lower()
        words_with_prefix: List[str] = self.words_with_prefix(prefix)
        return words_with_prefix

    def words_with_prefix(self, prefix: str, index = 0, current_node: Optional[TrieNode] = None) -> List[str]:
        if current_node is None:
            current_node = self.root
        if index == len(prefix):
            return [f'{prefix}{word}' for word in self.collect_suffixes(current_node)]
        else:
            first_char = prefix[index]
            if first_char in current_node.children:
                return self.words_with_prefix(prefix, index + 1,  current_node.children[first_char])
            else:
                return []

    def collect_suffixes(self, current_node: TrieNode, prefix: str = "") -> List[str]:
        words: List[str] = []
        if current_node.isFinish:
            words.append(prefix)
        for char, node in current_node.children.items():
            words.extend(self.collect_suffixes(node, f'{prefix}{char}'))
        return words