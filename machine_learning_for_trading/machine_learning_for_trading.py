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
        self.all_data = (self.bid+self.ask)/2
        self.to_what = 37000
        self.average_line = self.all_data[:self.to_what]
        self.pattern_array = []
        self.performance_array = []
        self.recognition_pattern = []
        self.variable_x = len(self.average_line)-60
        self.variable_y = 31
        self.accuracy_array = []
        self.samples = 0

    def __call__(self):
        """
        DOCSTRING
        """
        data_length = int(self.bid.shape[0])
        for i in range(self.to_what, data_length):
            self.average_line = self.average_line[:i]
            self.pattern_storage()
            self.current_pattern()
            self.pattern_recognition()
            input('Press any key to continue . . .')
            self.samples += 1
            accuracy_average = functools.reduce(lambda x, y: self.variable_x+y,
                                                self.accuracy_array)/len(self.accuracy_array)
            print('Backtesting Accuracy (%):', str(accuracy_average))
            print('Number of Samples:', self.samples)

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
        predicted_outcomes_array = []
        pattern_found = False
        plot_pattern_array = []
        x_axis = list(range(0, 30))
        for pattern in self.pattern_array:
            similarity = 0
            for i in range(30):
                similarity += 100.0-abs(self.percent_change(pattern[i],
                                                            self.recognition_pattern[i]))
            similarity = similarity/30.0
            if similarity > 50:
                pattern_found = True
                plot_pattern_array.append(pattern)
        prediction_array = []
        if pattern_found:
            for pattern in plot_pattern_array:
                future_points = self.pattern_array.index(pattern)
                if self.performance_array[future_points] > self.recognition_pattern[29]:
                    point_color = '#24BC00'
                    prediction_array.append(1.00)
                else:
                    point_color = '#D40000'
                    prediction_array.append(-1.00)
                predicted_outcomes_array.append(self.performance_array[future_points])
            real_outcome_range = self.all_data[self.to_what+20:self.to_what+30]
            real_average_outcome = functools.reduce(lambda x, y: self.variable_x+y,
                                                    real_outcome_range)/len(real_outcome_range)
            predicted_average_outcome = functools.reduce(lambda x, y: self.variable_x+y,
                                                         predicted_outcomes_array)/len(
                                                             predicted_outcomes_array)
            real_movement = self.percent_change(self.all_data[self.to_what], real_average_outcome)
            prediction_average = functools.reduce(lambda x, y: self.variable_x+y,
                                                  prediction_array)/len(prediction_array)
            if prediction_average < 0:
                print('Drop Predicted')
                print(self.recognition_pattern[29])
                print(real_movement)
                if real_movement < self.recognition_pattern[29]:
                    self.accuracy_array.append(100.00)
                else:
                    self.accuracy_array.append(0.00)
            if prediction_average > 0:
                print('Rise Predicted')
                print(self.recognition_pattern[29])
                print(real_movement)
                if real_movement > self.recognition_pattern[29]:
                    self.accuracy_array.append(100.00)
                else:
                    self.accuracy_array.append(0.00)

    def pattern_storage(self):
        """
        DOCSTRING
        """
        start_time = time.time()
        while self.variable_y < self.variable_x:
            pattern = []
            for i in range(29, -1, -1):
                pattern.append(
                    self.percent_change(self.average_line[self.variable_y-30],
                                        self.average_line[self.variable_y-i]))
            outcome_range = self.average_line[self.variable_y+20:self.variable_y+30]
            current_point = self.average_line[self.variable_y]
            try:
                average_outcome = functools.reduce(lambda x, y: self.variable_x+y,
                                                   outcome_range/len(outcome_range))
            except Exception as exception:
                print(str(exception))
                average_outcome = 0
            future_outcome = self.percent_change(current_point, average_outcome)
            self.pattern_array.append(pattern)
            self.performance_array.append(future_outcome)
            self.variable_y += 1
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
    MachineLearningForTrading()()
    TOTAL_TIME = time.time()-START_TIME
    print('Run Time:Total (seconds):', TOTAL_TIME)
    