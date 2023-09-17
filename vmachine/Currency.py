import copy

class Currency:
    def __init__(self, ONE_SHEKELS:int=0, TWO_SHEKELS:int=0, FIVE_SHEKELS:int=0, TEN_SHEKELS:int=0):
        self.__currencyComposition:dict = {
            1: ONE_SHEKELS,
            2: TWO_SHEKELS,
            5: FIVE_SHEKELS,
            10: TEN_SHEKELS,
        }

        self.__totalCurrency:int = 0

        for key in self.__currencyComposition:
            self.__totalCurrency += key * self.__currencyComposition[key]

    def getCurrencies(self):
        return self.__currencyComposition.keys()

    def getCurrencyInfo(self):
        string = ""

        keys = list(self.__currencyComposition.keys())
        keys.sort()

        for i in range(len(keys)):
            string += f"\t\t{keys[i]}: {self.__currencyComposition[keys[i]]}\n"

        string += f"\n\t\tTotal: {self.__totalCurrency}"

        return string

    def getTotalCurrency(self) -> int:
        return self.__totalCurrency

    def add(self, money:"Currency") -> None:
        for key in money.__currencyComposition.keys():
            self.__currencyComposition[key] += money.__currencyComposition[key]
            self.__totalCurrency += key * money.__currencyComposition[key]

    def tryToGenerateChange(self, amountBeingPaid:"Currency", totalChangeLeft:int) -> tuple[bool, "Currency", "Currency"]:
        tempCurrency:Currency = copy.deepcopy(self)
        tempCurrency.add(amountBeingPaid)

        coins = list(self.__currencyComposition.keys())
        coins.sort(reverse=True)

        changeGiven:Currency = Currency()

        if totalChangeLeft == 0:
            return True, tempCurrency, changeGiven

        for i in range(len(self.__currencyComposition)):
                while totalChangeLeft > 0 and coins[i] <= totalChangeLeft and tempCurrency.__currencyComposition[coins[i]] > 0:
                    changeGiven.__currencyComposition[coins[i]] += 1
                    changeGiven.__totalCurrency += coins[i]

                    totalChangeLeft -= coins[i]

                    tempCurrency.__currencyComposition[coins[i]] -= 1
                    tempCurrency.__totalCurrency -= coins[i]

                    if totalChangeLeft == 0:
                        return True, tempCurrency, changeGiven

        return False, None, None #type: ignore