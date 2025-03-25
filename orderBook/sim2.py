import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

base_price = 10000
depth = 10
tick = 10

buy_lambda = [2 + (depth - i) * 0.5 for i in range(depth)]
sell_lambda = [2 + i * 0.5 for i in range(depth)]
buy_prices = [base_price - (i + 1) * tick for i in range(depth)]
sell_prices = [base_price + (i + 1) * tick for i in range(depth)]

buy_orders = np.zeros(depth)
sell_orders = np.zeros(depth)

fig, ax = plt.subplots(figsize=(10, 5))
buy_bar = ax.barh(buy_prices, buy_orders, color='green', label='Buy Orders')
sell_bar = ax.barh(sell_prices, sell_orders, color='red', label='Sell Orders')
ax.axhline(base_price, color='black', linestyle='--', label='Base Price')
ax.set_xlabel('Order Quantity')
ax.set_ylabel('Price')
ax.set_title('호가창 동적 시뮬레이션')
ax.invert_yaxis()
ax.set_xlim(0, 20)
ax.legend()
ax.grid(True)

def update(frame):
    new_buy = np.random.poisson(buy_lambda)
    new_sell = np.random.poisson(sell_lambda)

    for rect, new in zip(buy_bar, new_buy):
        rect.set_width(rect.get_width() + new)
    for rect, new in zip(sell_bar, new_sell):
        rect.set_width(rect.get_width() + new)

    ax.set_title(f'호가창 동적 시뮬레이션 - Tick {frame}')

ani = FuncAnimation(fig, update, frames=100, interval=500)

plt.tight_layout()
plt.show()
