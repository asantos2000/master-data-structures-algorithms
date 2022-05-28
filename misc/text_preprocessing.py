import re, string, unicodedata
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import contractions
import inflect
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)

def remove_URL(sample):
    """Remove URLs from a sample string"""
    return re.sub(r"http\S+", "", sample)

def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    words = remove_stopwords(words)
    return words

def preprocess(sample):
    sample = remove_URL(sample)
    sample = replace_contractions(sample)
    # Tokenize
    words = nltk.word_tokenize(sample)

    # Normalize
    return normalize(words)


if __name__ == "__main__":
#     sample = "Blood test for Down's syndrome hailed http://bbc.in/1BO3eWQ"               
    
#     sample = remove_URL(sample)
#     sample = replace_contractions(sample)

#     # Tokenize
#     words = nltk.word_tokenize(sample)
#     print(words)

#     # Normalize
#     words = normalize(words)
#     print(words)
    
    # Import packages
    import wikipedia
    import re
    # Specify the title of the Wikipedia page
    wiki = wikipedia.page('Negras')
    # Extract the plain text content of the page
    text = wiki.content
    # Clean text
    text = re.sub(r'==.*?==+', '', text)
    text = text.replace('\n', '')
    import numpy as np
    from PIL import Image
    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    import matplotlib.pyplot as plt

    #Creating the Word Cloud
    #https://matplotlib.org/stable/gallery/color/colormap_reference.html
    stop_words = set(STOPWORDS)
    woman_mask = np.array(Image.open("worldcloud_mask3.png"))
    final_wordcloud = WordCloud(max_words=2000, mask=woman_mask, background_color ='white', colormap="Oranges", stopwords = stop_words).generate(text)
    # Displaying the WordCloud
    plt.figure(figsize = (10, 10), facecolor = None)
    plt.imshow(final_wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.savefig("worldcloud.png", format="png")
    plt.show()