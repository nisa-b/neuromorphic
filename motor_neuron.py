import numpy as np

def motor_neuron(
    spikes,
    weight=1.0,
    leak=0.05,
    threshold=0.5
):
    """
    Simple Leaky Integrate-and-Fire (LIF) motor neuron model.
    """

    V = 0.0  # membrane potential
    output_spikes = []

    for s in spikes:
        # Integrate incoming spike
        V += weight * s

        # Leak
        V -= leak

        # Fire condition
        if V >= threshold:
            output_spikes.append(1)
            V = 0.0  # reset after firing
        else:
            output_spikes.append(0)

    return np.array(output_spikes)
