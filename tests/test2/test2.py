import vmachine

vm:vmachine = vmachine.VendingMachine(50, 50, 50, 50)
vm.setupLogsFile('./logs.txt')

bamba = vm.addProduct("Bamba", 5, 3)
bisli = vm.addProduct("Bisli", 6, 4)
coca_cola = vm.addProduct("Coca Cola", 5, 4)

c:vmachine.Currency = vmachine.Currency(FIVE_SHEKELS=1, TEN_SHEKELS=1)

try:
    c = vm.purchase(c, bamba)
    c = vm.purchase(c, bisli)
    c = vm.purchase(c, coca_cola)

except Exception as e:
    print(e)
