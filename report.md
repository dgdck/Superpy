### Highlights

The *sold* function within main.py is a complex function. This is because it has to check several things before and during execution.
```
def sold(product_name, amount, sell_price):
    total_inventory = sum_inventory(product_name)
    amount = float(amount)
    sell_price = float(sell_price)
```
The total inventory is being calculated with a different function. So that this specific functionality can also be used in other functions.
The amount and sell_price are converted to floats. For the amount a unit of measure could be kilograms, but also per box.
Then several *if* statements are used:
```
    if (total_inventory - amount) < 0:
        return f'Not enough inventory, there are {total_inventory} of {product_name}.'
```
When the amount sold is larger then in storage an error message comes up stating there is not enough and how much is in storage. Now the user knows how much can be sold and new stock needs to be bought.
<br>
```
elif amount > 0:
        products = find_product(product_name) #list of dictionaries

```
The function continues when there is enough on stock and then uses the function *find product*. This reads the inventory.csv-file and returns the specific product-batches as a list of dictionaries. This list will be processed through the following statements:
```
        product = products[0]
        product_inventory = float(product['amount'])
        buy_id = product['buy_id']
```
Of the first item of the list the amount is registered as *product_inventory* and also the *buy_id* or batchnumber.
The following code snippet checks if the inventory from this batch gets completely sold.
```
        if amount >= product_inventory: 
            sold_log(product_name, product_inventory, sell_price, buy_id)
            amount = amount - product_inventory
            remove_product(product['id'])
            return sold(product_name, amount, sell_price)
```
If true the following happens:
- The sell is logged.
- The remaining amount of the order is calculated.
- The product is removed from inventory.
- The function repeats to complete the remaining order.

The following code snippet is executed when the batch is not completely sold:
```
        elif amount < product_inventory: #when stock-inventory is not depleted
            sold_log(product_name, amount, sell_price, buy_id)
            product_inventory = product_inventory - amount
            update_inventory(product['id'], 'amount', product_inventory)
            return 'done'
    else:
        return 'done'
```
If true the following happens:
- The sell is logged.
- Remaining product inventory is calculated.
- Product inventory is updated with the function *update_inventory*.
- Function *sold* returns done when complete.

With the repeat of the function *sold* it is possible to log per product-batch how much is sold and for what price.
