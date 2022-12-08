import yaml

import pylab
import matplotlib.ticker

from datetime import datetime

from DataBase.mysqllib import mysqllib
from domain.dataBase import MyWarning
from MyLibs.rounding import rounding


def main():

    with open("Configs/Config.yaml", "r") as stream:
        try:
            cfg = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    myBase = mysqllib(cfg['host'],
                      cfg['port'],
                      cfg['user'],
                      cfg['password'],
                      cfg['database'])

    startDate = datetime.strptime(cfg['startDate'], "%d-%m-%Y %H:%M:%S")
    endDate = datetime.strptime(cfg['endDate'], "%d-%m-%Y %H:%M:%S")
    rows = myBase.getCollumns([MyWarning.date_time, MyWarning.answer_time],
                              startDate, endDate)
    if len(rows) == 0:
        print("0 rows get from database")
        return

    figure = pylab.figure()
    axes = figure.add_subplot(1, 1, 1)

    axes.set_title('Just title')
    axes.set_ylabel('Time of responce (s)')
    axes.set_xlabel('Date and time')

    figure.set_figheight(7)
    figure.set_figwidth(12)

    x = []
    y = []
    for date, ans in rounding.arrRoundSortedList(rows,
                                                 cfg['deltaTimeInSeconds']):
        x.append(date.timestamp())
        y.append(ans / 1000)

    formatter = matplotlib.ticker.FuncFormatter(timestampFormatter)
    axes.xaxis.set_major_formatter(formatter)

    pylab.plot(x, y, 'o-r', lw=1, mec='b', mew=1, ms=5)

    axes.grid(True)
    pylab.legend(['Warning line'])
    pylab.show()


def timestampFormatter(timestamp: float, pos):
    date = datetime.fromtimestamp(timestamp)
    return ("{}\n{}".format(date.date(), date.time()))


if __name__ == '__main__':
    main()
