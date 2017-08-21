#!/usr/bin/python
# -*- coding: utf-8 -*-

import wave
import numpy as np


def read_wave_data(file_path):
    f = wave.open(file_path, "rb")
    nframes = f.getnframes()
    framerate = f.getframerate()
    duration = np.arange(0, nframes) * (1.0/framerate)
    return duration

if __name__ == '__main__':
    duration = read_wave_data("03--A-66686102---20170518092836.wav")
    print("duration = %s" % duration)
