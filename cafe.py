# Dictionary training

# Step 1: create menu list with items.
menu = ['coffee', 'tea', 'water', 'snack']

# Step 2: create a dictionary for the item stocks.
cafe_stock_dict = {'coffee': 238,
                   'tea': 277,
                   'water': 312,
                   'snack': 183
                   }

# Step 3: create a dictionary for the item prices.
cafe_price_dict = {'coffee': 3.5,
                   'tea': 2.5,
                   'water': 2,
                   'snack': 2.7
                   }

# Either use step 4 and 5 or skip to step 6.
# Step 4: If you wish to know the individual item stock worth left, calculate the stock price for each item.
coffee_stock_worth = (cafe_stock_dict['coffee']) * (cafe_price_dict['coffee'])
print(f'Your total coffee stock price is {coffee_stock_worth}£')

tea_stock_worth = (cafe_stock_dict['tea']) * (cafe_price_dict['tea'])
print(f'Your total tea stock price is {tea_stock_worth}£')

water_stock_worth = (cafe_stock_dict['water']) * (cafe_price_dict['water'])
print(f'Your total water stock price is {water_stock_worth}£')

snack_stock_worth = (cafe_stock_dict['snack']) * (cafe_price_dict['snack'])
print(f'Your total snack stock price is {snack_stock_worth}£')

# Step 5: add them all up together for total stock worth left and print.
total_stock_worth = (coffee_stock_worth) + (tea_stock_worth) + (water_stock_worth) + (snack_stock_worth)
print(f'The total stock worth left for the cafe is {total_stock_worth}£')

# OR skip step 4 and 5 and go straight to step 6.
# Step 6: calculate the total worth by using the total number of stock using sum() times the price.
# of each item in the menu using for loop.
total_stock_worth = sum(cafe_stock_dict[item] * cafe_price_dict[item] for item in menu)  # item = Key : Value
print(f'The total stock worth left for the cafe is {total_stock_worth}£')
