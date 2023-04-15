## SuperPy


---
### Index
1. Introduction
2. Commands
	1. First time set-up
	2. Usage
3. Features


---
### Introduction

The goal of the project is to make a working command-line interface (CLI) for supermarket use.
This program keeps logs of different actions which update the inventory when necessary.


---
### Commands

#### First time set-up

It is recommended to reset Superpy and set the desired date.
Reset with:
>     py super.py --reset

Check current date:
>     py super.py date -c
>     py super.py date -current

Set date:
>     py super.py date -st 2023-01-12  
>     py super.py date --set-time 2023-01-12
<br>

#### Usage

To see the main menu type:
>     py super.py -h

<br>
For each command you can bring up their menu with -h :

> -     py super.py date -h
> -     py super.py buy -h
> -     py super.py sell -h
> -     py super.py report -h

Options for date-command:
>     -c, --current                        	     	returns the current date
>     -ad x, --advance x                        	advance time with x days
>     -st [YYYY-MM-DD], --set-time [YYYY-MM-DD] 	sets time to specified date

Options for buy-command:
>     -pn product, --product-name product               product to buy
>     -exp [YYYY-MM-DD], --expiration-date [YYYY-MM-DD] product expiration date
>     -a x, --amount x                                  x amount of product, default = 1
>     -p x, --price x                                   price of purchase, default = 1

Options for sell-command:
>     -pn product, --product-name product  		product to sell
>     -a x, --amount x      				x amount of product, default = 1
>     -p x, --price x       				price of product, default = 1

Options for report-command:
>     -pn product, --product-name product		productname
>     -m mode, --mode mode  				inventory/revenue/buy/sell/expired
>     -ds search date from, --date-search		search date from [YYYY-MM-DD]
>     -u search date until, --until 			search date until [YYYY-MM-DD]

---
### Features

Superpy is able to track costs, sales and inventory  per product.

When a product is purchased the amount, price and expiration date associated with that product are registered.

When a product has been sold Superpy will track the data associated with it. Like the amount of product sold from which batch, when is has been sold and for what price.

When a product meets its expiration date it is flagged as expired and removed from the inventory.

All of the above can be viewed in a table using the Superpy report command. It is possible to only see a specific product in the table. And it is possible to filter on date. These options can be combined.

The revenue is also tracked and available as a graph to see overall costs, sales, revenue and lost (*expired*) products.<br>
It is possible to filter data from a specific time span.<br>
The graph is generated with Matplotlib.

Superpy has its own internal date system. Managing this is done trough the CLI and the date is stored in a text-file.<br>
The date can be set to a date of choice.
To advance the time it will add days to the current date.
