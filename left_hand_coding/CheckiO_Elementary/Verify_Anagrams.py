### Verify_Anagrams



def verify_anagrams(words1, words2):
    words1 = sorted(words1.lower().replace(' ', ''))
    words2 = sorted(words2.lower().replace(' ', ''))

    return words1 == words2


verify_anagrams('tokyo', 'kyoto')
verify_anagrams('AOX', 'xoa')
verify_anagrams('tasdf', 'kasdfo')