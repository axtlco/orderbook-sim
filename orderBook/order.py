import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

base_price = 10000
depth = 10
tick = 10
threshold = 10

buy_lambda = [2 + (depth - i) * 0.5 for i in range(depth)]
sell_lambda = [2 + i * 0.5 for i in range(depth)]
buy_prices = [base_price - (i + 1) * tick for i in range(depth)]
sell_prices = [base_price + (i + 1) * tick for i in range(depth)]

buy_orders = np.zeros(depth)
sell_orders = np.zeros(depth)

trades = []

fig, ax = plt.subplots(figsize=(10, 5))
buy_bar = ax.barh(buy_prices, buy_orders, color='green', label='Buy Orders')
sell_bar = ax.barh(sell_prices, sell_orders, color='red', label='Sell Orders')
ax.axhline(base_price, color='black', linestyle='--', label='Base Price')
ax.set_xlabel('Order Quantity')
ax.set_ylabel('Price')
ax.set_title('호가창 동적 시뮬레이션 + 체결')
ax.set_xlim(0, 20)
ax.legend()

def update(frame):
    global buy_orders, sell_orders

    new_buy = np.random.poisson(buy_lambda)
    new_sell = np.random.poisson(sell_lambda)
    buy_orders += new_buy
    sell_orders += new_sell

    for i in range(depth):
        if buy_orders[i] >= threshold:
            trades.append(("BUY", buy_prices[i], threshold))
            buy_orders[i] -= threshold
            break 

    for i in range(depth):
        if sell_orders[i] >= threshold:
            trades.append(("SELL", sell_prices[i], threshold))
            sell_orders[i] -= threshold
            break

    for rect, val in zip(buy_bar, buy_orders):
        rect.set_width(val)
    for rect, val in zip(sell_bar, sell_orders):
        rect.set_width(val)

    ax.set_title(f'호가창 시뮬레이션 - Tick {frame} | 최근 체결: {trades[-1] if trades else "없음"}')

ani = FuncAnimation(fig, update, frames=200, interval=500)
plt.tight_layout()
plt.show()
