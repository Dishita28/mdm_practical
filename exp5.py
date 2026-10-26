import matplotlib.pyplot as plt
# Sample data
parameters = ['Download', 'Upload', 'Latency']
values = [95, 42, 18]
plt.figure(figsize=(7,5))
plt.bar(parameters, values)
plt.title("Network Performance")
plt.ylabel("Value (Mbps / ms)")
plt.grid(axis='y')
plt.show()