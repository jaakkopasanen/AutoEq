# HiSoundAudio BA-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.1; 25 -2.2; 28 -2.2; 31 -2.3; 34 -2.5; 37 -2.6; 41 -2.7; 45 -2.9; 49 -3.1; 54 -3.3; 60 -3.7; 66 -4.0; 72 -4.3; 79 -4.7; 87 -5.1; 96 -5.6; 106 -5.9; 116 -6.1; 128 -6.5; 141 -6.8; 155 -7.0; 170 -7.2; 187 -7.3; 206 -7.5; 227 -7.3; 249 -7.4; 274 -7.3; 302 -7.2; 332 -7.1; 365 -6.9; 402 -6.7; 442 -6.4; 486 -6.3; 535 -6.0; 588 -5.5; 647 -5.3; 712 -5.3; 783 -5.0; 861 -5.2; 947 -5.3; 1042 -5.6; 1146 -5.8; 1261 -6.1; 1387 -6.6; 1526 -7.2; 1678 -7.5; 1846 -7.0; 2031 -5.5; 2234 -3.2; 2457 -1.5; 2703 -1.9; 2973 -3.8; 3270 -6.1; 3597 -5.5; 3957 -4.9; 4353 -6.9; 4788 -8.8; 5267 -7.6; 5793 -3.4; 6373 -0.5; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio BA-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio BA-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 1.08 | 3.7 dB  |
| Peaking | 1713 Hz  | 2.04 | -2.6 dB |
| Peaking | 2490 Hz  | 3.6  | 5.1 dB  |
| Peaking | 4930 Hz  | 4.53 | -4.5 dB |
| Peaking | 6363 Hz  | 4.96 | 5.8 dB  |
| Peaking | 61 Hz    | 1.43 | 1.3 dB  |
| Peaking | 223 Hz   | 0.59 | -2.2 dB |
| Peaking | 607 Hz   | 4    | 0.4 dB  |
| Peaking | 824 Hz   | 2.09 | 0.9 dB  |
| Peaking | 22050 Hz | 1.74 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20BA-100/HiSoundAudio%20BA-100.png)