import numpy as np
import scipy.io.wavfile as wavfile
import fire
import pyaudio

dt = 0

C4 = 259
D4 = 290
E4 = 326
F4 = 345
G4 = 388
A4 = 435
B4 = 488
C5 = 517

L = 400
H = 800

volume = 0.5
duration = 0.25


def synthesize(note_duration, hzs_left, hzs_right, fs=44100):
    global dt
    samples_lst_left = []
    samples_lst_right = []
    for f_left, f_right in zip(hzs_left, hzs_right):
        x = np.arange(fs * dt, fs * (note_duration + dt)) 
        if f_left == 0:
            samples_left = np.zeros(int(fs*note_duration)).astype(np.float32)
        else:
            samples_left = (np.sin(2 * np.pi * np.arange(fs * dt, fs * (note_duration + dt)) * f_left / fs)).astype(np.float32)
        
        if f_right == 0:
            samples_right = np.zeros(int(fs*note_duration)).astype(np.float32)
        else:
            samples_right = (np.sin(2 * np.pi * np.arange(fs * dt, fs * (note_duration + dt)) * f_right / fs)).astype(np.float32)

        samples_lst_left.append(samples_left)
        samples_lst_right.append(samples_right)
        dt += note_duration
    return np.column_stack((np.concatenate(samples_lst_left), np.concatenate(samples_lst_right)))



def deutsch_1975_1a():
    """
    Deutsch, D. (1975). Two-channel listening to musical scales. The Journal of the Acoustical Society of America, 57(5), 1156-1160.
    Fig 1a.
    """
    
    repetitions = 10

    signal = synthesize(duration,
                        [ C5, D4, A4, F4, F4, A4, D4, C5 ] * repetitions,
                        [ C4, B4, E4, G4, G4, E4, B4, C4 ] * repetitions)

    return signal * volume

def deutsch_1975_1b():
    """
    Deutsch, D. (1975). Two-channel listening to musical scales. The Journal of the Acoustical Society of America, 57(5), 1156-1160.
    Fig 1b.
    """
    
    repetitions = 10

    signal = synthesize(duration,
                        [ 0, D4, 0, F4, 0, A4, 0, C5 ] * repetitions,
                        [ C4, 0, E4, 0, G4, 0, B4, 0 ] * repetitions)

    return signal * volume


def deutsch_1975_1c():
    """
    Deutsch, D. (1975). Two-channel listening to musical scales. The Journal of the Acoustical Society of America, 57(5), 1156-1160.
    Fig 1c.
    """
    
    repetitions = 10

    signal = synthesize(duration,
                        [ C5, 0, A4, 0, F4, 0, D4, 0 ] * repetitions,
                        [ 0, B4, 0, G4, 0, E4, 0, C4 ] * repetitions)

    return signal * volume


def deutsch_1975_discussion():
    """
    The first test sequence consisted of the repetitive presentation of the ascending scale switching from ear to ear shown on Fig. 1(b), 
    and so had indeed been hidden in the dichotic sequence. 
    The second consisted of the repetitive presentation of the upper tones of the dichotic sequence, but these were presented entirely to the right ear, 
    and so had not in fact had been hidden. 
    The order of presentation of the two test sequences was strictly counterbalanced.
    """

    first_test_sequence = [
        [0, D4, 0, F4, 0, A4, 0, C5], # Left
        [C4, 0, E4, 0, G4, 0, B4, 0] # Right
    ]

    second_test_sequence = [
        [0, 0, 0, 0, 0, 0, 0, 0], # Left
        [C5, B4, A4, G4, G4, A4, B4, C5] # Right
    ]

    signal = synthesize(duration,
                        first_test_sequence[0] + second_test_sequence[0],
                        first_test_sequence[1] + second_test_sequence[1])

    return signal * volume



def deutsch_1974():
    """
    Octave Illussion
    Deutsch, D. (1974). An auditory illusion. Nature, 251(5473), 307–309. https://doi.org/10.1038/251307a0
    """
    repetitions = 40

    signal = synthesize(duration, [ H, L ] * repetitions, [ L, H ] * repetitions)

    return signal * volume



def generate_signal(experiment, reversed):
    if experiment in globals():
        signal = globals()[experiment]()
    else:
        print(f'Experiment \'{experiment}\' not implemented')
        exit(1)
    if reversed:
        signal[:, [0, 1]] = signal[:, [1, 0]]
    return signal

def main(mode='play', experiment='deutsch_1975_1a', reversed=False):
    stereo_signal = generate_signal(experiment, reversed)

    if mode == 'play':
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32,
                channels=2,  # Stereo
                rate=44100,
                output=True)

        # Play the stereo signal
        stream.write(stereo_signal.tobytes())

        # Stop the stream
        stream.stop_stream()
        stream.close()

        # Terminate PyAudio
        p.terminate()

    elif mode == 'save':
        stereo_signal = np.int16(stereo_signal * 32767)
        wav_name = experiment + '_rev.wav' if reversed else experiment + '.wav'
        wavfile.write(wav_name, 44100, stereo_signal)
        


fire.Fire(main)