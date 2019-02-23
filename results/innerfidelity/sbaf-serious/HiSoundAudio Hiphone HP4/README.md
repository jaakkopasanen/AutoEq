# HiSoundAudio Hiphone HP4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.2; 23 -14.3; 25 -14.3; 28 -14.4; 31 -14.4; 34 -14.4; 37 -14.5; 41 -14.5; 45 -14.6; 49 -14.6; 54 -14.7; 60 -14.9; 66 -15.0; 72 -15.1; 79 -15.3; 87 -15.5; 96 -15.6; 106 -15.5; 116 -15.4; 128 -15.4; 141 -15.2; 155 -15.0; 170 -14.7; 187 -14.3; 206 -13.9; 227 -13.4; 249 -12.9; 274 -12.3; 302 -11.6; 332 -10.9; 365 -10.2; 402 -9.5; 442 -8.7; 486 -8.1; 535 -7.4; 588 -6.4; 647 -5.8; 712 -5.2; 783 -4.5; 861 -4.4; 947 -4.2; 1042 -4.1; 1146 -4.1; 1261 -3.8; 1387 -3.6; 1526 -3.0; 1678 -2.6; 1846 -2.0; 2031 -1.5; 2234 -3.1; 2457 -2.4; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -2.7; 5267 -3.4; 5793 -5.4; 6373 -9.0; 7010 -7.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio Hiphone HP4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Hiphone HP4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.31 | -6.4 dB |
| Peaking | 143 Hz  | 0.37 | -8.1 dB |
| Peaking | 1159 Hz | 0.46 | 3.8 dB  |
| Peaking | 3477 Hz | 1.66 | 5.3 dB  |
| Peaking | 1206 Hz | 3.92 | -0.7 dB |
| Peaking | 1932 Hz | 6.59 | 1.3 dB  |
| Peaking | 5093 Hz | 2.97 | 1.3 dB  |
| Peaking | 6407 Hz | 6.36 | -4.3 dB |
| Peaking | 9634 Hz | 1.69 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.1 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Hiphone%20HP4/HiSoundAudio%20Hiphone%20HP4.png)