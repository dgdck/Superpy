import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib.dates import AutoDateLocator, AutoDateFormatter
from main import csvreader


def main():
    data = csvreader('revenue.csv')
    x = []
    y = []
    for item in data:
           x.append(datetime.datetime.strptime(item['date'], '%Y-%m-%d'))
           y.append(float(item['revenue']))
    
    # create plots:
    figure, axes = plt.subplots()
        
    # format date
    locator = AutoDateLocator()
    axes.xaxis.set_major_locator(locator)
    axes.xaxis.set_major_formatter(AutoDateFormatter(locator))
    
    figure.autofmt_xdate()
    
    plt.plot(x, y, marker='o')
    plt.title('Revenue')
    plt.xlabel("time")
    plt.ylabel("EUR")
    plt.grid()
    plt.show()


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


if __name__ == '__main__':
    main()