import os
from gensim import corpora, models
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# Path to the folder containing the text files
#folder_path = 'assets/Year2023text/original'
folder_path ='assets/Year2023text/original/12_tool.txt'
# Read text data from files in the folder
documents = []
for filename in os.listdir(folder_path):
    with open(os.path.join(folder_path, filename), 'r') as file:
        documents.append(file.read())

# Tokenize the documents
stop_words = stopwords.words('english')
tokenized_docs = [[token for token in doc.lower().split() if token not in stop_words]
                  for doc in documents]

# Create a dictionary from the tokenized documents
dictionary = corpora.Dictionary(tokenized_docs)

# Create a corpus from the tokenized documents
corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]

# Perform LDA topic modeling
num_topics = 5  # Number of topics to extract
lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)

# Print the topics and their associated words
for topic_num in range(num_topics):
    topic_words = lda_model.show_topic(topic_num)
    print(f"Topic #{topic_num+1}:")
    print([word for word, _ in topic_words])
    print()
