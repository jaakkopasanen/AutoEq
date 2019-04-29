# Westone UM Pro 30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.5; 25 -7.7; 28 -7.9; 31 -8.0; 34 -8.2; 37 -8.3; 41 -8.4; 45 -8.5; 49 -8.7; 54 -8.9; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.1; 87 -10.4; 96 -10.8; 106 -11.2; 116 -11.5; 128 -11.8; 141 -12.0; 155 -12.2; 170 -12.3; 187 -12.4; 206 -12.4; 227 -12.2; 249 -12.1; 274 -11.9; 302 -11.7; 332 -11.4; 365 -11.1; 402 -10.7; 442 -10.4; 486 -9.9; 535 -9.5; 588 -9.0; 647 -8.5; 712 -8.0; 783 -7.4; 861 -6.9; 947 -6.7; 1042 -6.9; 1146 -7.6; 1261 -8.4; 1387 -8.8; 1526 -8.7; 1678 -8.0; 1846 -7.1; 2031 -5.5; 2234 -3.4; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -9.9; 9330 -7.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM Pro 30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM Pro 30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 64 Hz    | 0.11 | -0.7 dB |
| Peaking | 216 Hz   | 0.38 | -5.5 dB |
| Peaking | 1603 Hz  | 1.41 | -7.7 dB |
| Peaking | 3044 Hz  | 0.4  | 8.2 dB  |
| Peaking | 8595 Hz  | 3.1  | -7.0 dB |
| Peaking | 2095 Hz  | 4.89 | -1.5 dB |
| Peaking | 2451 Hz  | 2.41 | 1.7 dB  |
| Peaking | 3432 Hz  | 1.88 | -1.1 dB |
| Peaking | 6126 Hz  | 4.73 | 1.8 dB  |
| Peaking | 13013 Hz | 1.46 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Westone%20UM%20Pro%2030/Westone%20UM%20Pro%2030.png)