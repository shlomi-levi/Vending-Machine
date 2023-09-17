# Vending Machine Library
![Vending Machine](https://img.shields.io/badge/Vending%20Machine-Python-blue)
<p align="center">
  <img src='https://i.pinimg.com/550x/d1/f4/ee/d1f4ee469417cdeac410dbcf2921c94f.jpg' alt="Vending Machine">
</p>

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Example](#example)

## Introduction

The Vending Machine Library is a Python library that allows you to simulate the functionality of a vending machine. You can use this library to create, manage, and interact with vending machines in your Python projects.

## Features

- Create and manage vending machines with customizable products and prices.
- Load products from JSON files.
- Calculate and return change to the user.
- Keep track of inventory and sales.
- Highly customizable and extensible.

## Example

Products.json:
```json
  {
    "data": [
        {
            "name": "Chips",
            "quantity": 15,
            "price": 3
        },
        {
            "name": "Snickers",
            "quantity": 15,
            "price": 5
        }
    ]
}
```

test.py:
```python
  import vmachine

  vm:vmachine = vmachine.VendingMachine(50, 50, 50, 50)
  vm.setupLogsFile('./logs.txt')
  vm.loadProductsFromJson('products.json')
  
  # This would show that chips has an id of 1 and snickers has an id of 2.
  vm.viewAvailableProducts()
  
  chips = 1
  snickers = 2
  
  c:vmachine.Currency = vmachine.Currency(FIVE_SHEKELS=1, TEN_SHEKELS=1)
  c = vm.purchase(c, chips)
  c = vm.purchase(c, snickers)
```
Console output:
```console
  Chips(Product ID:1) - 3$
  Snickers(Product ID:2) - 5$
```
logs.txt:
```
  Loading 2 Products (2023-09-17 03:01:37.425371):
	Product ID: 1
	Product name: Chips
	Product price: 3
	Product quantity: 15

	Product ID: 2
	Product name: Snickers
	Product price: 5
	Product quantity: 15

2 Products loaded successfully.


Purchase (2023-09-17 03:01:37.425371):
	Transaction ID: 1
	Product: Chips (Product ID: 1)
	Price: 3

	Money given: 
		1: 0
		2: 0
		5: 1
		10: 1

		Total: 15

	Change given:
		1: 0
		2: 1
		5: 0
		10: 1

		Total: 12

Purchase (2023-09-17 03:01:37.426371):
	Transaction ID: 2
	Product: Snickers (Product ID: 2)
	Price: 5

	Money given: 
		1: 0
		2: 1
		5: 0
		10: 1

		Total: 12

	Change given:
		1: 0
		2: 1
		5: 1
		10: 0

		Total: 7

Loading 2 Products (2023-09-17 03:03:14.280768):
	Product ID: 1
	Product name: Chips
	Product price: 3
	Product quantity: 15

	Product ID: 2
	Product name: Snickers
	Product price: 5
	Product quantity: 15

2 Products loaded successfully.


Purchase (2023-09-17 03:03:14.281768):
	Transaction ID: 1
	Product: Chips (Product ID: 1)
	Price: 3

	Money given: 
		1: 0
		2: 0
		5: 1
		10: 1

		Total: 15

	Change given:
		1: 0
		2: 1
		5: 0
		10: 1

		Total: 12

Purchase (2023-09-17 03:03:14.281768):
	Transaction ID: 2
	Product: Snickers (Product ID: 2)
	Price: 5

	Money given: 
		1: 0
		2: 1
		5: 0
		10: 1

		Total: 12

	Change given:
		1: 0
		2: 1
		5: 1
		10: 0

		Total: 7
```
---
Enjoy!

Created by: Shlomi Levi

GitHub: [@shlomi-levi](https://github.com/shlomi-levi)
