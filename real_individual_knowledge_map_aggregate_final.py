# -*- coding: utf-8 -*-
"""Real_Individual_Knowledge_Map_Aggregate_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RtzzOvwymvKIC-sALaEHR4oSp_jD364N
"""

from pyvis.network import Network
import pandas as pd
import numpy as np

# Color categories: First three weeks, Middle three weeks, Last two weeks
palette_2021 = [['#e3342f', '#e3342f', '#e3342f', '#f7806f', '#f7806f', '#f7806f', '#ffB99f', '#ffB99f'],
             ['#f6993f', '#f6993f', '#f6993f', '#fac97f', '#fac97f', '#fac97f', '#fdec6f', '#fdec6f'],
             ['#ffed4a', '#ffed4a','#ffed4a','#fff88a', '#fff88a','#fff88a','#ffffba', '#ffffba'],
             ['#38c172', '#38c172', '#38c172', '#7dd2b2', '#7dd2b2', '#7dd2b2', '#b3dee2', '#b3dee2'],
             ['#4dc0b5', '#4dc0b5', '#4dc0b5', '#91d0d9', '#91d0d9', '#91d0d9', '#c4dcf4', '#c4dcf4'],
             ['#3490dc', '#3490dc', '#3490dc', '#89a8ec', '#89a8ec', '#89a8ec', '#c8c0f8', '#c8c0f8'],
             ['#6574cd', '#6574cd', '#6574cd', '#95a4f1', '#95a4f1', '#95a4f1', '#b9bcff', '#b9bcff'],
             ['#9561e2', '#9561e2', '#9561e2', '#bd91fa', '#bd91fa', '#bd91fa', '#dbb5ff', '#dbb5ff'],
             ['#f66d9b', '#f66d9b', '#f66d9b', '#fa9dbb', '#fa9dbb', '#fa9dbb', '#fdc1d3', '#fdc1d3']]

# Color categories: First three weeks, Middle three weeks, Last four weeks
palette_2022 = [['#e3342f', '#e3342f', '#e3342f', '#f7806f', '#f7806f', '#f7806f', '#ffB99f', '#ffB99f', '#ffB99f', '#ffB99f'],
             ['#f6993f', '#f6993f', '#f6993f', '#fac97f', '#fac97f', '#fac97f', '#fdec6f', '#fdec6f', '#fdec6f', '#fdec6f'],
             ['#ffed4a', '#ffed4a','#ffed4a','#fff88a', '#fff88a','#fff88a','#ffffba', '#ffffba', '#ffffba', '#ffffba'],
             ['#38c172', '#38c172', '#38c172', '#7dd2b2', '#7dd2b2', '#7dd2b2', '#b3dee2', '#b3dee2', '#b3dee2', '#b3dee2'],
             ['#4dc0b5', '#4dc0b5', '#4dc0b5', '#91d0d9', '#91d0d9', '#91d0d9', '#c4dcf4', '#c4dcf4', '#c4dcf4', '#c4dcf4'],
             ['#3490dc', '#3490dc', '#3490dc', '#89a8ec', '#89a8ec', '#89a8ec', '#c8c0f8', '#c8c0f8', '#c8c0f8', '#c8c0f8'],
             ['#6574cd', '#6574cd', '#6574cd', '#95a4f1', '#95a4f1', '#95a4f1', '#b9bcff', '#b9bcff', '#b9bcff', '#b9bcff'],
             ['#9561e2', '#9561e2', '#9561e2', '#bd91fa', '#bd91fa', '#bd91fa', '#dbb5ff', '#dbb5ff', '#dbb5ff', '#dbb5ff'],
             ['#f66d9b', '#f66d9b', '#f66d9b', '#fa9dbb', '#fa9dbb', '#fa9dbb', '#fdc1d3', '#fdc1d3', '#fdc1d3', '#fdc1d3']]

palette_2023 = [['#e3342f', '#e3342f', '#e3342f', '#f7806f', '#f7806f', '#f7806f', '#ffB99f', '#ffB99f', '#ffB99f'],
             ['#f6993f', '#f6993f', '#f6993f', '#fac97f', '#fac97f', '#fac97f', '#fdec6f', '#fdec6f', '#fdec6f'],
             ['#ffed4a', '#ffed4a','#ffed4a','#fff88a', '#fff88a','#fff88a','#ffffba', '#ffffba', '#ffffba'],
             ['#38c172', '#38c172', '#38c172', '#7dd2b2', '#7dd2b2', '#7dd2b2', '#b3dee2', '#b3dee2', '#b3dee2'],
             ['#4dc0b5', '#4dc0b5', '#4dc0b5', '#91d0d9', '#91d0d9', '#91d0d9', '#c4dcf4', '#c4dcf4', '#c4dcf4'],
             ['#3490dc', '#3490dc', '#3490dc', '#89a8ec', '#89a8ec', '#89a8ec', '#c8c0f8', '#c8c0f8', '#c8c0f8'],
             ['#6574cd', '#6574cd', '#6574cd', '#95a4f1', '#95a4f1', '#95a4f1', '#b9bcff', '#b9bcff', '#b9bcff'],
             ['#9561e2', '#9561e2', '#9561e2', '#bd91fa', '#bd91fa', '#bd91fa', '#dbb5ff', '#dbb5ff', '#dbb5ff'],
             ['#f66d9b', '#f66d9b', '#f66d9b', '#fa9dbb', '#fa9dbb', '#fa9dbb', '#fdc1d3', '#fdc1d3', '#fdc1d3']]

file_names_2021 = ['Y2021_Student_01','Y2021_Student_02','Y2021_Student_03','Y2021_Student_04','Y2021_Student_05','Y2021_Student_06','Y2021_Student_07']
year2021_df = []
for i in range(len(file_names_2021)):
    temp_df = pd.read_csv("/Users/stephanielin/Desktop/TLTLab/Y2021/"+file_names_2021[i]+".csv",index_col=0)
    year2021_df.append(temp_df)

file_names_2022 = ['Y2022_Student_01','Y2022_Student_02','Y2022_Student_03','Y2022_Student_04','Y2022_Student_05','Y2022_Student_06','Y2022_Student_07','Y2022_Student_08','Y2022_Student_09','Y2022_Student_10','Y2022_Student_11','Y2022_Student_12']
year2022_df = []
for i in range(len(file_names_2022)):
    temp_df = pd.read_csv("/Users/stephanielin/Desktop/TLTLab/Y2022/"+file_names_2022[i]+".csv",index_col=0)
    year2022_df.append(temp_df)

file_names_2023 = ['Y2023_Student_01','Y2023_Student_02','Y2023_Student_03','Y2023_Student_04','Y2023_Student_05','Y2023_Student_06','Y2023_Student_07','Y2023_Student_08','Y2023_Student_09','Y2023_Student_10','Y2023_Student_11','Y2023_Student_12']
year2023_df = []
for i in range(len(file_names_2023)):
    temp_df = pd.read_csv("/Users/stephanielin/Desktop/TLTLab/Y2023/"+file_names_2023[i]+".csv",index_col=0)
    year2023_df.append(temp_df)

keywords = pd.read_csv("/Users/stephanielin/Desktop/TLTLab/dictionary 5.0 (final with subcategory).csv")["display concept"].tolist()

# the number shows which category the keyword belongs to
keywords_group = pd.read_csv("/Users/stephanielin/Desktop/TLTLab/dictionary 5.0 (final with subcategory).csv")["category"].to_numpy()

# def aggregate_individual_knowledge_map(student_df, color_plate):
#     nets = []
#     for i in range(student_df.shape[0]):
#         net = Network(notebook=True, heading="Individual Knowledge Map Aggregate Week " + str(i+1))
#         occurence = student_df.iloc[:(i+1)].sum()
#         for n in range(i+1): 
#             for j, value in enumerate(student_df.iloc[n]):
#                 if value == 1:
#                     category_number = keywords_group[j]-1
#                     net.add_node(j, label=keywords[j], title='Week'+str(n+1),size=(int(occurence[j])+1)*3, color=color_plate[category_number][n])
#         net_id = [dic['id'] for dic in net.nodes]
#         for i in net_id:
#             for j in net_id:
#                 if i != j and keywords_group[i] == keywords_group[j]:
#                     net.add_edge(i,j,hidden=True)
#         net.repulsion(central_gravity=1,spring_length=50)
#         nets.append(net)
        
#     return nets

def aggregate_individual_knowledge_map(student_df, color_plate):
    nets = []
    category_positions = np.linspace(0, 2 * np.pi, len(color_plate))
    for i in range(student_df.shape[0]):
        net = Network(notebook=True)
        occurence = student_df.iloc[:(i + 1)].sum()
        node_counts = [0] * len(color_plate)
        for n in range(i + 1):
            for j, value in enumerate(student_df.iloc[n]):
                if value == 1:
                    category_number = keywords_group[j] - 1
                    node_counts[category_number] += 1
                    angle = category_positions[category_number]
                    radius = 100 + node_counts[category_number] * 10
                    x = radius * np.cos(angle)
                    y = radius * np.sin(angle)
                    net.add_node(j, label=keywords[j], title='Week' + str(n + 1), size=(int(occurence[j]) + 1) * 3,
                                 color=color_plate[category_number][n], x=x, y=y)
        net_id = [dic['id'] for dic in net.nodes]
        for i in net_id:
            for j in net_id:
                if i != j and keywords_group[i] == keywords_group[j]:
                    net.add_edge(i, j, hidden=True)
        net.repulsion(central_gravity=0.8,spring_length=50)
        nets.append(net)

    return nets

indi_aggregate_s1_2021 = aggregate_individual_knowledge_map(year2021_df[0],palette_2021)
indi_aggregate_s2_2021 = aggregate_individual_knowledge_map(year2021_df[1],palette_2021)
indi_aggregate_s3_2021 = aggregate_individual_knowledge_map(year2021_df[2],palette_2021)
indi_aggregate_s4_2021 = aggregate_individual_knowledge_map(year2021_df[3],palette_2021)
indi_aggregate_s5_2021 = aggregate_individual_knowledge_map(year2021_df[4],palette_2021)
indi_aggregate_s6_2021 = aggregate_individual_knowledge_map(year2021_df[5],palette_2021)
indi_aggregate_s7_2021 = aggregate_individual_knowledge_map(year2021_df[6],palette_2021)

indi_aggregate_s1_2022 = aggregate_individual_knowledge_map(year2022_df[0],palette_2022)
indi_aggregate_s2_2022 = aggregate_individual_knowledge_map(year2022_df[1],palette_2022)
indi_aggregate_s3_2022 = aggregate_individual_knowledge_map(year2022_df[2],palette_2022)
indi_aggregate_s4_2022 = aggregate_individual_knowledge_map(year2022_df[3],palette_2022)
indi_aggregate_s5_2022 = aggregate_individual_knowledge_map(year2022_df[4],palette_2022)
indi_aggregate_s6_2022 = aggregate_individual_knowledge_map(year2022_df[5],palette_2022)
indi_aggregate_s7_2022 = aggregate_individual_knowledge_map(year2022_df[6],palette_2022)
indi_aggregate_s8_2022 = aggregate_individual_knowledge_map(year2022_df[7],palette_2022)
indi_aggregate_s9_2022 = aggregate_individual_knowledge_map(year2022_df[8],palette_2022)
indi_aggregate_s10_2022 = aggregate_individual_knowledge_map(year2022_df[9],palette_2022)
indi_aggregate_s11_2022 = aggregate_individual_knowledge_map(year2022_df[10],palette_2022)
indi_aggregate_s12_2022 = aggregate_individual_knowledge_map(year2022_df[11],palette_2022)

indi_aggregate_s1_2023 = aggregate_individual_knowledge_map(year2023_df[0],palette_2023)
indi_aggregate_s2_2023 = aggregate_individual_knowledge_map(year2023_df[1],palette_2023)
indi_aggregate_s3_2023 = aggregate_individual_knowledge_map(year2023_df[2],palette_2023)
indi_aggregate_s4_2023 = aggregate_individual_knowledge_map(year2023_df[3],palette_2023)
indi_aggregate_s5_2023 = aggregate_individual_knowledge_map(year2023_df[4],palette_2023)
indi_aggregate_s6_2023 = aggregate_individual_knowledge_map(year2023_df[5],palette_2023)
indi_aggregate_s7_2023 = aggregate_individual_knowledge_map(year2023_df[6],palette_2023)
indi_aggregate_s8_2023 = aggregate_individual_knowledge_map(year2023_df[7],palette_2023)
indi_aggregate_s9_2023 = aggregate_individual_knowledge_map(year2023_df[8],palette_2023)
indi_aggregate_s10_2023 = aggregate_individual_knowledge_map(year2023_df[9],palette_2023)
indi_aggregate_s11_2023 = aggregate_individual_knowledge_map(year2023_df[10],palette_2023)
indi_aggregate_s12_2023 = aggregate_individual_knowledge_map(year2023_df[11],palette_2023)

indi_aggregate_s12_2022[9].show("social_network.html")

indi_aggregate_s4_2023[5].show("social_network.html")



