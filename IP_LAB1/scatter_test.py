from matplotlib import pyplot as plt
import Data
import numpy as np
import pandas as pd
import seaborn as sns


def foo(test: Data.ContinuousData):
    plt.style.use('seaborn')

    plt.scatter(test.education_list, test.income_list, s=5, alpha=0.5)

    #m, b = np.polyfit(test.child5_list, test.child13_list, 1)
    #plt.plot(test.child5_list, m * np.asarray(test.child5_list) + b, color='r')
    #plt.title('Working hours-Income scatter plot')
    plt.xlabel('Education')
    plt.ylabel('Income')
    plt.tight_layout()
    plt.show()

    plt.scatter(test.child5_list, test.child17_list, s=5, alpha=0.95)
    #m, b = np.polyfit(test.age_list, test.income_list, 1)
    #plt.plot(test.child13_list, m * np.asarray(test.age_list) + b, color='r')
    plt.xlabel('child5')
    plt.ylabel('child17')
    plt.tight_layout()
    plt.show()


def bar(test: Data.ContinuousData):
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
    plt.show()

def heatmap(test: Data.ContinuousData):
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
    ax = sns.heatmap(df)
    plt.show()