import argparse
import logging
from composition import create_composition

def main():
    parser = argparse.ArgumentParser(description='Create a composition from sound files.')
    parser.add_argument('sounds_dir', type=str, help='Directory containing sound files.')
    parser.add_argument('output_file', type=str, help='Output WAV file path.')
    
    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(level=logging.INFO)
    
    try:
        create_composition(args.sounds_dir, args.output_file)
        logging.info("Composition created successfully.")
    except Exception as e:
        logging.error(f"Error creating composition: {e}")

if __name__ == "__main__":
    main()
