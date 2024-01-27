#15
import nltk
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    V -> "saw" [1.0]
    P -> "with" [1.0]
    NP -> N [0.4] | Det N [0.3] | NP PP [0.3]
    N -> "John" [0.4] | "Mary" [0.4] | "telescope" [0.2]
    Det -> "a" [1.0]
""")
parser = nltk.ViterbiParser(grammar)

sentence = "John saw Mary with a telescope".split()

trees = list(parser.parse(sentence))

trees.sort(key=lambda tree: -tree.prob())

for tree in trees:
    print(tree)
