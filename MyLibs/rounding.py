from datetime import timedelta, datetime
from pyparsing import Generator


class rounding():

    def arrRoundSortedList(arr: "list", deltaSeconds: int,
                           dateIndex=0, roundValueIndex=1) ->\
                           "Generator[tuple[datetime, int], None, None]":
        tmpData = arr[0][dateIndex]
        rndValue = arr[0][roundValueIndex]
        count = 1
        deltTime = timedelta(seconds=deltaSeconds)
        for index, value in enumerate(arr):
            if index == 0:
                continue
            if value[0] - tmpData <= deltTime:
                rndValue += value[1]
                count += 1
            else:
                yield tmpData, rndValue // count
                tmpData = value[0]
                rndValue = value[1]
                count = 1
