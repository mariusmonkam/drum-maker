# Drum Maker

## Description

Drum Maker is a Python-based tool for creating audio compositions using sound files. This project reads sound files from a directory, mixes them according to specified tracks, and outputs a single WAV file with the mixed audio. It also includes a Node.js script to handle the setup and execution of the Python script.

## Project Structure

```
/drum_maker
│
├── /scripts
│   ├── main.py
│   ├── file_utils.py
│   ├── audio_processing.py
│   ├── wav_utils.py
│   └── composition.py
│
├── /sounds                 # Place your sound files here
│   ├── kick.wav
│   └── snare.wav
│
├── requirements.txt
├── package.json
├── index.js
└── README.md
```

## Requirements

### Python Dependencies

The project requires the following Python libraries:

- `numpy`
- `soundfile`

### Node.js Dependencies

The Node.js script requires:

- `child_process`
- `path`
- `fs`

## Installation

### Python Environment

1. **Create a Virtual Environment** (Recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. **Install Python Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Node.js Setup

1. **Install Node.js Dependencies**:

   If you haven’t already, initialize a Node.js project and install the required modules:

   ```bash
   npm init -y
   npm install
   ```

2. **Install Required Modules**:

   ```bash
   npm install
   ```

## Usage

### Preparing Your Sound Files

1. **Place Your Sound Files**:

   Add your `.wav` or `.ogg` sound files to the `sounds` directory. For example:

   ```
   /drum_maker/sounds/
   ├── kick.wav
   └── snare.wav
   ```

2. **Create the Composition**:

   You can run the Python script directly if you prefer not to use the Node.js script.

   ```bash
   python scripts/main.py sounds output.wav
   ```

   Replace `sounds` with the path to your directory containing the sound files (relative to the project root), and `output.wav` with the path for the output WAV file.

### Running via Node.js Script

To install Python dependencies and run the script via Node.js:

1. **Ensure Python and Node.js are Installed**.

2. **Run the Node.js Script**:

   ```bash
   node index.js
   ```

   This will install the required Python packages and execute the Python script. Make sure that the `sounds` directory and `output.wav` are correctly specified in the Node.js script if needed.

## Contributing

Feel free to submit issues, pull requests, or suggestions. Make sure to follow the project's code style and contribute in a way that maintains the integrity and purpose of the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
