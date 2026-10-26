
# Simulation of Basic Communication System (Tx-Channel-Rx)
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0, 1, 1000)


frequency = 5 
message = np.sin(2 * np.pi * frequency * t)


noise = np.random.normal(0, 0.3, len(t))

received_signal = message + noise


recovered_signal = received_signal


plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(t, message, color='blue')
plt.title("Original Message Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t, noise, color='red')
plt.title("Noise Added by Channel")
plt.xlabel("Time (s)")
plt.ylabel("Noise")
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, recovered_signal, color='green')
plt.title("Received Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
