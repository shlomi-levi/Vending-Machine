import vmachine

def main():
    vm:vmachine = vmachine.VendingMachine(50, 50, 50, 50)
    vm.setupLogsFile('./logs.txt')

    vm.loadProductsFromJson('products.json')

    vm.viewAvailableProducts()

    # chipsID = vm.addProduct("chips", 3, 15)
    # snickersID = vm.addProduct("Snickers", 5, 10)
    # c:vmachine.Currency = vmachine.Currency(0, 0, 1, 0)
    # vm.purchase(c, snickersID)
    # vm.purchase(c, chipsID)

if __name__ == '__main__':
    main()


