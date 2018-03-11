from scipy import signal
import numpy as np


def simple():
    x = np.array([1, 2, 1, 1, 2, 2, 1, 1], dtype='float32')
    h = np.array([2, 1], dtype='float32')

    y = signal.convolve(h, x)
    _y = signal.convolve(x, h)
    print()
    print(y, 'Convolution h*x')
    print(_y, 'Convolution x*h')

    _x, _ = signal.deconvolve(y, h)
    print()
    print(x, 'Original signal')
    print(_x, 'Recovered signal')

    _h, _ = signal.deconvolve(y, x)
    print()
    print(h, 'Original impulse response')
    print(_h, 'Recovered impulse response')


def real():
    sweep = np.array([1, 2, 1, 1, 2, 2], dtype='float32')
    music = np.array([2, 1, 2, 2, 1, 1], dtype='float32')
    speakers = np.array([1, 2], dtype='float32')
    room = np.array([2, 1], dtype='float32')
    head = np.array([1, 3], dtype='float32')
    pinna = np.array([3, 1], dtype='float32')
    ear_canal = np.array([2, 3], dtype='float32')
    headphone = np.array([3, 2], dtype='float32')
    iem = np.array([1, 4], dtype='float32')
    ciem = np.array([4, 1], dtype='float32')

    # Finding personal room impulse response
    prir_record = sweep
    for h in [speakers, room, head, pinna]:
        prir_record = signal.convolve(prir_record, h)
    prir, _ = signal.deconvolve(prir_record, sweep)

    # Finding personal headphone impulse response
    phpir_record = sweep
    for h in [headphone, pinna]:
        phpir_record = signal.convolve(phpir_record, h)
    phpir, _ = signal.deconvolve(phpir_record, sweep)

    # Personal ear canal impulse response is taken as given, measured by Hefio
    pecir = ear_canal

    # Listening to music on speakers
    music_speakers = music
    for h in [speakers, room, head, pinna, ear_canal]:
        music_speakers = signal.convolve(music_speakers, h)
    print(music_speakers, 'Music on speakers')

    # Listening to music on IEMs without correction
    music_iem_raw = music
    for h in [iem, ear_canal]:
        music_iem_raw = signal.convolve(music_iem_raw, h)
    print(music_iem_raw, 'Music on IEM without correction')

    # Listening to music on IEMs with correction
    music_iem_corrected = music_iem_raw
    music_iem_corrected, _ = signal.deconvolve(music_iem_corrected, iem)
    music_iem_corrected = signal.convolve(music_iem_corrected, prir)
    print(music_iem_corrected, 'Music on IEM with correction')

    # Listening to music on CIEMs without correction
    music_ciem_raw = music
    for h in [ciem]:
        music_ciem_raw = signal.convolve(music_ciem_raw, h)
    print(music_ciem_raw, 'Music on CIEM without correction')

    # Listening to music on IEMs with correction
    music_ciem_corrected = music_ciem_raw
    music_ciem_corrected, _ = signal.deconvolve(music_ciem_corrected, ciem)
    music_ciem_corrected = signal.convolve(music_ciem_corrected, prir)
    music_ciem_corrected = signal.convolve(music_ciem_corrected, pecir)
    print(music_ciem_corrected, 'Music on CIEM with correction')

    # Listening to music on headphones without correction
    music_hp_raw = music
    for h in [headphone, pinna, ear_canal]:
        music_hp_raw = signal.convolve(music_hp_raw, h)
    print(music_hp_raw, 'Music on headphones without correction')

    # Listening to music on headphones with correction
    music_hp_corrected = music_hp_raw
    music_hp_corrected = signal.convolve(music_hp_corrected, prir)
    music_hp_corrected, _ = signal.deconvolve(music_hp_corrected, phpir)
    print(music_hp_corrected, 'Music on headphones with correction')

    # Listening to music on headphones with combo ir correction
    music_hp_corrected = music_hp_raw
    combo_ir, rem = signal.deconvolve(prir, phpir)
    music_hp_corrected = signal.convolve(music_hp_corrected, combo_ir)
    print(music_hp_corrected.astype('int').astype('float'), 'Music on headphones with combo ir correction')


if __name__ == '__main__':
    real()
