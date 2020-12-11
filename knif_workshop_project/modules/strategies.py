
import pandas as pd
from beartype import beartype
from knif_workshop_project.modules.data_handling import TimeSeries, MovingAverage
class Strategy:
    def __init__(self):
        pass
    def generate_signal(self):
        raise NotImplementedError("Method must be overridden in the derived class!")
    def _is_valid(self):
        raise ValueError("Series has to contain any observation!")

class BuyHoldStrategy(Strategy):

    def __init__(self, series: TimeSeries):
        super().__init__()
        self.__series = series
        self.__is_valid()

    def generate_signal(self):
        return 1

    def _is_valid(self):
        if len(delf.__series)>0:
            return True
        raise ValueError("Series has to contain any observation!")

class ReversalStrategy(Strategy):

    def __init__(self, series: TimeSeries):
        super().__init__()
        self.__series = series
        self.__is_valid()

    def generate_signal(self):
        if self.__series.calculate_returns()[-1]>0:
            return -1
        else:
            return 1

    def _is_valid(self):
        if len(delf.__series) > 0:
            return True
        raise ValueError("Series has to contain any observation!")

class MovingAverageCrossoverStrategy(Strategy):
    @beartype
    def __init__(selfself, series: TimeSeries, short_na_window: int, long_na_window: int):
        super().__int__()
        self.__series = series
        self._is_valid()
        self.__short = short_na_window
        self.__long = long_na_window

    def generate_signal(self):
        short_ma = MovingAverage(self.__series, self.__short)
        long_ma = MovingAverage(self.__series, self.__long)
        if long_ma.get_moving_average()[-1]>short_ma.get_moving_average()[-1]:
            retur 1
        return -1

    def _is_valid(self):
        if len(delf.__series) < self.__long:
            raise ValueError("Too long period!")
        if self.__short > self.__long or self.__short <0:
            raise ValueError("Improper periods lengths!")
        return True

            return True
        raise ValueError("Series has to contain any observation!")
