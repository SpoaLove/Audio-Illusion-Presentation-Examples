# Stream segregation: Spatial location presentation examples


This Python repository is a collection of functions that generate and play or save audio signals for auditory illusions described in two research papers by Diana Deutsch: "Two-channel listening to musical scales" (1975) and "An auditory illusion" (1974).

## Prerequisites
The code requires the following Python libraries to be installed:
- numpy
- scipy
- pyaudio
- fire

You can install these libraries using pip:
```bash
pip install numpy scipy pyaudio fire
```

## Quick start

To generate all the experiment stimuli examples as WAV files, you can use the provided script `generate_all_examples.sh`. This script will execute the Python code for each example and save the generated audio signals as WAV files in the current directory.

1. Open a terminal or command prompt.

2. Navigate to the directory containing the Python script and the `generate_all_examples.sh` script.

3. Run the `generate_all_examples.sh` script:

```bash
./generate_all_examples.sh
```

This will execute the Python script for each example and save the generated audio signals as WAV files in the current directory.

Note: Make sure the script has execute permissions. If not, you can set the execute permission using the following command:

```bash
chmod +x generate_all_examples.sh
```

## Usage

The main functionality of the code is accessed through the main function, which takes the following arguments:

- `mode`: Specifies the mode of operation. It can be set to 'play' to play the generated audio signal or 'save' to save the signal as a WAV file. The default value is 'play'.
- `experiment`: Specifies the experiment stimuli to generate the audio signal for. The available options are '`deutsch_1975_1a`', '`deutsch_1975_1b`', '`deutsch_1975_1c`', '`deutsch_1975_discussion`', and '`deutsch_1974`'. The default value is '`deutsch_1975_1a`'.
- `reversed`: Specifies whether to reverse the stereo channels (to simulate flipping of earphones described in the paper). If True, the left and right channels will be swapped in the generated signal. The default value is False.

To run the code, you can execute the Python script with the desired arguments. For example, to play the audio signal for the experiment '`deutsch_1975_1a`', you can run:

```bash
python script.py --mode play --experiment deutsch_1975_1a
```

## Experiment Stimulis
The code includes several functions, each corresponding to a specific experiment described in the research papers. Here is a brief description of each function:

- `deutsch_1975_1a`: Generates the audio signal for Fig 1a of the paper "Two-channel listening to musical scales" (1975).
- `deutsch_1975_1b`: Generates the audio signal for Fig 1b of the paper "Two-channel listening to musical scales" (1975).
- `deutsch_1975_1c`: Generates the audio signal for Fig 1c of the paper "Two-channel listening to musical scales" (1975).
- `deutsch_1975_discussion`: Generates the audio signal for the additional experiment described in the discussion section of the paper "Two-channel listening to musical scales" (1975).
- `deutsch_1974`: Generates the audio signal for the auditory illusion described in the paper "An auditory illusion" (1974).


## License
This code is provided under the MIT license. Please refer to the LICENSE file for more information.


## References
- Deutsch, D. (1975). Two-channel listening to musical scales. The Journal of the Acoustical Society of America, 57(5), 1156-1160.

- Deutsch, D. (1974). An auditory illusion. Nature 251, 307–309.