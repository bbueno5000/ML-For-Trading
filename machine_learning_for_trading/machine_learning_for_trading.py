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
    axis_1.xaxis.set_major_formatter(mpl_dates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    mpl_pyplot.grid(True)
    mpl_pyplot.show()

if __name__ == '__main__':
    graph_raw()
