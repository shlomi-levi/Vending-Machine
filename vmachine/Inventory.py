from .Product import Product
import vmachine.VendingMachineExceptions as VendingMachineExceptions
import datetime

class Inventory:
    def __init__(self):
        self.__currentProductID: int = 1
        self.__idToProductObject: dict = dict()
        self.__productsList: list[Product] = []
        self.__logsFile = None

    def addProduct(self, name:str, price:int, quantity:int, manual=True) -> int:
        newProduct:Product = Product(name, price, quantity, self.__currentProductID)

        self.__currentProductID += 1

        self.__productsList.append(newProduct)
        self.__idToProductObject[newProduct.getProductID()] = newProduct

        if manual and self.__logsFile is not None:
            string = (f"Loading 1 product manually ({datetime.datetime.now()}):\n"
                      f"\tProduct ID: {newProduct.getProductID()}\n"
                      f"\tProduct name: {name}\n"
                      f"\tProduct price: {price}\n"
                      f"\tProduct quantity: {quantity}\n\n")

            with open(self.__logsFile, 'a') as file:
                file.write(string + "\n")

        return newProduct.getProductID()

    def setupLogsFile(self, logsFile:str) -> None:
        self.__logsFile = logsFile

    def viewAvailableProducts(self) -> None:
        for prod in self.__productsList:
            if prod.getQuantity() > 0:
                print(prod.getDetails())

    def emptyInventory(self):
        self.__idToProductObject = dict()
        self.__productsList = []

    def getProductByID(self, productID) -> Product:
        if productID not in self.__idToProductObject:
            raise VendingMachineExceptions.ProductDoesntExistException(productID)

        return self.__idToProductObject[productID]

    def loadProductsFromJson(self, fileName:str) -> None:
        import json

        fixedFileName = fileName if '.json' in fileName else (fileName + '.json')

        with open(fixedFileName, 'r') as file:
            result = json.load(file)

        if not result['data'] or len(result['data']) == 0:
            return

        # load products and log data

        string = f"Loading {len(result['data'])} products from file ({datetime.datetime.now()}):\n"
        for product in result['data']:

            prodID = self.addProduct(name=product['name'], price=product['price'], quantity=product['quantity'], manual=False)
            string += (f"\tProduct ID: {prodID}\n"
                       f"\tProduct name: {product['name']}\n"
                       f"\tProduct price: {product['price']}\n"
                       f"\tProduct quantity: {product['quantity']}\n\n")

        string += f"{len(result['data'])} Products loaded successfully.\n\n"

        if self.__logsFile:
            with open(self.__logsFile, 'a') as file:
                file.write(string + '\n')

    def setProductQuantity(self, productID, newQuantity:int) -> None:
        if productID not in self.__idToProductObject:
            raise VendingMachineExceptions.ProductDoesntExistException(productID)

        self.__idToProductObject[productID].setQuantity(newQuantity)

    def getProductQuantity(self, productID) -> int:
        if productID not in self.__idToProductObject:
            raise VendingMachineExceptions.ProductDoesntExistException(productID)

        return self.__idToProductObject[productID].getQuantity()

    def reduceQuantityByOne(self, productID) -> None:
        (self.__idToProductObject[productID]).reduceQuantityByOne()