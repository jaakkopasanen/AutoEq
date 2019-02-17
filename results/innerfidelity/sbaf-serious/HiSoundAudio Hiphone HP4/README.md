# HiSoundAudio Hiphone HP4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.5; 23 -16.5; 25 -16.6; 28 -16.6; 31 -16.7; 34 -16.7; 37 -16.8; 41 -16.8; 45 -16.9; 49 -16.9; 54 -17.0; 60 -17.1; 66 -17.3; 72 -17.4; 79 -17.6; 87 -17.7; 96 -17.9; 106 -17.8; 116 -17.7; 128 -17.7; 141 -17.5; 155 -17.3; 170 -17.0; 187 -16.6; 206 -16.2; 227 -15.7; 249 -15.2; 274 -14.5; 302 -13.9; 332 -13.2; 365 -12.5; 402 -11.8; 442 -11.0; 486 -10.4; 535 -9.7; 588 -8.7; 647 -8.1; 712 -7.5; 783 -6.7; 861 -6.6; 947 -6.5; 1042 -6.4; 1146 -6.4; 1261 -6.1; 1387 -5.8; 1526 -5.3; 1678 -4.9; 1846 -4.3; 2031 -3.8; 2234 -5.4; 2457 -4.7; 2703 -3.3; 2973 -1.6; 3270 -0.7; 3597 -0.5; 3957 -1.5; 4353 -3.8; 4788 -5.0; 5267 -5.7; 5793 -7.7; 6373 -11.3; 7010 -9.3; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.3; 18182 -7.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio Hiphone HP4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Hiphone HP4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.2  | -9.6 dB |
| Peaking | 144 Hz   | 0.65 | -6.0 dB |
| Peaking | 307 Hz   | 1.14 | -3.2 dB |
| Peaking | 3413 Hz  | 1.44 | 6.0 dB  |
| Peaking | 6449 Hz  | 4.51 | -6.1 dB |
| Peaking | 489 Hz   | 5.45 | -0.6 dB |
| Peaking | 2179 Hz  | 1.15 | 2.2 dB  |
| Peaking | 2420 Hz  | 3.12 | -3.3 dB |
| Peaking | 4592 Hz  | 5.94 | -1.2 dB |
| Peaking | 17397 Hz | 3.62 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.2 dB |
| Peaking | 62 Hz    | 1.41 | -7.6 dB  |
| Peaking | 125 Hz   | 1.41 | -9.2 dB  |
| Peaking | 250 Hz   | 1.41 | -7.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Hiphone%20HP4/HiSoundAudio%20Hiphone%20HP4.png)