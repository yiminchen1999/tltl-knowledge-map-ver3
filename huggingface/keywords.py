# import libraries
import pandas as pd
import os
from transformers import pipeline
import re

# # combine txt files that start with "01" in the folder "Year_2021_corpus" into one txt file called "Year_2021_corpus_01.txt" and so on.
# for i in range(7):
#     with open("Year_2021_corpus_0" + str(i+1) + ".txt", "w") as f:
#         for file_name in os.listdir("Year_2021_corpus"):
#             if file_name.startswith("0"+str(i+1)):
#                 with open("Year_2021_corpus/" + file_name, "r") as f1:
#                     f.write(f1.read())
#data1 = pd.read_excel("assets/frank_2022_SA_01_combined.xlsx",engine='openpyxl')
# read a file from local folder and save it as a data frame called "dictionary"
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
file_names1 = ['dream1_SA', 'dream2_SA', 'frank_SA', 'lofi_SA', 'omni_SA', 'remix_SA', 'testing_SA', 'tool_SA']
# Create an empty list to store all the DataFrames
dfs = []
# All projects of student 1 of Year_2023_corpus
for file_name in os.listdir("/Users/chenyimin/PycharmProjects/tltl-knowledge-map-ver3/assets/Year2023text"):
    if file_name.startswith("12"):
        sentences = keyword_sentence_no_print("/Users/chenyimin/PycharmProjects/tltl-knowledge-map-ver3/assets/Year2023text/" + file_name)
        res = classifer(sentences)
        df = pd.DataFrame({"sentence": sentences, "label": [x["label"] for x in res],
                           "score": [x["score"] for x in res]})
        df['Name'] = file_name[3:-4]
        dfs.append(df)
        save_name = file_name[1:-4]
        df.to_excel("/Users/chenyimin/PycharmProjects/tltl-knowledge-map-ver3/assets/Year2023text/Student12_Projects/" + save_name + "_SA.xlsx", index=False)

# Concatenate all the DataFrames into a single DataFrame
combined_df = pd.concat(dfs)
# Write the combined DataFrame to a new Excel file
combined_df.to_excel('/Users/chenyimin/PycharmProjects/tltl-knowledge-map-ver3/assets/Year2023text/Student12_Projects/2023_student12_8projects_combined.xlsx', index=False)

# Year_2021_s1 = keyword_sentence("Year_2021_corpus_01.txt")
# Year_2021_s2 = keyword_sentence("Year_2021_corpus_02.txt")
# Year_2021_s3 = keyword_sentence("Year_2021_corpus_03.txt")
# Year_2021_s4 = keyword_sentence("Year_2021_corpus_04.txt")
# Year_2021_s5 = keyword_sentence("Year_2021_corpus_05.txt")
# Year_2021_s6 = keyword_sentence("Year_2021_corpus_06.txt")
# Year_2021_s7 = keyword_sentence("Year_2021_corpus_07.txt")