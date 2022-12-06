import yaml
import matplotlib.pyplot as plt

from DataBase.mysqllib import mysqllib
from domain.dataBase import MyWarning


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

    x = myBase.getCollumns([MyWarning.date_time])
    y = myBase.getCollumns([MyWarning.answer_time])

    plt.figure(figsize=(12, 7))
    plt.plot(x, y, 'o-r', label="warning", lw=1, mec='b', mew=1, ms=5)
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
