import unittest
from Trie import Trie

class TestTrie(unittest.TestCase):

    def test_empty_tree(self):
        trie = Trie()
        self.assertEqual(sorted(trie.words_with_prefix("")), [])
        self.assertEqual(sorted(trie.words_with_prefix("a")), [])
        self.assertEqual(sorted(trie.words_with_prefix("app")), [])


    def test_words_with_prefix(self):
        trie = Trie()

        words = ["app", "apple", "ban", "banana"]

        for word in words:
            trie.insert(word)

        self.assertEqual(sorted(trie.words_with_prefix("")), ["app", "apple", "ban", "banana"])

        self.assertEqual(sorted(trie.words_with_prefix("a")), ["app", "apple"])
        self.assertEqual(sorted(trie.words_with_prefix("A")), ["app", "apple"])

        self.assertEqual(sorted(trie.words_with_prefix("ApP")), ["app", "apple"])
        self.assertEqual(sorted(trie.words_with_prefix("app")), ["app", "apple"])

        self.assertEqual(sorted(trie.words_with_prefix("apple")), ["apple"])
        self.assertEqual(sorted(trie.words_with_prefix("apples")), [])

        self.assertEqual(sorted(trie.words_with_prefix("BA")), ["ban", "banana"])
        self.assertEqual(sorted(trie.words_with_prefix("bAnANa")), ["banana"])

        words = ["a", "appbanana", "bananaapp"]

        for word in words:
            trie.insert(word)

        self.assertEqual(sorted(trie.words_with_prefix("a")), ["a", "app", "appbanana", "apple"])
        self.assertEqual(sorted(trie.words_with_prefix("app")), ["app", "appbanana", "apple"])
        self.assertEqual(sorted(trie.words_with_prefix("banana")), ["banana", "bananaapp"])


    def test_words_with_unified_prefix(self):
        trie = Trie()

        words = ["app", "apple", "ban", "banana"]

        for word in words:
            trie.insert(word)

        self.assertEqual(sorted(trie.words_with_unified_prefix("")), ["app", "apple", "ban", "banana"])

        self.assertEqual(sorted(trie.words_with_unified_prefix("a")), ["app", "apple"])
        self.assertNotEqual(sorted(trie.words_with_unified_prefix("A")), ["app", "apple"])

        self.assertNotEqual(sorted(trie.words_with_unified_prefix("ApP")), ["app", "apple"])
        self.assertEqual(sorted(trie.words_with_unified_prefix("app")), ["app", "apple"])

        self.assertEqual(sorted(trie.words_with_unified_prefix("apple")), ["apple"])
        self.assertEqual(sorted(trie.words_with_unified_prefix("apples")), [])

        self.assertEqual(sorted(trie.words_with_unified_prefix("ba")), ["ban", "banana"])
        self.assertNotEqual(sorted(trie.words_with_unified_prefix("bAnANa")), ["banana"])

        words = ["a", "appbanana", "bananaapp"]

        for word in words:
            trie.insert(word)

        self.assertEqual(sorted(trie.words_with_unified_prefix("a")), ["a", "app", "appbanana", "apple"])
        self.assertEqual(sorted(trie.words_with_unified_prefix("app")), ["app", "appbanana", "apple"])
        self.assertEqual(sorted(trie.words_with_unified_prefix("banana")), ["banana", "bananaapp"])

    def test_collect_suffixes(self):
        trie = Trie()

        words = ["a", "app", "apple", "ban", "banana"]

        for word in words:
            trie.insert(word)

        current_node = trie.root
        #Now, we have prefix "" (prefix of every word)

        self.assertEqual(trie.collect_suffixes(current_node), ["a", "app", "apple", "ban", "banana"])

        current_node = current_node.children['a']
        #Now, we have prefix "a"

        self.assertEqual(trie.collect_suffixes(current_node), ["", "pp", "pple"])

        current_node = current_node.children['p']
        current_node = current_node.children['p']
        #Now, we have prefix "app"

        self.assertEqual(trie.collect_suffixes(current_node), ["", "le"])

        current_node = current_node.children['l']
        #Now, we have prefix "appl"

        self.assertEqual(trie.collect_suffixes(current_node), ["e"])

        current_node = current_node.children['e']
        #Now, we have prefix "apple"

        self.assertEqual(trie.collect_suffixes(current_node), [""])

    def test_example_cases(self):
        trie = Trie()

        trie.insert("car")
        trie.insert("carpet")
        trie.insert("java")
        trie.insert("javascript")
        trie.insert("internet")

        self.assertEqual(sorted(trie.words_with_prefix("c")), ["car", "carpet"])
        self.assertEqual(sorted(trie.words_with_prefix("car")), ["car", "carpet"])
        self.assertEqual(sorted(trie.words_with_prefix("carp")), ["carpet"])
        self.assertEqual(sorted(trie.words_with_prefix("jav")), ["java", "javascript"])
        self.assertEqual(sorted(trie.words_with_prefix("intern")), ["internet"])
        self.assertEqual(sorted(trie.words_with_prefix("foo")), [])

if __name__ == '__main__':
    unittest.main()
