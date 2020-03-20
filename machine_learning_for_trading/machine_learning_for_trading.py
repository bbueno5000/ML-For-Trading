"""
DOCSTRING
"""
import functools
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as mpl_pyplot
import numpy

class MachineLearningForTrading:
    """
    DOCSTRING
    """
    def __init__(self):
        """
        DOCSTRING
        """
        self.date, self.bid, self.ask = numpy.loadtxt('data\\GBPUSD1d.txt',
                                                      unpack=True,
                                                      delimiter=',',
                                                      converters={0:self.converter})

    def converter(self, date_bytes):
        """
        DOCSTRING
        """
        return mpl_dates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))

    def graph_raw(self):
        """
        DOCSTRING
        """
        figure = mpl_pyplot.figure(figsize=(10, 7))
        axis_1 = mpl_pyplot.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40)
        axis_1.plot(self.date, self.bid)
        axis_1.plot(self.date, self.ask)
        mpl_pyplot.gca().get_yaxis().get_major_formatter().set_useOffset(False)
        axis_1.xaxis.set_major_formatter(mpl_dates.DateFormatter('%Y-%m-%d %H:%M:%S'))
        for label in axis_1.xaxis.get_ticklabels():
            label.set_rotation(45)
        axis_2 = axis_1.twinx()
        axis_2.fill_between(self.date, 0, (self.ask-self.bid), facecolor='g', alpha=0.3)
        mpl_pyplot.subplots_adjust(bottom=0.23)
        mpl_pyplot.grid(True)
        mpl_pyplot.show()

    def pattern_finder(self):
        """
        DOCSTRING
        """
        average_line = (self.bid+self.ask)/2
        variable_x = len(average_line)-30
        variable_y = 11
        while variable_y < variable_x:
            point_1 = self.percent_change(average_line[variable_y-10], average_line[variable_y-9])
            point_2 = self.percent_change(average_line[variable_y-10], average_line[variable_y-8])
            point_3 = self.percent_change(average_line[variable_y-10], average_line[variable_y-7])
            point_4 = self.percent_change(average_line[variable_y-10], average_line[variable_y-6])
            point_5 = self.percent_change(average_line[variable_y-10], average_line[variable_y-5])
            point_6 = self.percent_change(average_line[variable_y-10], average_line[variable_y-4])
            point_7 = self.percent_change(average_line[variable_y-10], average_line[variable_y-3])
            point_8 = self.percent_change(average_line[variable_y-10], average_line[variable_y-2])
            point_9 = self.percent_change(average_line[variable_y-10], average_line[variable_y-1])
            point_10 = self.percent_change(average_line[variable_y-10], average_line[variable_y])
            outcome_range = average_line[variable_y+20:variable_y+30]
            current_point = average_line[variable_y]
            print(functools.reduce(lambda x, y: variable_x+y, outcome_range/len(outcome_range)))
            print(current_point)
            print('___________')
            print(point_1, point_2, point_3, point_4, point_5)
            print(point_6, point_7, point_8, point_9, point_10)
            variable_y += 1

    def percent_change(self, start, current):
        """
        DOCSTRING
        """
        return ((float(current)-start)/start)*100.00

if __name__ == '__main__':
    MachineLearningForTrading().pattern_finder()
