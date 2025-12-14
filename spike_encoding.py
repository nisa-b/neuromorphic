import numpy as np
import pywt
from scipy.io import wavfile

def downsample(signal, target_len):
    """
    Reduces a long signal to a fixed number of samples.
    """
    indices = np.linspace(0, len(signal) - 1, target_len).astype(int)
    return signal[indices]

def wavelet_to_spikes(
    wav_path,
    wavelet="db4",
    target_len=50,
    threshold=0.005
):
    """
    Converts a speech signal into a spike train using wavelet detail coefficients.
    """

    # Read wav file
    fs, x = wavfile.read(wav_path)

    # Convert to float and flatten
    x = x.astype(float).flatten()

    # Downsample to fixed length
    x_ds = downsample(x, target_len)

    # Discrete Wavelet Transform
    _, cD = pywt.dwt(x_ds, wavelet)

    # Spike encoding via thresholding
    spikes = (np.abs(cD) > threshold).astype(int)

    return spikes
