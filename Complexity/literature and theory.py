import matplotlib.pyplot as plt

data = ["Azure", "AWS", "Azure", "Azure", "Azure", "GCP", "Azure", "Azure", "AWS", "Azure", "Azure", "AWS"]

# Count the occurrences of each platform
platform_counts = {"Azure": data.count("Azure"), "AWS": data.count("AWS"), "GCP": data.count("GCP")}

# Create a pie chart
labels = platform_counts.keys()
sizes = platform_counts.values()
colors = ['lightskyblue', 'lightcoral', 'gold']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.axis('equal')
plt.title('Cloud Platform Preference for Theory and Practice Literature')
plt.show()

# Determine the platform with the highest count
max_platform = max(platform_counts, key=platform_counts.get)
print(f"Based on the responses, {max_platform} is considered to have better literature for theory and practice.")
