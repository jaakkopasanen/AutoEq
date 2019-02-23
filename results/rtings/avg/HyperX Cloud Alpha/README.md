# HyperX Cloud Alpha
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.0; 25 -7.0; 28 -7.1; 31 -7.2; 34 -7.2; 37 -7.1; 41 -7.0; 45 -6.9; 49 -6.9; 54 -6.8; 60 -6.7; 66 -6.9; 72 -7.0; 79 -7.2; 87 -7.5; 96 -7.8; 106 -8.2; 116 -8.4; 128 -8.7; 141 -8.8; 155 -8.8; 170 -8.8; 187 -8.6; 206 -8.5; 227 -8.3; 249 -8.1; 274 -8.1; 302 -8.3; 332 -8.2; 365 -7.8; 402 -7.4; 442 -7.0; 486 -6.8; 535 -6.4; 588 -5.9; 647 -5.5; 712 -5.2; 783 -5.1; 861 -5.0; 947 -5.0; 1042 -5.0; 1146 -5.3; 1261 -5.7; 1387 -6.4; 1526 -7.2; 1678 -8.0; 1846 -8.6; 2031 -8.7; 2234 -7.8; 2457 -6.8; 2703 -6.3; 2973 -6.0; 3270 -6.0; 3597 -4.7; 3957 -2.6; 4353 -0.8; 4788 -0.5; 5267 -0.5; 5793 -3.3; 6373 -4.7; 7010 -5.3; 7711 -8.3; 8482 -10.2; 9330 -10.6; 10263 -9.1; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.8; 18182 -12.1; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Alpha GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 163 Hz   | 0.89 | -2.5 dB |
| Peaking | 1982 Hz  | 3.82 | -2.9 dB |
| Peaking | 4875 Hz  | 2.1  | 6.8 dB  |
| Peaking | 8900 Hz  | 3.08 | -5.2 dB |
| Peaking | 18106 Hz | 1.73 | -6.5 dB |
| Peaking | 28 Hz    | 1.8  | -0.6 dB |
| Peaking | 345 Hz   | 2.56 | -1.1 dB |
| Peaking | 1030 Hz  | 0.97 | 2.9 dB  |
| Peaking | 1447 Hz  | 1    | -1.9 dB |
| Peaking | 14180 Hz | 2.14 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Alpha/HyperX%20Cloud%20Alpha.png)