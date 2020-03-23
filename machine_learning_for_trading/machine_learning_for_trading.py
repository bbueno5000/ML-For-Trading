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
        current_pattern_1 = self.percent_change(self.average_line[-11], self.average_line[-10])
        current_pattern_2 = self.percent_change(self.average_line[-11], self.average_line[-9])
        current_pattern_3 = self.percent_change(self.average_line[-11], self.average_line[-8])
        current_pattern_4 = self.percent_change(self.average_line[-11], self.average_line[-7])
        current_pattern_5 = self.percent_change(self.average_line[-11], self.average_line[-6])
        current_pattern_6 = self.percent_change(self.average_line[-11], self.average_line[-5])
        current_pattern_7 = self.percent_change(self.average_line[-11], self.average_line[-4])
        current_pattern_8 = self.percent_change(self.average_line[-11], self.average_line[-3])
        current_pattern_9 = self.percent_change(self.average_line[-11], self.average_line[-2])
        current_pattern_10 = self.percent_change(self.average_line[-11], self.average_line[-1])
        self.recognition_pattern.append(current_pattern_1)
        self.recognition_pattern.append(current_pattern_2)
        self.recognition_pattern.append(current_pattern_3)
        self.recognition_pattern.append(current_pattern_4)
        self.recognition_pattern.append(current_pattern_5)
        self.recognition_pattern.append(current_pattern_6)
        self.recognition_pattern.append(current_pattern_7)
        self.recognition_pattern.append(current_pattern_8)
        self.recognition_pattern.append(current_pattern_9)
        self.recognition_pattern.append(current_pattern_10)

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
            similarity_1 = 100.0-abs(self.percent_change(pattern[0], self.recognition_pattern[0]))
            similarity_2 = 100.0-abs(self.percent_change(pattern[1], self.recognition_pattern[1]))
            similarity_3 = 100.0-abs(self.percent_change(pattern[2], self.recognition_pattern[2]))
            similarity_4 = 100.0-abs(self.percent_change(pattern[3], self.recognition_pattern[3]))
            similarity_5 = 100.0-abs(self.percent_change(pattern[4], self.recognition_pattern[4]))
            similarity_6 = 100.0-abs(self.percent_change(pattern[5], self.recognition_pattern[5]))
            similarity_7 = 100.0-abs(self.percent_change(pattern[6], self.recognition_pattern[6]))
            similarity_8 = 100.0-abs(self.percent_change(pattern[7], self.recognition_pattern[7]))
            similarity_9 = 100.0-abs(self.percent_change(pattern[8], self.recognition_pattern[8]))
            similarity_10 = 100.0-abs(self.percent_change(pattern[9], self.recognition_pattern[9]))
            similarity = similarity_1 + similarity_2 + similarity_3 + similarity_4 + similarity_5
            similarity = similarity_6 + similarity_7 + similarity_8 + similarity_9 + similarity_10
            similarity = similarity / 10.0
            if similarity > 70:
                pattern_index = self.pattern_array.index(pattern)
                print('########################################')
                print(self.recognition_pattern)
                print('========================================')
                print(pattern)
                print('----------------------------------------')
                print('Predicted Outcome:', self.performance_array[pattern_index])
                print('########################################')

    def pattern_storage(self):
        """
        DOCSTRING
        """
        start_time = time.time()
        variable_x = len(self.average_line)-30
        variable_y = 11
        while variable_y < variable_x:
            pattern = []
            point_1 = self.percent_change(self.average_line[variable_y-10],
                                          self.average_line[variable_y-9])
            point_2 = self.percent_change(self.average_line[variable_y-10],
                                          self.average_line[variable_y-8])
            point_3 = self.percent_change(self.average_line[variable_y-10],
                                          self.average_line[variable_y-7])
            point_4 = self.percent_change(self.average_line[variable_y-10],
                                          self.average_line[variable_y-6])
            point_5 = self.percent_change(self.average_line[variable_y-10],
                                          self.average_line[variable_y-5])
            point_6 = self.percent_change(self.average_line[variable_y-10],
                                          self.average_line[variable_y-4])
            point_7 = self.percent_change(self.average_line[variable_y-10],
                                          self.average_line[variable_y-3])
            point_8 = self.percent_change(self.average_line[variable_y-10],
                                          self.average_line[variable_y-2])
            point_9 = self.percent_change(self.average_line[variable_y-10],
                                          self.average_line[variable_y-1])
            point_10 = self.percent_change(self.average_line[variable_y-10],
                                           self.average_line[variable_y])
            outcome_range = self.average_line[variable_y+20:variable_y+30]
            current_point = self.average_line[variable_y]
            try:
                average_outcome = functools.reduce(lambda x, y: variable_x+y, outcome_range/len(outcome_range))
            except Exception as exception:
                print(str(exception))
                average_outcome = 0
            future_outcome = self.percent_change(current_point, average_outcome)
            pattern.append(point_1)
            pattern.append(point_2)
            pattern.append(point_3)
            pattern.append(point_4)
            pattern.append(point_5)
            pattern.append(point_6)
            pattern.append(point_7)
            pattern.append(point_8)
            pattern.append(point_9)
            pattern.append(point_10)
            self.pattern_array.append(pattern)
            self.performance_array.append(future_outcome)
            variable_y += 1
        end_time = time.time()
        print('Run Time:Pattern Storage (seconds):', end_time-start_time)

    def percent_change(self, start, current):
        """
        DOCSTRING
        """
        return ((float(current)-start)/abs(start))*100.0

if __name__ == '__main__':
    ml_for_trading = MachineLearningForTrading()
    ml_for_trading.pattern_storage()
    ml_for_trading.current_pattern()
    ml_for_trading.pattern_recognition()
    TOTAL_TIME = time.time()-START_TIME
    print('Run Time:Total (seconds):', TOTAL_TIME)
    