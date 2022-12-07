import yaml
import matplotlib.pyplot as plt
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

    plt.figure(figsize=(12, 7))

    for date, ans in rounding.arrRoundSortedList(rows,
                                                 cfg['deltaTimeInSeconds']):
        print(date, ans)
        plt.plot(date, ans, 'o-r', lw=1, mec='b', mew=1, ms=5)

    plt.legend(['Warning line'])
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
