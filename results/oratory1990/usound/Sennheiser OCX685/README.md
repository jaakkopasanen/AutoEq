# Sennheiser OCX685
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.2; 25 -2.5; 28 -2.8; 31 -3.1; 34 -3.3; 37 -3.5; 41 -3.7; 45 -4.0; 49 -4.2; 54 -4.5; 60 -4.8; 66 -5.2; 72 -5.5; 79 -5.9; 87 -6.3; 96 -6.7; 106 -7.1; 116 -7.4; 128 -7.7; 141 -7.9; 155 -8.0; 170 -8.1; 187 -8.1; 206 -7.9; 227 -7.7; 249 -7.5; 274 -7.2; 302 -6.8; 332 -6.4; 365 -5.9; 402 -5.4; 442 -4.9; 486 -4.4; 535 -3.8; 588 -3.3; 647 -2.7; 712 -2.1; 783 -1.7; 861 -1.5; 947 -1.5; 1042 -1.8; 1146 -2.2; 1261 -2.7; 1387 -2.9; 1526 -3.0; 1678 -3.0; 1846 -3.0; 2031 -3.3; 2234 -3.9; 2457 -4.8; 2703 -5.3; 2973 -5.2; 3270 -4.5; 3597 -4.0; 3957 -4.2; 4353 -5.5; 4788 -8.5; 5267 -9.2; 5793 -5.1; 6373 -0.5; 7010 -2.1; 7711 -4.4; 8482 -4.6; 9330 -6.2; 10263 -5.2; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser OCX685 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser OCX685 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.27 | 3.1 dB  |
| Peaking | 177 Hz  | 0.52 | -3.8 dB |
| Peaking | 863 Hz  | 0.85 | 3.6 dB  |
| Peaking | 5136 Hz | 5    | -5.9 dB |
| Peaking | 6505 Hz | 6.17 | 5.6 dB  |
| Peaking | 1982 Hz | 3.46 | 1.1 dB  |
| Peaking | 2739 Hz | 2.15 | -1.4 dB |
| Peaking | 3694 Hz | 4.07 | 1.4 dB  |
| Peaking | 9629 Hz | 7.86 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20OCX685/Sennheiser%20OCX685.png)