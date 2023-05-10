
import pandas as pd
import os
from transformers import pipeline
import re

dictionary = pd.read_excel("/Users/chenyimin/PycharmProjects/tltl-knowledge-map-ver3/assets/dictionaryfinal.xlsx",engine='openpyxl')
# extract keyword list from dictionary
keyword_list = dictionary["display concept"].tolist()
#
classifer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")




def keyword_sentence_no_print(file_name):
    # read a txt file, extract sentences which are separated by period, exclamation point or question mark while
    # keeping the punctuations in the sentence, remove any new line, and save sentences in a list called "sentences"
    with open(file_name, "r", encoding='iso-8859-1') as f:
        text = f.read().replace("\n", " ")
    sentences = re.findall(r'\b.+?[.!?]+(?:\s|\n\n|$)', text)
    sentence_df = pd.DataFrame({"sentence": sentences})

    # find out sentences in sentences list which contain any keyword in keyword list and save those sentences in a
    # list called "keyword_sentences"
    keyword_sentences = []
    for sentence in sentences:
        for keyword in keyword_list:
            if keyword in sentence:
                keyword_sentences.append(sentence)
                break

    return keyword_sentences

# Define a list of filenames without extension
file_names1 = ['frank_SA', 'omni_SA', 'remix_SA', 'rube_SA', 'dream1_SA', 'dream2_SA','dream3_SA', 'lofi_SA','tool_SA']
# Create an empty list to store all the DataFrames
dfs = []
# All projects of student 1 of Year_2023_corpus
for file_name in os.listdir("/Users/chenyimin/PycharmProjects/tltl-knowledge-map-ver3/assets/Year2023text"):
    if "tool" in file_name:
        sentences = keyword_sentence_no_print("/Users/chenyimin/PycharmProjects/tltl-knowledge-map-ver3/assets/Year2023text/" + file_name)
        res = classifer(sentences)
        df = pd.DataFrame({"sentence": sentences, "label": [x["label"] for x in res],
                           "score": [x["score"] for x in res]})
        df['student number'] = file_name[:2]
        dfs.append(df)
        save_name = file_name[:2]
        df.to_excel("/Users/chenyimin/PycharmProjects/tltl-knowledge-map-ver3/assets/Year2023text/tool_" + save_name + "_SA.xlsx", index=False)

# Concatenate all the DataFrames into a single DataFrame
combined_df = pd.concat(dfs)
# Write the combined DataFrame to a new Excel file
combined_df.to_excel('/Users/chenyimin/PycharmProjects/tltl-knowledge-map-ver3/assets/Year2023text/combined/2023_student_9.xlsx', index=False)
