# MrSpeakers Ether Flow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -1.8; 25 -1.7; 28 -1.3; 31 -0.8; 34 -0.5; 37 -0.5; 41 -1.1; 45 -2.2; 49 -2.9; 54 -2.6; 60 -3.2; 66 -3.9; 72 -4.5; 79 -4.7; 87 -5.7; 96 -6.2; 106 -6.5; 116 -6.6; 128 -6.7; 141 -6.8; 155 -6.6; 170 -6.8; 187 -7.0; 206 -6.9; 227 -6.6; 249 -6.3; 274 -5.8; 302 -5.2; 332 -4.7; 365 -4.2; 402 -3.5; 442 -2.9; 486 -2.6; 535 -2.4; 588 -1.9; 647 -1.6; 712 -2.2; 783 -2.2; 861 -2.5; 947 -2.7; 1042 -3.6; 1146 -1.4; 1261 -1.1; 1387 -1.6; 1526 -2.9; 1678 -3.7; 1846 -4.2; 2031 -4.0; 2234 -3.3; 2457 -2.7; 2703 -1.9; 2973 -2.6; 3270 -3.1; 3597 -3.3; 3957 -3.2; 4353 -3.8; 4788 -3.5; 5267 -2.5; 5793 -2.6; 6373 -5.0; 7010 -4.3; 7711 -3.6; 8482 -4.1; 9330 -4.0; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Ether Flow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether Flow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.8  | 3.8 dB  |
| Peaking | 156 Hz  | 0.46 | -3.6 dB |
| Peaking | 559 Hz  | 1.08 | 3.0 dB  |
| Peaking | 1259 Hz | 5.04 | 2.8 dB  |
| Peaking | 2741 Hz | 4.11 | 1.9 dB  |
| Peaking | 769 Hz  | 4.49 | 0.2 dB  |
| Peaking | 1905 Hz | 6.55 | -0.9 dB |
| Peaking | 5667 Hz | 4.15 | 2.0 dB  |
| Peaking | 6369 Hz | 6.83 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20Flow/MrSpeakers%20Ether%20Flow.png)