"""
DOCSTRING
"""
# standard imports
import functools
import time
# non-standard imports
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as mpl_pyplot
import numpy

START_TIME = time.time()

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
        self.average_line = (self.bid+self.ask)/2
        self.pattern_array = []
        self.performance_array = []
        self.recognition_pattern = []

    def converter(self, date_bytes):
        """
        DOCSTRING
        """
        return mpl_dates.strpdate2num('%Y%m%d%H%M%S')(date_bytes.decode('ascii'))

    def current_pattern(self):
        """
        DOCSTRING
        """
        for i in range(-30, 0): 
            self.recognition_pattern.append(
                self.percent_change(self.average_line[-31], 
                                    self.average_line[i]))

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

    def pattern_recognition(self):
        """
        DOCSTRING
        """
        for pattern in self.pattern_array:
            similarity = 0
            for i in range(30):
                similarity += 100.0-abs(self.percent_change(pattern[i], self.recognition_pattern[i]))
            similarity = similarity/30.0
            if similarity > 30:
                pattern_index = self.pattern_array.index(pattern)
                print('########################################')
                print(self.recognition_pattern)
                print('========================================')
                print(pattern)
                print('----------------------------------------')
                print('Predicted Outcome:', self.performance_array[pattern_index])
                x_axis = list(range(0, 30))
                figure = mpl_pyplot.figure()
                mpl_pyplot.plot(x_axis, self.recognition_pattern)
                mpl_pyplot.plot(x_axis, pattern)
                mpl_pyplot.show()
                print('########################################')

    def pattern_storage(self):
        """
        DOCSTRING
        """
        start_time = time.time()
        variable_x = len(self.average_line)-60
        variable_y = 31
        while variable_y < variable_x:
            pattern = []
            for i in range(29, -1, -1):
                pattern.append(
                    self.percent_change(self.average_line[variable_y-30],
                                        self.average_line[variable_y-i]))
            outcome_range = self.average_line[variable_y+20:variable_y+30]
            current_point = self.average_line[variable_y]
            try:
                average_outcome = functools.reduce(lambda x, y: variable_x+y,
                                                   outcome_range/len(outcome_range))
            except Exception as exception:
                print(str(exception))
                average_outcome = 0
            future_outcome = self.percent_change(current_point, average_outcome)
            self.pattern_array.append(pattern)
            self.performance_array.append(future_outcome)
            variable_y += 1
        end_time = time.time()
        print('Run Time:Pattern Storage (seconds):', end_time-start_time)

    def percent_change(self, start, current):
        """
        DOCSTRING
        """
        try:
            variable_x = ((float(current)-start)/abs(start))*100.0
            if variable_x == 0.0:
                return 0.01
            else:
                return variable_x
        except:
            return 0.01

if __name__ == '__main__':
    ML_FOR_TRADING = MachineLearningForTrading()
    ML_FOR_TRADING.pattern_storage()
    ML_FOR_TRADING.current_pattern()
    ML_FOR_TRADING.pattern_recognition()
    TOTAL_TIME = time.time()-START_TIME
    print('Run Time:Total (seconds):', TOTAL_TIME)
    