import copy
import datetime

class VendingMachine:
    def __init__(self):
        self._currency:Currency = Currency()
        self._inventory:Inventory = Inventory()
        self._transactions:Transactions = Transactions()

    def addProduct(self, name, price, quantity) -> None:
        self._inventory.addProduct(name, price, quantity)

    def viewAvailableProducts(self) -> None:
        self._inventory.viewAvailableProducts()

    def viewLastTransactions(self, count:int) -> None:
        self._transactions.viewLastTransactions(count)

    def viewTransactionInfo(self, transcationID:int) -> None:
        self._transactions.viewTransactionInfo(transcationID)

    def purchase(self, amountBeingPaid:"Currency", productID:int) -> None:
        requestedProduct = self._inventory.getProductByID(productID)
        requestedProductPrice = requestedProduct.getPrice()

        if requestedProduct.getQuantity() < 1:
            raise ValueError("The product (" + requestedProduct.getProductName() + ") is out of stock.")

        if amountBeingPaid.getTotalCurrency() < requestedProductPrice:
            raise ValueError("You are missing " + str(requestedProductPrice - amountBeingPaid.getTotalCurrency()) + "$ To purchase " + requestedProduct.getProductName() +".")


        if not self._currency.ableToReturnChange(amountBeingPaid, requestedProductPrice):
            raise ValueError("Unable to generate change for this composition of currency")

        change:Currency = self._currency.purchase(amountBeingPaid, requestedProductPrice)
        requestedProduct.reduceQuantityByOne()
        self._transactions.createTransaction(requestedProduct, requestedProductPrice, amountBeingPaid, change)


class Currency:
    def __init__(self, PENNIES:int=0, NICKELS:int=0, DIMES:int=0, QUARTERS:int= 0, FIFTY_CENTS:int=0, ONE_DOLLARS:int=0, TWO_DOLLARS:int=0):
        self.currencyComposition:dict = {
            0.01: PENNIES,
            0.05: NICKELS,
            0.1: DIMES,
            0.25: QUARTERS,
            0.5: FIFTY_CENTS,
            1: ONE_DOLLARS,
            2: TWO_DOLLARS
        }

        self._totalCurrency:int = 0

        for key in self.currencyComposition:
            self._totalCurrency += key * self.currencyComposition[key]

    def getCurrencies(self):
        return self.currencyComposition.keys()

    def getTotalCurrency(self) -> int:
        return self._totalCurrency

    def add(self, money:"Currency") -> None:
        for key in money.currencyComposition:
            self.currencyComposition[key] += money.currencyComposition[key]
            self._totalCurrency += key * money.currencyComposition[key]


    def ableToReturnChange(self, amountBeingPaid:"Currency", productsPrice:int):
        tempCurrency:Currency = copy.deepcopy(self)
        tempCurrency.add(amountBeingPaid)

        return tempCurrency.tryToGenerateChange(amountBeingPaid.getTotalCurrency() - productsPrice)


    def tryToGenerateChange(self, change:int):


    def generateChange(self) -> "Currency":
        pass

class Product:
    def __init__(self, name:str, price:int, quantity:int, _id:int) -> None:
        self._name:str = name
        self._quantity:int = quantity
        self._price:int = price
        self._productID:int = _id

    def getDetails(self) -> str:
        return self._name + "(" + str(self._productID) + ") - " + str(self._price) + "$"

    def getQuantity(self) -> int:
        return self._quantity

    def reduceQuantityByOne(self) -> None:
        self._quantity -= 1

    def getPrice(self) -> int:
        return self._price

    def getProductName(self) -> str:
        return self._name

class Inventory:
    def __init__(self):
        self._currentProductID: int = 1
        self._idToProductObject: dict = dict()
        self._productsList: list[Product] = []

    def addProduct(self, name:str, price:int, quantity:int) -> None:
        newProduct:Product = Product(name, price, quantity, self._currentProductID)

        self._productsList.append(newProduct)
        self._idToProductObject[self._currentProductID] = newProduct

        self._currentProductID += 1

    def viewAvailableProducts(self) -> None:
        for prod in self._productsList:
            if prod.getQuantity() > 0:
                print(prod.getDetails())

    def getProductByID(self, productID) -> Product:
        return self._idToProductObject.get(productID, None)

class Transactions:
    def __init__(self):
        self._currentTransactionID:int = 1
        self._transactions: list[Transaction] = []
        self._transactionsMapping: dict = dict()

    def createTransaction(self, prod:Product, priceAtTimeOfPurchase:int, recieved:Currency, change:Currency):
        t = Transaction(prod, priceAtTimeOfPurchase, recieved, change, self._currentTransactionID)
        self._transactions.insert(0, t)
        self._transactionsMapping[self._currentTransactionID] = t

        self._currentTransactionID += 1

    def viewLastTransactions(self, count:int) -> None:
        transactionCount:int = len(self._transactions)

        for i in range(min(transactionCount, count)):
            print(self._transactions[i].getTransactionInfo())

    def viewTransactionInfo(self, transactionID:int) -> None:
        if transactionID not in self._transactionsMapping:
            raise ValueError("Transcation with the id of " + str(transactionID) + " doesnt exist.")

        print(self._transactionsMapping[transactionID].getTransactionInfo())

class Transaction:
    def __init__(self, prod:Product, priceAtTimeOfPurchase:int, recieved:Currency, change:Currency, _id:int):
        self._transactionID:int = _id
        self._transactionProduct:Product = prod
        self._transactionRecieved:Currency = recieved
        self._transactionChange:Currency = change
        self._transactionWasCancelled:bool = False
        self._transcationDate:datetime = datetime.datetime.now()
        self._transactionAmount = priceAtTimeOfPurchase

    def cancelTransaction(self):
        self._transactionWasCancelled = True

    def getTransactionInfo(self) -> str:
        return "(" + str(self._transcationDate) + ") ID: " + str(self._transactionID) + " " + self._transactionProduct.getProductName() + str(self._transactionProduct.getPrice()) + "$"