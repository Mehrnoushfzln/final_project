import matplotlib.pyplot as plt

data = ["AWS", "AWS", "Azure", "AWS", "AWS", "AWS", "GCP", "AWS", "AWS", "AWS", "AWS", "GCP"]

# Count the occurrences of each platform
platform_counts = {"AWS": data.count("AWS"), "Azure": data.count("Azure"), "GCP": data.count("GCP")}

# Create a pie chart
labels = platform_counts.keys()
sizes = platform_counts.values()
colors = ['lightpink', 'lightskyblue', 'gold']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.axis('equal')
plt.title('Cloud Platform Preference for Dynamic Technology Complexity')
plt.show()

# Determine the platform with the highest count
max_platform = max(platform_counts, key=platform_counts.get)
print(f"Based on the responses, {max_platform} has the highest dynamic technology complexity.")
