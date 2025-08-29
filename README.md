![NLTKaz Banner](https://i.imgur.com/JecGkI0.png)

# NLTKAZ 📚

**NLTKAZ** is a natural language processing toolkit designed for the Azerbaijani language making it easier to preprocess Azerbaijani text for NLP tasks.

## Installation ⬇️
```bash
pip install nltkaz
```

## Features 🧩
Currently provided features:
- **Stemming**: Reduce words to their root forms.
- **Stopword Removal**: Easily remove common Azerbaijani stopwords from text.
- **Tokenization**: Tokenize text into words, sentences, or tweets.

## Usage ⚙️
### Stemming
```python
from nltkaz import Stemmer

# Initialize stemmer with the appropriate keyboard type
# Use 'az' for Azerbaijani text or 'en' if the text is typed using an English keyboard
stemmer = Stemmer(keyboard="az")

# Stem your string
stemmed_string = stemmer.stem("your_string")
```

### Stopword Removal
```python
from nltkaz import load, remove

# Load stopwords
stopwords = load()

# Remove stopwords from the given string
result = remove(stopwords=stopwords, sentence="your_string")
```

### Tokenization

#### Word Tokenizer
```python
from nltkaz import wordTokenize

words = wordTokenize("your_string")
```

#### Sentence Tokenizer
```python
from nltkaz import sentenceTokenize

sentences = sentenceTokenize("your_string")
```

#### Tweet Tokenizer
```python
from nltkaz import tweetTokenize

tweets = tweetTokenize("your_string")
```

## Author 🧑‍💻
- **Nagi Nagiyev**  

## Contact 📧
Gmail: nagiyevnagi01@gmail.com.

Linkedin: https://www.linkedin.com/in/naginagiyev/

## License 📜
MIT License

---

> This project is in early development. Contributions and feedback are welcome! 🤝