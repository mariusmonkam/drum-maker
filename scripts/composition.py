# composition.py
from file_utils import load_sounds
from audio_processing import mix_tracks
from wav_utils import save_wav

def create_composition(sounds_dir, output_file):
    """
    Creates a 30-second composition using all available audio files.

    Args:
        sounds_dir (str): Path to the directory containing sound files.
        output_file (str): Filename for the output WAV file.
    """
    sounds = load_sounds(sounds_dir)
    
    # Create tracks with each sound lasting 30 seconds
    tracks = []
    for name, sound in sounds.items():
        duration_ms = 30000  # 30 seconds
        volume = 0.5  # Default volume, adjust as needed
        tracks.append({"name": name, "duration": duration_ms, "volume": volume})
    
    mixed_samples = mix_tracks(tracks, sounds)
    save_wav(mixed_samples, output_file)
