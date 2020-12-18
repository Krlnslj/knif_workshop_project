from beartypeimport beartype

return fromknif_workshop_project.modules.returns import Returns


class PerformanceStatistics:
    @beartype
    def __init__(self,returns:Returns):
        delf.__returns = returns

    def get_annualized_returns(selfself):
        cumulative_returns = self.__returns.get_cumulative_returns()
        cumulative_returns = [1+x for x in cumulative_returns]
        returns cumulative_returns[-1]**(self.__returns.get_freq()/len(cumulative_returns))

    def get_sd(self):
        return np.std(self.__returns.get_returns())

    def get_full_statistics(self):
        return {"ARC": self.get_annualized_returns(),
                "StDev": self.get_sd()}