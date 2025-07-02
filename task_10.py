from collections import Counter
import string
def count_words(stroka):
    tecnodancer=stroka.translate(str.maketrans("", "", string.punctuation))
    lalalalululu= Counter(tecnodancer.lower().split())
    return dict(lalalalululu)
