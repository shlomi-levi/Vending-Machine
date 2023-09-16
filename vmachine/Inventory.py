from .Product import Product

class Inventory:
    def __init__(self):
        self.__currentProductID: int = 1
        self.__idToProductObject: dict = dict()
        self.__productsList: list[Product] = []

    def addProduct(self, name:str, price:int, quantity:int) -> int:
        newProduct:Product = Product(name, price, quantity, self.__currentProductID)

        self.__currentProductID += 1

        self.__productsList.append(newProduct)
        self.__idToProductObject[newProduct.getProductID()] = newProduct

        return newProduct.getProductID()

    def viewAvailableProducts(self) -> None:
        for prod in self.__productsList:
            if prod.getQuantity() > 0:
                print(prod.getDetails())

    def getProductByID(self, productID) -> Product:
        return self.__idToProductObject.get(productID, None)

    def reduceQuantityByOne(self, productID) -> None:
        (self.__idToProductObject[productID]).reduceQuantityByOne()