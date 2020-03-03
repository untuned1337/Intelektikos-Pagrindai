import matplotlib
import Calculations as Cl
import matplotlib.pyplot as plt
from matplotlib.cbook import boxplot_stats
import numpy as np
import Data
import seaborn as sns
import math
import pandas as pd
import decimal


def plot(data):
    bins = range(0, 100, 10)
    plt.title('1')
    plt.xticks(np.arange(0, 100, step=10))
    plt.hist(data, bins=bins, edgecolor='black')
    plt.subplot()
    plt.show()


def plot_continuous(data: Data.ContinuousData):
    # region Draw 1
    fig, ax = plt.subplots(2, 2)
    fig.canvas.set_window_title('Continuous_1')
    fig.set_size_inches(12, 8)

    bins = [18, 25, 35, 45, 55, 64]
    ax[0, 0].set_xticks(bins)
    ax[0, 0].hist(data.age_list, bins=bins, edgecolor='black')
    ax[0, 0].set_title('Age')
    ax[0, 0].set_xlabel('Age of the wife')
    ax[0, 0].set_ylabel('No of individuals')

    bins = range(Cl.minimum(data.hours_list), Cl.maximum(data.hours_list),
                 int(len(data.hours_list) / (1 + 3.22 * math.log(len(data.hours_list)))))
    ax[0, 1].set_xticks(range(bins[0], bins[len(bins) - 1], 500))
    ax[0, 1].hist(data.hours_list, bins=bins,
                  edgecolor='black')
    # range(Cl.minimum(data.hours_list), Cl.maximum(data.hours_list), 500)
    ax[0, 1].set_title('Hours')
    ax[0, 1].set_xlabel('Wife working hours per year')
    ax[0, 1].set_ylabel('No of individuals')

    ax[1, 0].hist(data.income_list, bins=range(Cl.minimum(data.income_list), Cl.maximum(data.income_list), 120),
                  edgecolor='black')
    ax[1, 0].set_title('Income')
    ax[1, 0].set_xlabel('Income in hundreds of dollars')
    ax[1, 0].set_ylabel('No of individuals')

    bins = np.arange(-0.5, 18, 1)
    ax[1, 1].set_xticks(range(0, 18, 1))
    ax[1, 1].hist(data.education_list, bins=bins, edgecolor='black')
    ax[1, 1].set_title('Education')
    ax[1, 1].set_xlabel('Education years of the wife')
    ax[1, 1].set_ylabel('No of individuals')
    # endregion

    fig1, ax1 = plt.subplots(2, 2)
    fig1.canvas.set_window_title('Continuous_2')
    fig1.set_size_inches(12, 8)

    bins = np.arange(-0.5, Cl.maximum(data.child5_list) + 1, 1)
    x_tick_labels = [str(i) for i in range(1, Cl.maximum(data.child5_list) + 2)]
    x_tick_labels.insert(0, "none")
    ax1[0, 0].set_xticks(range(0, Cl.maximum(data.child5_list) + 1, 1))
    ax1[0, 0].set_xticklabels(x_tick_labels, rotation='vertical')
    ax1[0, 0].hist(data.child5_list, bins=bins, edgecolor='black')
    ax1[0, 0].set_title('Child5')
    ax1[0, 0].set_xlabel('Number of children for ages 0 to 5')
    ax1[0, 0].set_ylabel('No of individuals')

    bins = np.arange(-0.5, Cl.maximum(data.child13_list) + 1, 1)
    x_tick_labels = [str(i) for i in range(1, Cl.maximum(data.child13_list) + 2)]
    x_tick_labels.insert(0, "none")
    ax1[0, 1].set_xticks(range(0, Cl.maximum(data.child13_list) + 1, 1))
    ax1[0, 1].set_xticklabels(x_tick_labels, rotation='vertical')
    ax1[0, 1].hist(data.child13_list, bins=bins, edgecolor='black')
    ax1[0, 1].set_title('Child13')
    ax1[0, 1].set_xlabel('Number of children for ages 6 to 13')
    ax1[0, 1].set_ylabel('No of individuals')

    bins = np.arange(-0.5, Cl.maximum(data.child17_list) + 1, 1)
    x_tick_labels = [str(i) for i in range(1, Cl.maximum(data.child17_list) + 2)]
    x_tick_labels.insert(0, "none")
    ax1[1, 0].set_xticks(range(0, Cl.maximum(data.child17_list) + 1, 1))
    ax1[1, 0].set_xticklabels(x_tick_labels, rotation='vertical')
    ax1[1, 0].hist(data.child17_list, bins=bins, edgecolor='black')
    ax1[1, 0].set_title('Child17')
    ax1[1, 0].set_xlabel('Number of children for ages 14 to 17')
    ax1[1, 0].set_ylabel('No of individuals')

    bins = range(0, 31, 1)
    ax1[1, 1].hist(data.unemployed_list, bins=bins, edgecolor='black')
    ax1[1, 1].set_title('Unemployed')
    ax1[1, 1].set_xlabel('local unemployment rate in %')
    ax1[1, 1].set_ylabel('No of individuals')

    plt.subplots_adjust(wspace=0.35, hspace=0.35)

    plt.show()


def plot_categorical(data: Data.CategoricalData):
    fig, ax = plt.subplots(2, 2)
    fig.canvas.set_window_title('Categorical')
    fig.set_size_inches(12, 8)

    bins = bins = np.arange(-0.5, Cl.maximum(data.nonwhite_list) + 1, 1)
    ax[0, 0].hist(data.nonwhite_list, bins=bins, edgecolor='black')
    ax[0, 0].set_xticks(range(0, 2))
    x_tick_labels = ['White', 'Non-White']
    ax[0, 0].set_xticklabels(x_tick_labels, rotation='horizontal')
    ax[0, 0].set_title('Race')
    ax[0, 0].set_xlabel('Is the wife white?')
    ax[0, 0].set_ylabel('No of individuals')

    bins = bins = np.arange(-0.5, Cl.maximum(data.owned_list) + 1, 1)
    ax[0, 1].hist(data.owned_list, bins=bins, edgecolor='black')
    ax[0, 1].set_xticks(range(0, 2))
    x_tick_labels = ['No', 'Yes']
    ax[0, 1].set_xticklabels(x_tick_labels, rotation='horizontal')
    ax[0, 1].set_title('Owned')
    ax[0, 1].set_xlabel('Is the home owned by the household?')
    ax[0, 1].set_ylabel('No of individuals')

    bins = bins = np.arange(-0.5, Cl.maximum(data.mortgage_list) + 1, 1)
    ax[1, 0].hist(data.mortgage_list, bins=bins, edgecolor='black')
    ax[1, 0].set_xticks(range(0, 2))
    x_tick_labels = ['No', 'Yes']
    ax[1, 0].set_xticklabels(x_tick_labels, rotation='horizontal')
    ax[1, 0].set_title('Mortgage')
    ax[1, 0].set_xlabel('Is the home on mortgage?')
    ax[1, 0].set_ylabel('No of individuals')

    # SUKURTI HASHTABLE, kur key - pavadinimas(names), value - pasikartojimu sk(values).
    # ir naudoti ax[1, 1].bar(names, values)
    data_dict = Cl.build_dictionary(data.occupation_list)
    names = list(data_dict.keys())
    values = list(data_dict.values())
    bins = data.occupation_list
    patches = ax[1, 1].bar(names, values)

    ax[1, 1].set_title('Occupation')
    ax[1, 1].set_xlabel('Occupation of the husband')
    ax[1, 1].set_ylabel('No of individuals')

    # region Write bar values
    rects = ax[0, 0].patches
    # Make some labels.

    labels = []
    for patch in rects:
        labels.append(int(patch.get_height()))

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax[0, 0].text(rect.get_x() + rect.get_width() / 2, height, label,
                      ha='center', va='bottom')

    rects = ax[0, 1].patches
    # Make some labels.
    labels = []
    for patch in rects:
        labels.append(int(patch.get_height()))

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax[0, 1].text(rect.get_x() + rect.get_width() / 2, height, label,
                      ha='center', va='bottom')

    rects = ax[1, 0].patches
    # Make some labels.
    labels = []
    for patch in rects:
        labels.append(int(patch.get_height()))

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax[1, 0].text(rect.get_x() + rect.get_width() / 2, height, label,
                      ha='center', va='bottom')

    rects = ax[1, 1].patches
    # Make some labels.
    labels = []
    for patch in rects:
        labels.append(int(patch.get_height()))

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax[1, 1].text(rect.get_x() + rect.get_width() / 2, height, label,
                      ha='center', va='bottom')
    # endregion

    plt.subplots_adjust(wspace=0.35, hspace=0.35)

    plt.show()


def scatter_plot(test: Data.ContinuousData):
    dictionary = {}
    dictionary.setdefault('hours', test.hours_list)
    dictionary.setdefault('income', test.income_list)
    dictionary.setdefault('age', test.age_list)
    dictionary.setdefault('education', test.education_list)

    dictionary.setdefault('unemployed', test.unemployed_list)
    dictionary.setdefault('child5', test.child5_list)
    dictionary.setdefault('child13', test.child13_list)
    dictionary.setdefault('child17', test.child17_list)

    df = pd.DataFrame(dictionary)
    pd.plotting.scatter_matrix(df, diagonal='scatter')

    plt.suptitle('Tolydinių atributų scatter-plot matrica')

    plt.show()


def histograms(data: Data.CategoricalData):
    dictionary = {}
    dictionary.setdefault('mortgage', data.mortgage_list)
    dictionary.setdefault('owned', data.owned_list)
    df = pd.DataFrame(dictionary)

    df_0 = df[df['mortgage'] == 0]
    print(df_0['owned'].sum())
    df_1 = df[df['mortgage'] == 1]
    print(df_1['owned'].sum())

    raw_data = {'owned, when mortgage=0': [df_0['owned'].sum(), data.count - df_0['owned'].sum()],
                'owned, when mortgage=1': [df_1['owned'].sum(), data.count - df_1['owned'].sum()]}
    df_new = pd.DataFrame(raw_data)
    r = [0, 1]

    # From raw value to percentage
    totals = [i + j for i, j in zip(df_new['owned, when mortgage=0'], df_new['owned, when mortgage=1'])]
    mortgages = [i / j * 100 for i, j in zip(df_new['owned, when mortgage=0'], totals)]
    owned = [i / j * 100 for i, j in zip(df_new['owned, when mortgage=1'], totals)]

    # plot
    barwidth = 0.85
    names = ('Not on mortgage', 'On mortgage')
    # Create green Bars
    plt.bar(r, mortgages, color='#b5ffb9', edgecolor='white', width=barwidth, label="group A")
    # Create orange Bars
    plt.bar(r, owned, bottom=mortgages, color='#f9bc86', edgecolor='white', width=barwidth, label="group B")
    legends = ('Owned', 'Not owned')
    plt.legend(legends, loc='upper center', bbox_to_anchor=(0.5, -0.05),
               fancybox=True, shadow=True, ncol=5)
    plt.xticks(r, names)
    plt.title('Correlation between \'Mortgage\' and \'Owned\' attributes')
    plt.show()


def identify_outliers(data: Data.ContinuousData):
    fig = plt.figure()
    fig.suptitle('Box plots for outlier identification', fontsize=16)
    fig.canvas.set_window_title('Box plots')

    plt.subplot(311, title="hours")
    sns.boxplot(x=data.hours_list)
    plt.subplot(312, title="unemployed")
    sns.boxplot(x=data.unemployed_list)
    plt.subplot(313, title="income")
    sns.boxplot(x=data.income_list, whis=6)
    plt.subplots_adjust(hspace=1)

    plt.show()


def remove_outliers(data: Data.ContinuousData):
    outlier_dict = {'hours': boxplot_stats(X=data.hours_list)[0]["fliers"],
                    'unemp': boxplot_stats(X=data.unemployed_list)[0]["fliers"],
                    'income': boxplot_stats(X=data.income_list, whis=6)[0]["fliers"]}

    modified_data = Cl.remove_rows_cont(data, outlier_dict['hours'], 'hours')
    modified_data = Cl.remove_rows_cont(modified_data, outlier_dict['unemp'], 'unemp')
    modified_data = Cl.remove_rows_cont(modified_data, outlier_dict['income'], 'income')

    return modified_data


def correlation_matrix(data: Data.ContinuousData):
    dictionary = {}
    dictionary.setdefault('hours', data.hours_list)
    dictionary.setdefault('income', data.income_list)
    dictionary.setdefault('age', data.age_list)
    dictionary.setdefault('education', data.education_list)

    dictionary.setdefault('unemployed', data.unemployed_list)
    dictionary.setdefault('child5', data.child5_list)
    dictionary.setdefault('child13', data.child13_list)
    dictionary.setdefault('child17', data.child17_list)

    df = pd.DataFrame(dictionary)
    corr = df.corr()
    matrix = np.triu(df.corr())
    ax = sns.heatmap(corr, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(20, 220, n=200), square=True,
                     annot=True, fmt='.1g', mask=matrix)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    ax.set_title('Tolydinių atributų koreliacijos matrica')
    plt.show()
