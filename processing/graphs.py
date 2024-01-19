import math

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def softmax(vec, temperature):
    """
    turn vec into normalized probability
    """
    sum_exp = sum(math.exp(x/temperature) for x in vec)
    return [math.exp(x/temperature)/sum_exp for x in vec]


def get_percentage_graph(vacancies, model):
    vacancie = vacancies.loc[0]
    labels = vacancie.keys()
    feature_contribution = []

    for label in labels:
        indexes = [index for index, col in enumerate(
            model.feature_names_in_) if label in col]
        feature_coefs = model.coef_[indexes]
        feature_vec = vacancie.iloc[indexes].values
        feature_contribution.append(feature_vec.dot(feature_coefs))

    feature_contribution = np.abs(np.array(feature_contribution))

    indexes = np.argwhere(feature_contribution != 0).flatten()
    indexes_zero = np.argwhere(feature_contribution == 0).flatten()

    scaler = MinMaxScaler()
    scaler.fit(feature_contribution[indexes].reshape(-1, 1))

    data = scaler.transform(feature_contribution[indexes].reshape(-1, 1))
    data = data.reshape(1, -1).flatten()

    data_probs = softmax(data, 1)

    if len(indexes_zero) != 0:
        data_probs.insert(indexes_zero, 0)

    data_probs = np.array(data_probs)

    colors = sns.color_palette('pastel')[0:5]
    fig, ax = plt.subplots()
    ax.pie(data_probs, labels=labels, colors=colors, autopct='%.0f%%')
    return fig
