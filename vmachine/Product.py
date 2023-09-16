class Product:
    def __init__(self, name:str, price:int, quantity:int, _id:int) -> None:
        self.__name:str = name
        self.__quantity:int = quantity
        self.__price:int = price
        self.__productID:int = _id

    def getDetails(self) -> str:
        return self.__name + "(" + str(self.__productID) + ") - " + str(self.__price) + "$"

    def getQuantity(self) -> int:
        return self.__quantity

    def reduceQuantityByOne(self) -> None:
        self.__quantity -= 1

    def getPrice(self) -> int:
        return self.__price

    def getProductName(self) -> str:
        return self.__name

    def getProductID(self) -> int:
        return self.__productID