from .Transaction import Transaction
from .Product import Product
from .Currency import Currency

import VendingMachine.VendingMachineExceptions

class TransactionsKeeper:
    def __init__(self):
        self.__currentTransactionID:int = 1
        self.__transactions: list[Transaction] = []
        self.__transactionsMapping: dict = dict()

    def createTransaction(self, prod:Product, priceAtTimeOfPurchase:int, recieved:Currency, change:Currency):
        t = Transaction(prod, priceAtTimeOfPurchase, recieved, change, self.__currentTransactionID)
        self.__transactions.insert(0, t)
        self.__transactionsMapping[self.__currentTransactionID] = t

        self.__currentTransactionID += 1

    def viewLastTransactions(self, count:int) -> None:
        transactionCount:int = len(self.__transactions)

        for i in range(min(transactionCount, count)):
            print(self.__transactions[i].getTransactionInfo())

    def viewTransactionInfo(self, transactionID:int) -> None:
        if transactionID not in self.__transactionsMapping:
            raise VendingMachine.VendingMachineExceptions.TransactionDoesntExistException(transactionID)

        print(self.__transactionsMapping[transactionID].getTransactionInfo())