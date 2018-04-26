#!/usr/bin/python
# -*- coding: utf-8 -*-

import wave
import numpy as np


def read_wave_data(file_path):
    # wave.Error: unknown format: 6
    f = wave.open(file_path, "rb")
    nframes = f.getnframes()
    framerate = f.getframerate()
    duration = np.arange(0, nframes) * (1.0/framerate)
    return duration


if __name__ == '__main__':
    duration = read_wave_data("03--A-66686102---20170518092836.wav")
    print("duration = %s" % duration)

'''

D:\devsoft\Python\Python36\python.exe D:/workspace/PycharmProjects/Basics/builtins/bins-modules/bins-wave.py
Traceback (most recent call last):
  File "D:/workspace/PycharmProjects/Basics/builtins/bins-modules/bins-wave.py", line 18, in <module>
    duration = read_wave_data("03--A-66686102---20170518092836.wav")
  File "D:/workspace/PycharmProjects/Basics/builtins/bins-modules/bins-wave.py", line 10, in read_wave_data
    f = wave.open(file_path, "rb")
  File "D:\devsoft\Python\Python36\lib\wave.py", line 499, in open
    return Wave_read(f)
  File "D:\devsoft\Python\Python36\lib\wave.py", line 163, in __init__
    self.initfp(f)
  File "D:\devsoft\Python\Python36\lib\wave.py", line 143, in initfp
    self._read_fmt_chunk(chunk)
  File "D:\devsoft\Python\Python36\lib\wave.py", line 260, in _read_fmt_chunk
    raise Error('unknown format: %r' % (wFormatTag,))
wave.Error: unknown format: 6
'''