from .Currency import Currency
from .Inventory import Inventory
from .TransactionsKeeper import TransactionsKeeper

import vmachine.VendingMachineExceptions as VendingMachineExceptions
from threading import Lock

class VendingMachine:
    def __init__(self, ONE_SHEKELS:int=0, TWO_SHEKELS:int=0, FIVE_SHEKELS:int=0, TEN_SHEKELS:int=0, logsFile=None):
        self.__purchaseLock = Lock()
        self.__addProductLock = Lock()
        self.__currency:Currency = Currency(ONE_SHEKELS, TWO_SHEKELS, FIVE_SHEKELS, TEN_SHEKELS)
        self.__inventory:Inventory = Inventory()
        self.__transactions:TransactionsKeeper = TransactionsKeeper()
        self.__logsFile = logsFile

        if logsFile is not None:
            self.__transactions.setupLogsFile(logsFile)
            self.__inventory.setupLogsFile(logsFile)

    def addProduct(self, name, price, quantity) -> int:
        with self.__addProductLock:
            prodID = self.__inventory.addProduct(name, price, quantity)
            return prodID

    def loadProductsFromJson(self, fileName: str):
        self.__inventory.loadProductsFromJson(fileName)

    def emptyInventory(self):
        self.__inventory.emptyInventory()
    def setProductQuantity(self, productID: int, newQuantity:int) -> None:
        self.__inventory.setProductQuantity(productID, newQuantity)
    def getProductQuantity(self, productID:int) -> int:
        return self.__inventory.getProductQuantity(productID)

    def setCurrency(self, ONE_SHEKELS:int, TWO_SHEKELS:int, FIVE_SHEKELS:int, TEN_SHEKELS:int) -> None:
        self.__currency = Currency(ONE_SHEKELS, TWO_SHEKELS, FIVE_SHEKELS, TEN_SHEKELS)

    def setupLogsFile(self, logsFile:str) -> None:
        self.__logsFile = logsFile
        self.__transactions.setupLogsFile(logsFile)
        self.__inventory.setupLogsFile(logsFile)

    def viewAvailableProducts(self) -> None:
        self.__inventory.viewAvailableProducts()

    def viewLastTransactions(self, count:int=5) -> None:
        self.__transactions.viewLastTransactions(count)

    def viewTransactionInfo(self, transcationID:int) -> None:
        self.__transactions.viewTransactionInfo(transcationID)

    def purchase(self, amountBeingPaid:Currency, productID:int) -> Currency:
        with self.__purchaseLock:
            requestedProduct = self.__inventory.getProductByID(productID)
            requestedProductPrice = requestedProduct.getPrice()

            if requestedProduct.getQuantity() < 1:
                raise VendingMachineExceptions.ProductOutOfStockException(requestedProduct.getProductName())

            if amountBeingPaid.getTotalCurrency() < requestedProductPrice:
                raise VendingMachineExceptions.InsufficientFundsException(requestedProductPrice - amountBeingPaid.getTotalCurrency(), requestedProduct.getProductName())

            change:int = amountBeingPaid.getTotalCurrency() - requestedProductPrice

            canGenerateChange:bool
            newCurrency:Currency
            changeComposition:Currency

            canGenerateChange, newCurrency, changeComposition = self.__currency.tryToGenerateChange(amountBeingPaid, change)

            if not canGenerateChange:
                raise VendingMachineExceptions.UnableToGenerateChangeException()

            self.__currency = newCurrency

            self.__inventory.reduceQuantityByOne(productID)
            self.__transactions.createTransaction(requestedProduct, requestedProductPrice, amountBeingPaid, changeComposition)

            return changeComposition










