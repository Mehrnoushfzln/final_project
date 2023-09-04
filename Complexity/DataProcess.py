import matplotlib.pyplot as plt

data = ["GCP", "GCP", "Azure", "GCP", "Azure", "AWS", "GCP", "GCP", "GCP", "GCP", "GCP", "GCP"]

# Count the occurrences of each platform
platform_counts = {"GCP": data.count("GCP"), "Azure": data.count("Azure"), "AWS": data.count("AWS")}

# Create a pie chart
labels = platform_counts.keys()
sizes = platform_counts.values()
colors = ['gold', 'lightskyblue', 'lightcoral']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.axis('equal')
plt.title('Cloud Platform Preference for Data Processing Capability')
plt.show()

# Determine the platform with the highest count
max_platform = max(platform_counts, key=platform_counts.get)
print(f"Based on the responses, {max_platform} has the highest data processing capability.")
