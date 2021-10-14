from matplotlib import pyplot as plt
from matplotlib import dates
from pyowm_helper import get_temperature
from api_key import get_humidity

degree_sign = u'\N{DEGREE SIGN}'


def init_plot():
    plt.figure('PyOWM Weather', figsize=(5, 4))
    plt.xlabel('Day')
    plt.ylabel(f'Temperature({degree_sign}F)')
    plt.title('Weekly Forecast')


def plot_temperatures(days, temp_min, temp_max):
    days = dates.date2num(days)
    bar_min = plt.bar(days - .25, temp_min, width=0.5, color='#4286f4')
    bar_max = plt.bar(days + .25, temp_max, width=0.5, color='#e58510')
    return (bar_min, bar_max)


def label_xaxis(days):
    plt.xticks(days)
    axes = plt.gca()
    xaxis_format = dates.DateFormatter('%m/%d')
    axes.xaxis.set_major_formatter(xaxis_format)


def write_temperatures_on_bar_chart(bar_min, bar_max):
    axes = plt.gca()
    y_axis_max = axes.get_ylim()[1]
    label_offset = y_axis_max * .1
    for bar_chart in [bar_min, bar_max]:
        for index, bar in enumerate(bar_chart):
            height = bar.get_height()
            xpos = bar.get_x() + bar.get_width() / 2.0
            ypos = height - label_offset
            label_text = str(int(height)) + degree_sign
            plt.text(xpos, ypos, label_text, horizontalalignment='center', verticalalignment='bottom', color='white')



def init_plot1():
    plt.figure('PyOWM Weather', figsize=(5,4))
    plt.xlabel('Day')
    plt.ylabel(f'Humidity (%)')
    plt.title('Humidity Forecast')

def plot_humidity(day, humidity):

    bar_humidity = plt.bar(day, humidity,align='center')
    return (bar_humidity)

def label_xaxis1(day):
    # Use the days as the x-axis labels
    plt.xticks(day)
    # Set format for axis label to just month and day
    axes = plt.gca()
    xaxis_format = dates.DateFormatter('%m/%d')
    axes.xaxis.set_major_formatter(xaxis_format)

def write_humidity_on_bar_chart(bar_humidity):
    axes = plt.gca()
    y_axis_max = axes.get_ylim()[1]
    label_offset = y_axis_max * .1
    # Write the temperatures on the chart
    for index, bar in enumerate(bar_humidity):
        height = bar.get_height()
        xpos = bar.get_x() + bar.get_width()/2.0
        ypos = height - label_offset
        label_text = str(int(height)) + "%"
        label = plt.text(xpos, ypos, label_text,
                         horizontalalignment='center',
                         verticalalignment='bottom',
                         color='white')



if __name__ == '__main__':
    City = input("Enter the City: ")
    init_plot()
    days, temp_min, temp_max = get_temperature(City)
    bar_min, bar_max = plot_temperatures(days, temp_min, temp_max)
    label_xaxis(days)
    write_temperatures_on_bar_chart(bar_min, bar_max)

    plt.show()


    day, humidity = get_humidity(City)
    init_plot1()
    bar_humidity = plot_humidity(day, humidity)
    label_xaxis1(day)
    write_humidity_on_bar_chart(bar_humidity)
    plt.show()