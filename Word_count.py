def word_count(sentence, N):

    sentence = sentence.lower()

    punctuations = ".,!?;:'\"()[]{}"
    for ch in punctuations:
        sentence = sentence.replace(ch, '')   

    words = sentence.split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    top_N = dict(sorted_words[:N])
    others = dict(sorted_words[N:])

    return top_N, others

top, others = word_count("Hello hello! How are you? You look well.", 2)
print(top)
print(others)





































