from typing import List, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.isFinish: bool = False


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        word = word.lower()
        current_char: TrieNode = self.root
        for c in word:
            if c not in current_char.children:
                current_char.children[c] = TrieNode()
            current_char = current_char.children[c]
        current_char.isFinish = True

    def words(self, prefix: str) -> List[str]:
        prefix = prefix.lower()
        words_with_prefix: List[str] = self.words_with_prefix(prefix)
        return [prefix + word for word in words_with_prefix]

    def words_with_prefix(self, prefix: str, current_char: Optional[TrieNode] = None) -> List[str]:
        if current_char is None:
            current_char = self.root
        if len(prefix) == 0:
            return self.collect_suffixes(current_char)
        else:
            first_char = prefix[0]
            if first_char in current_char.children:
                return self.words_with_prefix(prefix[1:], current_char.children[first_char])
            else:
                return []

    def collect_suffixes(self, current_char: TrieNode, prefix: str = "") -> List[str]:
        words: List[str] = []
        if current_char.isFinish:
            words.append(prefix)
        for char, node in current_char.children.items():
            words.extend(self.collect_suffixes(node, prefix + char))
        return words


if __name__ == '__main__':
    trie: Trie = Trie()
    words: List[str] = ["apple", "banana", "app", "ape", "bat"]
    for word in words:
        trie.insert(word)

    prefix: str = "app"
    print("Słowa z prefixem '{}':".format(prefix))
    print(trie.words(prefix))
