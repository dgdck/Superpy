## SuperPy


---
### Index
1. Introduction
2. Commands
3. Features


---
### Introduction

The goal of the project is to make a working command-line interface (CLI) for supermarket use.
This program keeps logs of different actions which update the inventory when necessary.


---
### Commands

To see the main menu type:

>py super.py -h

<br>
For each command you can bring up their menu with -h :

> - py super.py **date** -h
> - py super.py **buy** -h
> - py super.py **sell** -h
> - py super.py **report** -h


---
### Features

Superpy is able to track costs, sales and inventory  per product.

When a product is purchased the amount, price and expiration date associated with that product are registered.

When a product has been sold Superpy will track the data associated with it. Like the amount sold from which batch, when is has been sold and for what price.

When a product meets its expiration date it is flagged as expired and removed out of the inventory.

All of the above can be viewed in a table. It is possible to only see a specific product in the table. And it is possible to filter on date. Both of these options can be combined.

The revenue is also tracked and available as a graph to see overall costs, sales, revenue and lost (*expired*) products.<br>
It is possible to filter data from a specific time span.<br>
The graph is generated with Matplotlib.

Superpy has its own internal clock system to keep track of the date. Managing this is done trough the CLI and the date is stored in a text-file.<br>
The date can be set to a date of choice.
To advance the time it will add days to the current date.