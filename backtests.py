import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import random

# Generate 200 random trade amounts between $100-$300
trade_amounts = [random.randint(100, 300) for _ in range(200)]

# Group trades so each group reaches $10,000
trade_groups = []
current_group_count = 0
current_group_total = 0

for amount in trade_amounts:
    current_group_count += 1
    current_group_total += amount
    
    # Once we reach $10,000, save the group and start a new one
    if current_group_total >= 10000:
        trade_groups.append(current_group_count)
        current_group_count = 0
        current_group_total = 0

# If there are leftover trades that didn't reach $10,000, add them
if current_group_count > 0:
    trade_groups.append(current_group_count)

# Create labels for groups
labels = [f"Group {i+1}" for i in range(len(trade_groups))]

# Create bar graph
plt.figure(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))
plt.bar(labels, trade_groups, color=colors, edgecolor='black')
plt.xlabel("Trade Group")
plt.ylabel("Number of Trades to Reach $10,000")
plt.title("Trades Required to Reach $10,000 Per Group")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('bar_graph.png', dpi=100)
print(f"Bar graph saved to 'bar_graph.png'")
print(f"Total trades: {len(trade_amounts)}")
print(f"Total groups: {len(trade_groups)}\n")
for i, count in enumerate(trade_groups, 1):
    print(f"Group {i}: {count} trades to reach $10,000")