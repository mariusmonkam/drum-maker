import json
import wave
import array
import pygame
import numpy as np
import os
import logging

logger = logging.getLogger(__name__)


def save_composition(tracks, filename, sounds, include_voice=False):
    try:
        pygame.mixer.quit()
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

        max_duration = max(track['duration'] for track in tracks) if tracks else 0
        if include_voice and os.path.exists('voice_recording.npy'):
            voice_recording = np.load('voice_recording.npy')
            max_duration = max(max_duration, len(voice_recording) / 44100 * 1000)

        samples = array.array('h', [0] * int(max_duration * 44100 / 1000 * 2))

        for track in tracks:
            sound = sounds.get(track['name'])
            if sound:
                sound_array = pygame.sndarray.samples(sound)
                sound_array = sound_array.astype(np.int16)
                for i in range(0, min(len(samples), len(sound_array))):
                    samples[i] += sound_array[i]

        if include_voice and os.path.exists('voice_recording.npy'):
            voice_recording = np.load('voice_recording.npy')
            voice_stereo = np.column_stack((voice_recording, voice_recording))
            voice_stereo = voice_stereo.astype(np.int16).flatten()
            for i in range(0, min(len(samples), len(voice_stereo))):
                samples[i] += voice_stereo[i]

        # Normalize to 16-bit range
        max_sample = max(abs(sample) for sample in samples)
        if max_sample > 0:
            scaling_factor = 32767 / max_sample
            samples = array.array('h', (int(sample * scaling_factor) for sample in samples))

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(filename)
        os.makedirs(output_dir, exist_ok=True)

        # Save as WAV using wave library
        with wave.open(filename, 'wb') as wav_file:
            wav_file.setnchannels(2)  # Assuming stereo output
            wav_file.setsampwidth(2)
            wav_file.setframerate(44100)
            wav_file.writeframes(samples.tobytes())

        logger.info(f"Composition saved as WAV: {filename}")
        return json.dumps({"success": True, "message": f"Composition saved as WAV: {filename}"})

    except Exception as e:
        logger.error(f"Error in save_composition: {e}")
        return json.dumps({"success": False, "message": f"Error saving composition: {e}"})


