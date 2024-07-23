# wav_utils.py
import wave
import array

def save_wav(samples, filename):
    """
    Saves audio samples to a WAV file.

    Args:
        samples (array.array): Array of audio samples.
        filename (str): Filename for the output WAV file.
    """
    sample_rate = 44100
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 2 bytes for 16-bit samples
        wf.setframerate(sample_rate)
        wf.writeframes(samples.tobytes())
