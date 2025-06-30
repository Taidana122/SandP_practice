def combine_anagrams(words_array):
    anagram_groups = {}
    
    for word in words_array:# пройдёт по каждому слову в массиве
        sorted_word = ''.join(sorted(word.lower()))
        
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word] 
    return list(anagram_groups.values())

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]))