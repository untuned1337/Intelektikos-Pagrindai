import matplotlib
import Calculations as cl
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
    ax[0, 1].hist(data.hours_list, bins=range(cl.minimum(data.hours_list), cl.maximum(data.hours_list), 500),
                  edgecolor='black')
    ax[0, 1].set_title('Hours')
    ax[0, 1].set_xlabel('Wife working hours per year')
    ax[0, 1].set_ylabel('No of individuals')

    ax[1, 0].hist(data.income_list, bins=range(cl.minimum(data.income_list), cl.maximum(data.income_list), 120),
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

    bins = np.arange(-0.5, cl.maximum(data.child5_list)+1, 1)
    x_tick_labels = [str(i) for i in range(1, cl.maximum(data.child5_list)+2)]
    x_tick_labels.insert(0, "none")
    ax1[0, 0].set_xticks(range(0, cl.maximum(data.child5_list)+1, 1))
    ax1[0, 0].set_xticklabels(x_tick_labels, rotation='vertical')
    ax1[0, 0].hist(data.child5_list, bins=bins, edgecolor='black')
    ax1[0, 0].set_title('Child5')
    ax1[0, 0].set_xlabel('Number of children for ages 0 to 5')
    ax1[0, 0].set_ylabel('No of individuals')

    bins = np.arange(-0.5, cl.maximum(data.child13_list)+1, 1)
    x_tick_labels = [str(i) for i in range(1, cl.maximum(data.child13_list)+2)]
    x_tick_labels.insert(0, "none")
    ax1[0, 1].set_xticks(range(0, cl.maximum(data.child13_list)+1, 1))
    ax1[0, 1].set_xticklabels(x_tick_labels, rotation='vertical')
    ax1[0, 1].hist(data.child13_list, bins=bins, edgecolor='black')
    ax1[0, 1].set_title('Child13')
    ax1[0, 1].set_xlabel('Number of children for ages 6 to 13')
    ax1[0, 1].set_ylabel('No of individuals')

    bins = np.arange(-0.5, cl.maximum(data.child17_list)+1, 1)
    x_tick_labels = [str(i) for i in range(1, cl.maximum(data.child17_list)+2)]
    x_tick_labels.insert(0, "none")
    ax1[1, 0].set_xticks(range(0, cl.maximum(data.child17_list)+1, 1))
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


def identify_outliers(data: Data.ContinuousData):
    outlier_dict = {'hours': boxplot_stats(X=data.hours_list)[0]["fliers"],
                    'unemp': boxplot_stats(X=data.unemployed_list)[0]["fliers"],
                    'income': boxplot_stats(X=data.income_list)[0]["fliers"]}
    print(outlier_dict)
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

    #ax[1, 0] = sns.boxplot(x=data.unemployed_list)
    #ax[2, 0] = sns.boxplot(x=data.income_list)
    #ax = sns.boxplot(x=data.hours_list)
    #ax1 = sns.boxplot(x=data.unemployed_list)
    #ax2 = sns.boxplot(x=data.income_list)
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