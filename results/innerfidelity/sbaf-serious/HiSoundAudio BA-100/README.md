# HiSoundAudio BA-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.1; 25 -2.1; 28 -2.2; 31 -2.3; 34 -2.4; 37 -2.6; 41 -2.7; 45 -2.9; 49 -3.1; 54 -3.3; 60 -3.7; 66 -4.0; 72 -4.3; 79 -4.7; 87 -5.1; 96 -5.6; 106 -5.9; 116 -6.1; 128 -6.5; 141 -6.8; 155 -7.0; 170 -7.2; 187 -7.3; 206 -7.4; 227 -7.3; 249 -7.4; 274 -7.3; 302 -7.2; 332 -7.1; 365 -6.9; 402 -6.7; 442 -6.4; 486 -6.3; 535 -6.0; 588 -5.5; 647 -5.3; 712 -5.3; 783 -5.0; 861 -5.1; 947 -5.3; 1042 -5.6; 1146 -5.8; 1261 -6.1; 1387 -6.6; 1526 -7.2; 1678 -7.4; 1846 -6.9; 2031 -5.5; 2234 -3.2; 2457 -1.5; 2703 -1.8; 2973 -3.8; 3270 -6.0; 3597 -5.4; 3957 -4.9; 4353 -6.9; 4788 -8.8; 5267 -7.6; 5793 -3.4; 6373 -0.5; 7010 -3.0; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio BA-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio BA-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.03 | 3.8 dB  |
| Peaking | 1702 Hz | 2.5  | -2.5 dB |
| Peaking | 2501 Hz | 3.64 | 5.0 dB  |
| Peaking | 4930 Hz | 4.66 | -4.4 dB |
| Peaking | 6350 Hz | 4.97 | 5.8 dB  |
| Peaking | 61 Hz   | 1.47 | 1.2 dB  |
| Peaking | 220 Hz  | 0.62 | -2.1 dB |
| Peaking | 612 Hz  | 4.94 | 0.5 dB  |
| Peaking | 811 Hz  | 2.45 | 0.9 dB  |
| Peaking | 8101 Hz | 5.64 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20BA-100/HiSoundAudio%20BA-100.png)