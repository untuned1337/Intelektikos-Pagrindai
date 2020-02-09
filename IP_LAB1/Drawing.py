import inline as inline
import matplotlib
import Calculations as cl
import matplotlib.pyplot as plt
import numpy as np
import Data


def plot(data):
    bins = range(0, 100, 10)
    plt.title('1')
    plt.xticks(np.arange(0, 100, step=10))
    plt.hist(data, bins=bins, edgecolor='black')
    plt.subplot()
    plt.show()


def plot_continuous(data: Data.ContinuousData):

    fig, ax = plt.subplots(2, 2)
    fig.canvas.set_window_title('Continuous_1')
    fig.set_size_inches(12, 8)

    bins = [18, 25, 35, 45, 55, 64]
    ax[0, 0].set_xticks(bins)
    ax[0, 0].hist(data.age_list, bins=bins, edgecolor='black')
    ax[0, 0].set_title('Age')
    ax[0, 0].set_xlabel('Age of the wife')
    ax[0, 0].set_ylabel('No of individuals')

    ax[0, 1].hist(data.hours_list, bins=range(cl.minimum(data.hours_list), cl.maximum(data.hours_list), 500),
                  edgecolor='black')
    ax[0, 1].set_title('Hours')
    ax[0, 1].set_xlabel('Wife working hours per year')
    ax[0, 1].set_ylabel('No of individuals')

    ax[1, 0].hist(data.income_list, bins=range(cl.minimum(data.income_list), cl.maximum(data.income_list), 120),
                  edgecolor='black')
    ax[1, 0].set_title('Income')
    ax[1, 0].set_xlabel('The other household income in hundreds of dollars')
    ax[1, 0].set_ylabel('No of individuals')

    ax[1, 1].hist(data.education_list, bins=range(cl.minimum(data.education_list), cl.maximum(data.education_list), 1),
                  edgecolor='black')
    ax[1, 1].set_title('Education')
    ax[1, 1].set_xlabel('Education years of the wife ')
    ax[1, 1].set_ylabel('No of individuals')


    #fig1, ax1 = plt.subplots(2, 2)
    #fig1.set_window_title('Continuous_2')
    #fig.set_size_inches(12, 8)

    plt.subplots_adjust(wspace=0.35, hspace=0.35)
    plt.show()


#plt.style.use('fivethirtyeight')
#blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
'''
blood_sugar = [0, 0, 0, 0, 1, 1, 1]
bins = [-0.5, 0.5, 1.5]
#plt.xticks(np.arange(0, 2, step=1))
plt.xticks(np.arange(2), [min(blood_sugar), max(blood_sugar)])
plt.hist(blood_sugar, bins=bins, rwidth=0.95, edgecolor='black', color='g')  # by default number of bins is set to 10
plt.show()
'''