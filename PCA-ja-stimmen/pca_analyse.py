# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 18:10:05 2017

@author: Thomas
"""
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

data = genfromtxt('prozent-ja-stimmen.csv', delimiter=';')
importdata = pd.read_csv('prozent-ja-stimmen.csv', quotechar='"', delimiter=";", encoding="latin-1")
cantons = list(importdata.columns.values)[2:]
data_only = importdata.copy()
del data_only['id']
del data_only['Beschreibung']

post_jura_data = data_only.as_matrix()[0:320, ]
pre_jura_data = data_only.as_matrix()[320:, :25]

pca = PCA(n_components=2)
coordinates = pca.fit_transform(post_jura_data.T)


fig, ax = plt.subplots()
index = np.arange(len(cantons))
colors = cm.hsv(np.linspace(0, 1, len(cantons)))
for i, col in zip(index, colors):
    tmp = plt.scatter(coordinates[i, 0], coordinates[i, 1], color=col, label=cantons[i], s=50)
#plt.legend()
    plt.text(coordinates[i, 0] + 2, coordinates[i, 1] - 2, cantons[i], size=8)
    
n_questions = 10    
questions = pca.components_
weight = np.linalg.norm(questions, axis=0)
indexsort = np.argsort(weight)[-n_questions:]

index = np.arange(n_questions)
colors = cm.hsv(np.linspace(0, 1, n_questions))
plt.figure()
ax = plt.axes()
ids = importdata["id"][indexsort]
for i, col in zip(indexsort, colors):
    ax.arrow(0, 0, questions[0, i], questions[1, i], head_width=0.01, head_length=0.01, fc=col, ec=col, color=col)    
    tmp = plt.scatter(questions[0, i], questions[1, i], color=col, label=ids[i])
    plt.text(questions[0, i], questions[1, i], ids[i])
