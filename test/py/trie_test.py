from flamebroiler import Trie

fruits = ["apple", "peach", "pear", "mango", "lemon", "lime", "applesauce", "pineapple", "kiwi", "passionfruit"]

trie = Trie()
for fruit in fruits:
    trie[fruit] = fruit

if __name__ == "__main__":
    for fruit in fruits + [fruit.upper() for fruit in fruits]:
        f = trie.get(fruit, False)
        print fruit, "YES %s" % f if f else "NO"

    print trie.suffixes("pe")