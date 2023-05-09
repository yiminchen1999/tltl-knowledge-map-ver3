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

# read a file from local folder and save it as a data frame called "dictionary"
dictionary = pd.read_excel("dictionary_2.0.xlsx")
# extract keyword list from dictionary
keyword_list = dictionary["traget n-gram"].tolist()
# print(keyword_list)
#
# def keyword_sentence(file_name, number):
#     # read a txt file, extract sentences which are separated by period, exclamation point or question mark while keeping the punctuations in the sentence, remove any new line, and save sentences in a list called "sentences"
#     with open(file_name, "r") as f:
#         text = f.read().replace("\n", " ")
#     sentences = re.findall(r'\b.+?[.!?]+(?:\s|\n\n|$)', text)
#     sentence_df = pd.DataFrame({"sentence": sentences})
#     sentence_df.to_csv("Year_2022_Sentiment_Analysis/frank_2022_sentence_0" + str(number+1) + ".csv", index=False)
#
#     # find out sentences in sentences list which contain any keyword in keyword list and save those sentences in a list called "keyword_sentences"
#     keyword_sentences = []
#     for sentence in sentences:
#         for keyword in keyword_list:
#             if keyword in sentence:
#                 keyword_sentences.append(sentence)
#                 break
#
#     return keyword_sentences

# def keyword_sentence_double(file_name, number):
#     # read a txt file, extract sentences which are separated by period, exclamation point or question mark while keeping the punctuations in the sentence, remove any new line, and save sentences in a list called "sentences"
#     with open(file_name, "r") as f:
#         text = f.read().replace("\n", " ")
#     sentences = re.findall(r'\b.+?[.!?]+(?:\s|\n\n|$)', text)
#     sentence_df = pd.DataFrame({"sentence": sentences})
#     sentence_df.to_csv("Year_2022_Sentiment_Analysis/frank_2022_sentence_" + str(number) + ".csv", index=False)
#
#     # find out sentences in sentences list which contain any keyword in keyword list and save those sentences in a list called "keyword_sentences"
#     keyword_sentences = []
#     for sentence in sentences:
#         for keyword in keyword_list:
#             if keyword in sentence:
#                 keyword_sentences.append(sentence)
#                 break
#
#     return keyword_sentences

# frank_2022_01 = keyword_sentence("Year_2022_corpus/01_frank.txt")
#
classifer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")
# res = classifer(frank_2022_01)
# print(res)
# print(frank_2022_01)

# write out the res and frank_2022_01 to a csv file, each represents a column
# df = pd.DataFrame({"sentence": frank_2022_01, "sentiment": res})
# df.to_csv("frank_2022_01.csv", index=False)


# All frank projects of Year_2022_corpus
# for i in range(9):
#     frank_2022 = keyword_sentence("Year_2022_corpus/0" + str(i+1) + "_frank.txt", i)
#     res = classifer(frank_2022)
#     df = pd.DataFrame({"sentence": frank_2022, "sentiment": res})
#     df.to_csv("Year_2022_Sentiment_Analysis/frank_2022_SA_0" + str(i+1) + ".csv", index=False)
#
# for i in range(10, 13):
#     frank_2022 = keyword_sentence_double("Year_2022_corpus/" + str(i) + "_frank.txt", i)
#     res = classifer(frank_2022)
#     df = pd.DataFrame({"sentence": frank_2022, "sentiment": res})
#     df.to_csv("Year_2022_Sentiment_Analysis/frank_2022_SA_" + str(i) + ".csv", index=False)

def keyword_sentence_no_print(file_name):
    # read a txt file, extract sentences which are separated by period, exclamation point or question mark while
    # keeping the punctuations in the sentence, remove any new line, and save sentences in a list called "sentences"
    with open(file_name, "r") as f:
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


# All projects of student 1 of Year_2022_corpus
for file_name in os.listdir("Year_2022_corpus"):
    if file_name.startswith("01"):
        sentences = keyword_sentence_no_print("Year_2022_corpus/" + file_name)
        res = classifer(sentences)
        df = pd.DataFrame({"sentence": sentences, "label": [x["label"] for x in res],
                           "score": [x["score"] for x in res]})
        save_name = file_name[:-4]
        df.to_csv("Year_2022_Sentiment_Analysis/Student1_Projects/" + save_name + "_SA.csv", index=False)

# Year_2021_s1 = keyword_sentence("Year_2021_corpus_01.txt")
# Year_2021_s2 = keyword_sentence("Year_2021_corpus_02.txt")
# Year_2021_s3 = keyword_sentence("Year_2021_corpus_03.txt")
# Year_2021_s4 = keyword_sentence("Year_2021_corpus_04.txt")
# Year_2021_s5 = keyword_sentence("Year_2021_corpus_05.txt")
# Year_2021_s6 = keyword_sentence("Year_2021_corpus_06.txt")
# Year_2021_s7 = keyword_sentence("Year_2021_corpus_07.txt")