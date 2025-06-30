from collections import Counter
def count_words(stroka):
    return(Counter(stroka.lower().split()))


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))