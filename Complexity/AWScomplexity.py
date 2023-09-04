import matplotlib.pyplot as plt

data = [3, 9, 9, 9, 6, 4, 5, 5, 6, 5, 5, 5]

# Calculate the average
average = sum(data) / len(data)

# Create a bar chart
plt.bar(range(len(data)), data)
plt.xlabel('Participant ID')
plt.ylabel('Knowledge needs to deploy solutions on GCP')
plt.title('GCP Cloud platform Knowledge Rating')
plt.xticks(range(len(data)))
plt.ylim(0, 10)  # Set y-axis limits from 0 to 10
plt.axhline(y=average, color='r', linestyle='--', label=f'Average: {average:.2f}')
plt.legend()
plt.show()

print(f"Average cloud knowledge rating: {average:.2f}")
