# Spiral Ears SE5U sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.7; 34 -2.3; 37 -2.8; 41 -3.5; 45 -4.1; 49 -4.7; 54 -5.2; 60 -5.8; 66 -6.3; 72 -6.8; 79 -7.3; 87 -7.8; 96 -8.2; 106 -8.8; 116 -9.2; 128 -9.5; 141 -9.7; 155 -9.8; 170 -9.9; 187 -9.9; 206 -10.0; 227 -9.7; 249 -9.5; 274 -9.3; 302 -9.0; 332 -8.6; 365 -8.2; 402 -7.8; 442 -7.4; 486 -6.9; 535 -6.5; 588 -6.0; 647 -5.5; 712 -4.9; 783 -4.4; 861 -4.1; 947 -4.0; 1042 -4.4; 1146 -5.3; 1261 -6.5; 1387 -7.6; 1526 -8.7; 1678 -10.1; 1846 -12.5; 2031 -12.6; 2234 -9.7; 2457 -8.2; 2703 -7.6; 2973 -8.1; 3270 -4.8; 3597 -0.5; 3957 -0.5; 4353 -3.4; 4788 -5.0; 5267 -0.9; 5793 -1.2; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -8.5; 10263 -6.8; 11289 -6.6; 12418 -9.7; 13660 -13.0; 15026 -14.0; 16529 -11.8; 18182 -6.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spiral Ears SE5U sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spiral Ears SE5U sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.72 | 6.7 dB  |
| Peaking | 1933 Hz  | 3.47 | -7.0 dB |
| Peaking | 3743 Hz  | 5.08 | 6.8 dB  |
| Peaking | 5850 Hz  | 2.99 | 5.8 dB  |
| Peaking | 14965 Hz | 1.58 | -8.3 dB |
| Peaking | 46 Hz    | 1.58 | 1.8 dB  |
| Peaking | 178 Hz   | 0.62 | -3.7 dB |
| Peaking | 859 Hz   | 1.78 | 3.2 dB  |
| Peaking | 2998 Hz  | 9.89 | -2.7 dB |
| Peaking | 16494 Hz | 6.46 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -8.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Spiral%20Ears%20SE5U%20sample%201/Spiral%20Ears%20SE5U%20sample%201.png)