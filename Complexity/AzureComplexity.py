import matplotlib.pyplot as plt

data = [5, 7, 8, 7, 7, 5, 9, 6, 7, 6, 6, 6]

# Calculate the average
average = sum(data) / len(data)

# Create a bar chart
plt.bar(range(len(data)), data)
plt.xlabel('Participant ID')
plt.ylabel('Knowledge needs to deploy solutions on Microsoft Azure ')
plt.title('Azure Cloud platform Knowledge Rating')
plt.xticks(range(len(data)))
plt.ylim(0, 10)  # Set y-axis limits from 0 to 10
plt.axhline(y=average, color='r', linestyle='--', label=f'Average: {average:.2f}')
plt.legend()
plt.show()

print(f"Average cloud knowledge rating: {average:.2f}")

