import sys
from aubio import source, pitch
import numpy as np
# import matplotlib

# class wavToHz:
#     def __init__(self, your_file, samplerate):
#         self.your_file = "nothing"
#         self.samplerate = 4100

def convert(filename):

    win_s = 4096
    hop_s = 512 
    samplerate = 44100

    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate

    tolerance = 0.8

    pitch_o = pitch("yin", win_s, hop_s, samplerate)
    pitch_o.set_unit("midi")
    pitch_o.set_tolerance(tolerance)

    pitches = []
    confidences = []

    total_frames = 0
    while True:
        samples, read = s()
        pitchTwo = pitch_o(samples)[0]
        pitches += [pitchTwo]
        confidence = pitch_o.get_confidence()
        confidences += [confidence]
        total_frames += read
        if read < hop_s: break

    print(pitches)

    # Calculate duration

    import wave
    import contextlib
    with contextlib.closing(wave.open(filename,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print("Duration of song is: ")
        print(duration)

# print("Average frequency = " + str(np.array(pitches).mean()) + " hz")