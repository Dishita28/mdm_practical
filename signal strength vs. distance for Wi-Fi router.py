
import matplotlib.pyplot as plt

# Distance from Wi-Fi router (meters)
distance = [1, 2, 4, 6, 8, 10]

# Sample RSSI values (dBm)
rssi = [-35, -42, -50, -57, -63, -68]

plt.figure(figsize=(8, 5))
plt.plot(distance, rssi, marker='o', linewidth=2)

plt.title("Wi-Fi Signal Strength vs Distance")
plt.xlabel("Distance from Router (m)")
plt.ylabel("Signal Strength (RSSI in dBm)")

plt.grid(True)

# In RSSI, larger negative values mean weaker signal.
# Invert y-axis so stronger signals appear at the top.
plt.gca().invert_yaxis()

plt.show()
