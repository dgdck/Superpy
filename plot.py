import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib.dates import AutoDateLocator, AutoDateFormatter
from main import csvreader


def main():
     plot_revenue()
    

def plot_revenue():
    data = csvreader('revenue.csv')
    x = []
    y_costs = []
    y_income = []
    y_lost = []
    y_revenue = []
    
    for item in data:
           x.append(datetime.datetime.strptime(item['date'], '%Y-%m-%d'))
           y_costs.append(float(item['costs']))
           y_income.append(float(item['income']))
           y_lost.append(float(item['lost']))
           y_revenue.append(float(item['revenue']))

    # create plots:
    figure, axes = plt.subplots()
        
    # format date:
    locator = AutoDateLocator()
    axes.xaxis.set_major_locator(locator)
    axes.xaxis.set_major_formatter(AutoDateFormatter(locator))
    figure.autofmt_xdate()

    # add data:
    axes.plot(x, y_costs, marker = 'o', label='costs')
    axes.plot(x, y_income, marker = 'o', label='sales')
    axes.plot(x, y_lost, marker = 'o', label='lost')
    axes.plot(x, y_revenue, marker = 'o', label='revenue')    

    # plot make-up:
    axes.set_xlabel('time')
    axes.set_ylabel('EUR')
    axes.set_title('Financial overview')
    axes.legend()
    
    # show plot:
    plt.show()


if __name__ == '__main__':
    main()