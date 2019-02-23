# MrSpeakers Ether C Flow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -7.7; 25 -7.5; 28 -7.0; 31 -6.3; 34 -5.4; 37 -4.3; 41 -4.2; 45 -6.2; 49 -7.9; 54 -6.6; 60 -4.6; 66 -7.1; 72 -8.3; 79 -8.1; 87 -8.6; 96 -9.0; 106 -8.8; 116 -8.3; 128 -7.6; 141 -7.3; 155 -7.3; 170 -7.5; 187 -8.1; 206 -8.6; 227 -9.2; 249 -9.5; 274 -9.6; 302 -9.4; 332 -8.9; 365 -8.4; 402 -7.9; 442 -7.6; 486 -7.0; 535 -7.2; 588 -7.5; 647 -8.4; 712 -9.9; 783 -10.4; 861 -9.7; 947 -9.2; 1042 -8.7; 1146 -8.5; 1261 -9.1; 1387 -8.6; 1526 -8.4; 1678 -7.5; 1846 -6.4; 2031 -5.6; 2234 -5.4; 2457 -4.6; 2703 -4.8; 2973 -3.5; 3270 -1.7; 3597 -1.3; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -2.1; 5793 -4.3; 6373 -6.3; 7010 -6.7; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.1; 13660 -10.9; 15026 -7.1; 16529 -6.5; 18182 -6.5; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether C Flow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 96 Hz    | 2.62 | -2.5 dB |
| Peaking | 264 Hz   | 1.88 | -3.0 dB |
| Peaking | 936 Hz   | 1.13 | -3.3 dB |
| Peaking | 4031 Hz  | 1.65 | 6.7 dB  |
| Peaking | 13586 Hz | 3.9  | -4.8 dB |
| Peaking | 20 Hz    | 1.07 | -1.4 dB |
| Peaking | 38 Hz    | 4.39 | 3.2 dB  |
| Peaking | 5250 Hz  | 3.54 | 3.3 dB  |
| Peaking | 6101 Hz  | 1.15 | -3.7 dB |
| Peaking | 6527 Hz  | 0.49 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Ether%20C%20Flow/MrSpeakers%20Ether%20C%20Flow.png)