import vmachine.VendingMachineExceptions

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
            raise vmachine.VendingMachineExceptions.TransactionAlreadyCancelledException(self.__transactionID, self.__transactionCancellationTimestamp)

        self.__transactionWasCancelled = True
        self.__transactionCancellationTimestamp = datetime.datetime.now()

    def getTransactionInfo(self) -> str:
        ret = (f"Purchase ({str(self.__transcationTimestamp)}):"
               f"\n\tTransaction ID: {str(self.__transactionID)}"
               f"{' (Cancelled)' if self.__transactionWasCancelled else ''}"
               f"\n\tProduct: {self.__transactionProduct.getProductName()} (Product ID: {self.__transactionProduct.getProductID()})"
               f"\n\tPrice: {self.__transactionAmount}\n"
               f"\n\tMoney given: \n{self.__transactionRecieved.getCurrencyInfo()}\n"
               f"\n\tChange given:\n{self.__transactionChange.getCurrencyInfo()}\n")

        if self.__transactionWasCancelled:
            ret += f"\n\tCancellation Timestamp: {str(self.__transactionCancellationTimestamp)}"

        return ret


