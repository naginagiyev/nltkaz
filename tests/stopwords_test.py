from nltkaz.stopwords import load, remove

stopwords = load()
sentence = "Bu gün hava çox gözəldir. Bunu dəyərləndirməliyik ki, ən azından bir günümüz yaxşı keçsin!"

result = remove(stopwords=stopwords, sentence=sentence)
print(result)