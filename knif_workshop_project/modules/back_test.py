from beartype import beartype
from knif_workshop_project.modules.strategiesimport Strategy

class BackTest:
    @beartype
    def __init__(self,strategy:Strategy, data, n =250):
        self.__strategy = strategy
        self.__data = data
        self.__n = n

    def back_test(self):
        length = len(self.__data)
        signals = [0]*self.__n
        for i in range(self.__n,length):
            sliced = self.__data[i-self.__n:i]
            signal = self.__strategy.generate_signal(sliced)
            signals.append(signal)
            return signals
