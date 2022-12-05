import yaml

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
    rows = myBase.getLogs(MyWarning)
    print(rows[0])


if __name__ == '__main__':
    main()
