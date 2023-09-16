from .Currency import Currency
from .Inventory import Inventory
from .TransactionsKeeper import TransactionsKeeper

import VendingMachine.VendingMachineExceptions as VendingMachineExceptions
from threading import Lock

class VendingMachine:
    def __init__(self, ONE_SHEKELS:int=0, TWO_SHEKELS:int=0, FIVE_SHEKELS:int=0, TEN_SHEKELS:int=0):
        self.__purchaseLock = Lock()
        self.__addProductLock = Lock()
        self.__currency:Currency = Currency(ONE_SHEKELS, TWO_SHEKELS, FIVE_SHEKELS, TEN_SHEKELS)
        self.__inventory:Inventory = Inventory()
        self.__transactions:TransactionsKeeper = TransactionsKeeper()

    def addProduct(self, name, price, quantity) -> int:
        with self.__addProductLock:
            prodID = self.__inventory.addProduct(name, price, quantity)
            return prodID

    def setCurrency(self, ONE_SHEKELS:int, TWO_SHEKELS:int, FIVE_SHEKELS:int, TEN_SHEKELS:int):
        self.__currency = Currency(ONE_SHEKELS, TWO_SHEKELS, FIVE_SHEKELS, TEN_SHEKELS)

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

            change:int = requestedProductPrice - amountBeingPaid.getTotalCurrency()

            canGenerateChange:bool
            newCurrency:Currency
            changeComposition:Currency

            canGenerateChange, newCurrency, changeList = self.__currency.tryToGenerateChange(amountBeingPaid, change)

            if not canGenerateChange:
                raise VendingMachineExceptions.UnableToGenerateChangeException()

            self.__currency.setCurrencyComposition(newCurrency)

            self.__inventory.reduceQuantityByOne(productID)
            self.__transactions.createTransaction(requestedProduct, requestedProductPrice, amountBeingPaid, changeComposition)

            return changeComposition










