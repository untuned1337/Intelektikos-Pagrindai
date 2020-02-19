import matplotlib
import Calculations as Cl
import matplotlib.pyplot as plt
from matplotlib.cbook import boxplot_stats
import numpy as np
import Data
import seaborn as sns
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

    bins = range(0, 7000, 500)
    ax[0, 1].set_xticks(bins)
    ax[0, 1].hist(data.hours_list, bins=range(Cl.minimum(data.hours_list), Cl.maximum(data.hours_list), 500),
                  edgecolor='black')
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
    x_tick_labels = ['Non-White', 'White']
    ax[0, 0].set_xticklabels(x_tick_labels, rotation='horizontal')
    ax[0, 0].set_title('white or nah?')
    ax[0, 0].set_xlabel('white?')
    ax[0, 0].set_ylabel('No of individuals')

    bins = bins = np.arange(-0.5, Cl.maximum(data.owned_list) + 1, 1)
    ax[0, 1].hist(data.owned_list, bins=bins, edgecolor='black')
    ax[0, 1].set_xticks(range(0, 2))
    x_tick_labels = ['Yes', 'No']
    ax[0, 1].set_xticklabels(x_tick_labels, rotation='horizontal')
    ax[0, 1].set_title('Owned')
    ax[0, 1].set_xlabel('Is the home owned by the household?')
    ax[0, 1].set_ylabel('No of individuals')

    bins = bins = np.arange(-0.5, Cl.maximum(data.mortgage_list) + 1, 1)
    ax[1, 0].hist(data.mortgage_list, bins=bins, edgecolor='black')
    ax[1, 0].set_xticks(range(0, 2))
    x_tick_labels = ['Yes', 'No']
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
    #print(patches.patches[0].get_height())
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


def write_on_bars():
    pass


def identify_outliers(data: Data.ContinuousData):
    fig = plt.figure()
    fig.suptitle('Box plots for outlier identification', fontsize=16)
    fig.canvas.set_window_title('Box plots')
    plt.subplot(311, title="hours")
    sns.boxplot(x=data.hours_list)
    plt.subplot(312, title="unemployed")
    sns.boxplot(x=data.unemployed_list)
    plt.subplot(313, title="income")
    sns.boxplot(x=data.income_list)
    plt.subplots_adjust(hspace=1)

    print(len(data.hours_list))

    # ax[1, 0] = sns.boxplot(x=data.unemployed_list)
    # ax[2, 0] = sns.boxplot(x=data.income_list)
    # ax = sns.boxplot(x=data.hours_list)
    # ax1 = sns.boxplot(x=data.unemployed_list)
    # ax2 = sns.boxplot(x=data.income_list)
    plt.show()


def test_outliers(data: Data.ContinuousData):
    outlier_dict = {'hours': boxplot_stats(X=data.hours_list)[0]["fliers"],
                    'unemp': boxplot_stats(X=data.unemployed_list)[0]["fliers"],
                    'income': boxplot_stats(X=data.income_list)[0]["fliers"]}
    mod_hours_lst = Cl.remove_from_list(data.hours_list, outlier_dict['hours'])
    mod_unemp_lst = Cl.remove_from_list(data.unemployed_list, outlier_dict['unemp'])
    print(len(data.income_list))
    mod_income_lst = Cl.remove_from_list(data.income_list, outlier_dict['income'])
    print(len(data.income_list))
    print(len(mod_income_lst))
    data_to_plot = [data.income_list, mod_income_lst]
    sns.boxplot(data=data_to_plot, palette=["m", "g"])
    plt.show()
    data_to_plot = [data.hours_list, mod_hours_lst]
    sns.boxplot(data=data_to_plot)
    plt.show()
    data_to_plot = [data.unemployed_list, mod_unemp_lst]
    sns.boxplot(data=data_to_plot)
    plt.show()

# plt.style.use('fivethirtyeight')
# blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
'''
blood_sugar = [0, 0, 0, 0, 1, 1, 1]
bins = [-0.5, 0.5, 1.5]
#plt.xticks(np.arange(0, 2, step=1))
plt.xticks(np.arange(2), [min(blood_sugar), max(blood_sugar)])
plt.hist(blood_sugar, bins=bins, rwidth=0.95, edgecolor='black', color='g')  # by default number of bins is set to 10
plt.show()
'''
