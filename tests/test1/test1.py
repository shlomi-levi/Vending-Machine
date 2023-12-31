import vmachine

vm:vmachine = vmachine.VendingMachine(ONE_SHEKELS=50, TWO_SHEKELS=50, FIVE_SHEKELS=50, TEN_SHEKELS=50)
vm.setupLogsFile('./logs.txt')
vm.loadProductsFromJson('products.json')

# This would show that chips has an id of 1 and snickers has an id of 2.
vm.viewAvailableProducts()

chips = 1
snickers = 2

c:vmachine.Currency = vmachine.Currency(FIVE_SHEKELS=1, TEN_SHEKELS=1)
c = vm.purchase(c, chips)
c = vm.purchase(c, snickers)


