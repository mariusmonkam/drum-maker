# audio_processing.py
import numpy as np
import array

def convert_stereo_to_mono(sound_array):
    """
    Converts a stereo sound array to mono by averaging the two channels.

    Args:
        sound_array (np.array): Stereo sound array.

    Returns:
        np.array: Mono sound array.
    """
    if len(sound_array.shape) == 2 and sound_array.shape[1] == 2:
        return np.mean(sound_array, axis=1).astype(np.int16)
    return sound_array

def mix_tracks(tracks, sounds):
    """
    Mixes sound samples from tracks.

    Args:
        tracks (list): List of track dictionaries with 'name' key and optional 'volume' key.
        sounds (dict): Dictionary mapping sound names to sound objects.

    Returns:
        array.array: Array of mixed audio samples.
    """
    max_duration = 30000  # 30 seconds in milliseconds
    sample_rate = 44100
    num_samples = int(max_duration * sample_rate / 1000)
    
    # Initialize array with zeros
    samples = np.zeros(num_samples, dtype=np.int16)

    for track in tracks:
        sound_name = track['name']
        sound = sounds.get(sound_name)
        if sound is not None:
            volume = track.get('volume', 1.0)
            
            # Convert stereo to mono if necessary
            sound_array = np.array(sound, dtype=np.int16)
            sound_array = convert_stereo_to_mono(sound_array)
            
            # Adjust volume
            sound_array = (sound_array * volume).astype(np.int16)
            
            # Calculate the number of samples for the track
            track_samples = int(track['duration'] * sample_rate / 1000)
            if track_samples > len(sound_array):
                sound_array = np.pad(sound_array, (0, track_samples - len(sound_array)), 'constant')
            else:
                sound_array = sound_array[:track_samples]
                
            # Ensure sound_array length is appropriate
            if len(sound_array) > len(samples):
                sound_array = sound_array[:len(samples)]
                
            # Add sound to the samples array
            samples[:len(sound_array)] += sound_array

    # Normalize to 16-bit range
    samples = np.clip(samples, -32768, 32767).astype(np.int16)

    return array.array('h', samples)
