import soundfile as sf
import os
import logging

logger = logging.getLogger(__name__)


def load_sounds(sounds_dir):
    """
    Loads sound files from a directory into a dictionary.

    Args:
        sounds_dir (str): Path to the directory containing sound files.

    Returns:
        dict: Dictionary mapping sound names to loaded sound objects.
    """
    sounds = {}
    for filename in os.listdir(sounds_dir):
        if filename.endswith(".wav") or filename.endswith(".ogg"):  # Adjust for supported formats
            name, _ = os.path.splitext(filename)
            try:
                sound = sf.read(os.path.join(sounds_dir, filename))[0]
                sounds[name] = sound
                logger.info(f"Loaded sound: {name}")
            except Exception as e:
                logger.warning(f"Error loading sound {filename}: {e}")
    return sounds
