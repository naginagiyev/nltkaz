from nltkaz.stem import Stemmer

stemmer = Stemmer(keyboard="az")
stemmed_sentence = stemmer.stem("Bu gün hava çox gözəldir. Bunu dəyərləndirməliyik!")
print(stemmed_sentence)