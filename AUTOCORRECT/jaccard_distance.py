# https://stackoverflow.com/questions/46975929/how-can-i-calculate-the-jaccard-similarity-of-two-lists-containing-strings-in-py

def jaccard_distance(a, b):
    """dice coefficient 2nt/(na + nb)."""
    if not len(a) or not len(b): return 0.0
    if len(a) == 1:  a = a + u'.'
    if len(b) == 1:  b = b + u'.'

    a_bigram_list = []
    for i in range(len(a) - 1):
        a_bigram_list.append(a[i:i + 2])
    b_bigram_list = []
    for i in range(len(b) - 1):
        b_bigram_list.append(b[i:i + 2])

    a_bigrams = set(a_bigram_list)
    b_bigrams = set(b_bigram_list)
    c = a_bigrams.intersection(b_bigrams)

    jaccard_index = float(len(c)) /(len(a_bigrams) + len(b_bigrams) - len(c))
    return 1-jaccard_index





