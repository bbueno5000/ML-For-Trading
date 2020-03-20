"""
DOCSTRING
"""
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as mpl_pyplot
import numpy

def converter(date_bytes):
    """
    DOCSTRING
    """
    return mpl_dates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))

def graph_raw():
    """
    DOCSTRING
    """
    date, bid, ask = numpy.loadtxt('data\\GBPUSD1d.txt', unpack=True, delimiter=',',
                                   converters={0:converter})
    figure = mpl_pyplot.figure(figsize=(10, 7))
    axis_1 = mpl_pyplot.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40)
    axis_1.plot(date, bid)
    axis_1.plot(date, ask)
    mpl_pyplot.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    axis_1.xaxis.set_major_formatter(mpl_dates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for label in axis_1.xaxis.get_ticklabels():
        label.set_rotation(45)
    axis_2 = axis_1.twinx()
    axis_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=0.3)
    mpl_pyplot.subplots_adjust(bottom=0.23)
    mpl_pyplot.grid(True)
    mpl_pyplot.show()

def percent_change(start, current):
    """
    DOCSTRING
    """
    return ((current-start)/start)*100.00

if __name__ == '__main__':
    graph_raw()
