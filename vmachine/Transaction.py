import VendingMachine.VendingMachineExceptions

from .Product import Product
from .Currency import Currency
import datetime

class Transaction:
    def __init__(self, prod:Product, priceAtTimeOfPurchase:int, recieved:Currency, change:Currency, _id:int):
        self.__transactionID:int = _id
        self.__transactionProduct:Product = prod
        self.__transactionRecieved:Currency = recieved
        self.__transactionChange:Currency = change
        self.__transactionWasCancelled:bool = False
        self.__transcationTimestamp:datetime = datetime.datetime.now()
        self.__transactionCancellationTimestamp:datetime = None #type: ignore
        self.__transactionAmount = priceAtTimeOfPurchase

    def cancelTransaction(self):
        if self.__transactionWasCancelled:
            raise VendingMachine.VendingMachineExceptions.TransactionAlreadyCancelledException(self.__transactionID, self.__transactionCancellationTimestamp)

        self.__transactionWasCancelled = True
        self.__transactionCancellationTimestamp = datetime.datetime.now()

    def getTransactionInfo(self) -> str:
        return "(" + str(self.__transcationTimestamp) + ") ID: " + str(self.__transactionID) + " " + self.__transactionProduct.getProductName() + str(self.__transactionProduct.getPrice()) + "$"