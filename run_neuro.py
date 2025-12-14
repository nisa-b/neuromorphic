import matplotlib.pyplot as plt
from spike_encoding import wavelet_to_spikes
from motor_neuron import motor_neuron

# ---------------------------------------------------------
# EVET and HAYIR spike generation
# ---------------------------------------------------------
evet_spikes = wavelet_to_spikes("data/evet/evet_01.wav")
hayir_spikes = wavelet_to_spikes("data/hayir/hayir_01.wav")

# ---------------------------------------------------------
# Motor neuron processing
# ---------------------------------------------------------
evet_motor = motor_neuron(evet_spikes)
hayir_motor = motor_neuron(hayir_spikes)

# ---------------------------------------------------------
# Visualization
# ---------------------------------------------------------
plt.figure(figsize=(10,4))

plt.subplot(2,1,1)
plt.stem(evet_motor)
plt.title("Motor Neuron Output – EVET")
plt.ylabel("Spike")

plt.subplot(2,1,2)
plt.stem(hayir_motor)
plt.title("Motor Neuron Output – HAYIR")
plt.ylabel("Spike")
plt.xlabel("Time step")

plt.tight_layout()
plt.show()
