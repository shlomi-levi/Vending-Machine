import datetime

class TransactionAlreadyCancelledException(Exception):
    def __init__(self, transactionID:int, cancellationTimeStamp:datetime):
        errMsg = f"Transaction with id {transactionID} was already cancelled in {cancellationTimeStamp}"
        super().__init__(errMsg)

class ProductOutOfStockException(Exception):
    def __init__(self, productName: str):
        errMsg = f"The Product {productName} is out of stock!"
        super().__init__(errMsg)

class InsufficientFundsException(Exception):
    def __init__(self, missingAmount:int, productName:str):
        errMsg = f"You are missing {missingAmount}$ to purchase {productName}."
        super().__init__(errMsg)


class UnableToGenerateChangeException(Exception):
    def __init__(self):
        super().__init__('Unable to generate change for this composition of currency')

class TransactionDoesntExistException(Exception):
    def __init__(self, transactionID:int):
        errMsg = f'There is no transaction with the id of {transactionID}.'
        super().__init__(errMsg)