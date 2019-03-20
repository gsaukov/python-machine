import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def graph():
    date, value = np.loadtxt('sampleCSV.csv', delimiter=',', unpack=True,
                             converters={0: convert_date})

    # fig = plt.figure()
    #
    # ax1 = fig.add_subplot(1,1,1, axisbg='white')

    plt.plot_date(x=date, y=value, fmt='-')

    plt.title('some graph')
    plt.ylabel('val')
    plt.xlabel('date')
    plt.show()

def convert_date(date_bytes):
    return mdates.strpdate2num('%d-%m-%y')(date_bytes.decode('ascii'))

graph()