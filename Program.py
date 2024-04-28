from Trie import Trie

trie: Trie = Trie()

def insert_list(word_list):
    for word in word_list:
        insert(word)

def insert(word):
    trie.insert(word)

def get_words_with_prefix(prefix):
    return trie.words(prefix)

if __name__ == "__main__":

    #Here insert words to the dictionary, f.e:

    insert("car")
    insert("carpet")
    insert("java")
    insert("javascript")
    insert("internet")

    #or

    insert_list(["car", "carpet", "java", "javascript", "internet"])

    #Here check a list of the autocopleted words with given prefix, f.e:

    print(get_words_with_prefix("c"))
    print(get_words_with_prefix("car"))
    print(get_words_with_prefix("carp"))
    print(get_words_with_prefix("jav"))
    print(get_words_with_prefix("intern"))
    print(get_words_with_prefix("foo"))