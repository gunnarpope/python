""" Create a sine wave and plot the Bode plot of the frequency response.
    by: gunnar pope
    date: 1/27/23
"""
import numpy as np
import matplotlib.pyplot as plt

""" create a function that returns a sine wave at 10 hz for 1 second """
def sine_wave():
    return np.sin(2 * np.pi * 10 * np.arange(1000) / 1000)

""" create a function that plots the sine wave along with a subplot of the FFT.
    plot the frequency in units of Hz.
    plot the amplitude in units of dB.
"""
def plot_sine_wave():
    x = sine_wave()
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(x)
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.subplot(2,1,2)
    plt.magnitude_spectrum(x, Fs=1000, scale='dB')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (dB)')
    plt.grid(True)
    plt.show()

plot_sine_wave()


