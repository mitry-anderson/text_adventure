import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess(sentence):
    tokens = word_tokenize(sentence)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

input_sentence = "The quick brown fox jumps over the lazy dog."
preprocessed_sentence = preprocess(input_sentence)
print(preprocessed_sentence)


import nltk
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_entities(sentence):
    entities = []
    chunks = ne_chunk(pos_tag(word_tokenize(sentence)))
    for chunk in chunks:
        if hasattr(chunk, 'label'):
            entities.append((chunk.label(), ' '.join(c[0] for c in chunk)))
    return entities

input_sentence = "Apple is an American multinational technology company."
entities = extract_entities(input_sentence)
print(entities)





