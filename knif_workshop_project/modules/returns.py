import numpy as np
class Returns:
    def  __init__(self, returns, freq = 252):
        if replace_nan:
            returns = [0 if np.isnan()]
        self.__returns = returns
        self.__freq = freq
    def get_cumulative_returns(self):
        return list(np.cumprod([x+1 for x in self.__returns])-1)

    def signal_to_returns(self,signals):
        signal_returns = [x*y for x, y in zip(self.__returns, signals)]
        return Returns(signal_returns, self.__freq)

    def __len__(self):
        return len(self.__returns)

    def get_freq(self):
        return self.

    def __str__(self):
        return f'{self.__returns}'
