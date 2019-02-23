# Superlux HD 681
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.9; 25 -3.5; 28 -4.3; 31 -4.9; 34 -5.3; 37 -5.5; 41 -5.8; 45 -5.8; 49 -5.8; 54 -5.8; 60 -5.7; 66 -5.6; 72 -5.6; 79 -5.6; 87 -5.6; 96 -5.7; 106 -5.7; 116 -5.6; 128 -5.5; 141 -5.3; 155 -5.0; 170 -4.5; 187 -3.9; 206 -3.0; 227 -3.4; 249 -3.7; 274 -3.6; 302 -3.4; 332 -3.3; 365 -3.3; 402 -3.3; 442 -3.4; 486 -3.5; 535 -3.1; 588 -2.4; 647 -2.7; 712 -2.7; 783 -2.8; 861 -2.7; 947 -2.8; 1042 -2.8; 1146 -2.8; 1261 -2.8; 1387 -3.0; 1526 -3.6; 1678 -4.7; 1846 -6.8; 2031 -8.1; 2234 -8.2; 2457 -7.0; 2703 -5.8; 2973 -5.7; 3270 -5.8; 3597 -3.6; 3957 -0.5; 4353 -4.4; 4788 -9.2; 5267 -10.1; 5793 -7.7; 6373 -7.2; 7010 -7.5; 7711 -10.7; 8482 -12.9; 9330 -13.6; 10263 -13.3; 11289 -11.0; 12418 -8.2; 13660 -8.3; 15026 -8.6; 16529 -7.4; 18182 -8.1; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 3.11 | 2.5 dB  |
| Peaking | 2122 Hz  | 2.58 | -5.7 dB |
| Peaking | 4733 Hz  | 0.08 | 3.7 dB  |
| Peaking | 9336 Hz  | 1.6  | -7.7 dB |
| Peaking | 19339 Hz | 0.05 | -5.4 dB |
| Peaking | 103 Hz   | 0.57 | -0.9 dB |
| Peaking | 209 Hz   | 2.81 | 1.7 dB  |
| Peaking | 4036 Hz  | 6.28 | 7.1 dB  |
| Peaking | 4986 Hz  | 2.94 | -5.2 dB |
| Peaking | 6504 Hz  | 3.6  | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.0 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Superlux%20HD%20681/Superlux%20HD%20681.png)