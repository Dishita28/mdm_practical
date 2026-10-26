import matplotlib.pyplot as plt

file_size = [1, 5, 10, 25, 50]  # MB
transfer_time = [1.2, 3.5, 7.0, 18.0, 37.0]  # seconds

transfer_rate = []

for size, time in zip(file_size, transfer_time):
    rate = (size * 8) / time
    transfer_rate.append(rate)

print("File Size (MB) Time (s) Rate (Mbps)")

for size, time, rate in zip(file_size, transfer_time, transfer_rate):
    print(f"{size:10} {time:6.2f} {rate:8.2f}")

plt.figure(figsize=(8, 5))

plt.plot(
    file_size,
    transfer_rate,
    marker='o'
)

plt.xlabel("File Size (MB)")
plt.ylabel("Transfer Rate (Mbps)")
plt.title("Bluetooth Data Transfer Performance")
plt.grid(True)

plt.show()
