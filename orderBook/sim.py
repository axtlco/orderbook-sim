import numpy as np
import matplotlib.pyplot as plt

base_price = 10000
depth = 10
tick = 10

buy_lambda = [2 + (depth - i) * 0.5 for i in range(depth)]
sell_lambda = [2 + i * 0.5 for i in range(depth)]

buy_orders = np.random.poisson(buy_lambda)
sell_orders = np.random.poisson(sell_lambda)

buy_prices = [base_price - (i + 1) * tick for i in range(depth)]
sell_prices = [base_price + (i + 1) * tick for i in range(depth)]

plt.figure(figsize=(10, 5))
plt.barh(buy_prices, buy_orders, color='green', label='Buy Orders')
plt.barh(sell_prices, sell_orders, color='red', label='Sell Orders')
plt.axhline(base_price, color='black', linestyle='--', label='Base Price')
plt.xlabel('Order Quantity')
plt.ylabel('Price')
plt.title('OrderBook Sim (Poisson Distribution)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.gca().invert_yaxis() 
plt.show()
