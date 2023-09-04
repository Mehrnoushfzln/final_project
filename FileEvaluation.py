import matplotlib.pyplot as plt

# Data
cloud_platforms = ['Azure', 'AWS', 'GCP']
costs = [0.004, 0.023, 0.026]
backup_times = [4, 20, 32]
restore_times = [33, 6, 10]
colors = ['green', 'yellow', 'red']

# Figure 1: cost values  pie chart 
fig1, ax1 = plt.subplots()
wedges, texts, autotexts = ax1.pie(costs, labels=cloud_platforms, autopct='', startangle=90, colors=colors)
for i, (platform, cost) in enumerate(zip(cloud_platforms, costs)):
    texts[i].set_text(f'{platform}: ${cost:.3f}')
ax1.axis('equal') 
ax1.set_title('Cost Comparison')
plt.show()


# Figure 2: Line graph comparing backup times
fig2, ax2 = plt.subplots()
ax2.plot(cloud_platforms[0], backup_times[0], marker='o', linestyle='None', color='green', label='Azure')
ax2.plot(cloud_platforms[1], backup_times[1], marker='o', linestyle='None', color='yellow', label='AWS')
ax2.plot(cloud_platforms[2], backup_times[2], marker='o', linestyle='None', color='red', label='GCP')
ax2.set_xlabel('Cloud Platforms')
ax2.set_ylabel('Backup Time (s)')
ax2.set_title('Backup Time Comparison')
ax2.legend()
for x, y in zip(cloud_platforms, backup_times):
    ax2.annotate(f'{y} s', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()


# Figure 3: Line graph comparing restore times
fig3, ax3 = plt.subplots()
ax3.plot(cloud_platforms[0], restore_times[0], marker='o', linestyle='None', color='red', label='Azure')
ax3.plot(cloud_platforms[1], restore_times[1], marker='o', linestyle='None', color='green', label='AWS')
ax3.plot(cloud_platforms[2], restore_times[2], marker='o', linestyle='None', color='yellow', label='GCP')
ax3.set_xlabel('Cloud Platforms')
ax3.set_ylabel('Restore Time (s)')
ax3.set_title('Restore Time Comparison')
ax3.legend()
for x, y in zip(cloud_platforms, restore_times):
    ax3.annotate(f'{y} s', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()


