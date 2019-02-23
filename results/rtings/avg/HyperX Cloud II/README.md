# HyperX Cloud II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.4; 25 -6.8; 28 -7.3; 31 -7.7; 34 -7.9; 37 -8.1; 41 -8.2; 45 -8.2; 49 -8.2; 54 -8.1; 60 -8.2; 66 -8.3; 72 -8.5; 79 -8.7; 87 -9.1; 96 -9.4; 106 -9.8; 116 -10.1; 128 -10.2; 141 -9.9; 155 -9.7; 170 -9.4; 187 -8.7; 206 -7.9; 227 -7.1; 249 -6.4; 274 -6.0; 302 -5.9; 332 -6.0; 365 -6.1; 402 -6.0; 442 -6.0; 486 -6.1; 535 -6.2; 588 -6.1; 647 -5.9; 712 -5.6; 783 -5.2; 861 -4.9; 947 -3.9; 1042 -3.2; 1146 -3.6; 1261 -4.2; 1387 -4.8; 1526 -5.5; 1678 -6.6; 1846 -7.6; 2031 -8.7; 2234 -8.8; 2457 -7.5; 2703 -6.3; 2973 -5.6; 3270 -4.9; 3597 -2.2; 3957 -0.5; 4353 -0.6; 4788 -6.9; 5267 -6.6; 5793 -6.3; 6373 -8.2; 7010 -9.1; 7711 -10.3; 8482 -13.1; 9330 -13.5; 10263 -8.8; 11289 -6.5; 12418 -6.6; 13660 -10.7; 15026 -12.1; 16529 -10.3; 18182 -10.5; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 115 Hz   | 1.07 | -3.8 dB |
| Peaking | 1048 Hz  | 2.54 | 3.5 dB  |
| Peaking | 4002 Hz  | 4.71 | 7.4 dB  |
| Peaking | 8727 Hz  | 3.62 | -7.0 dB |
| Peaking | 19803 Hz | 0.27 | -5.4 dB |
| Peaking | 40 Hz    | 1.92 | -1.3 dB |
| Peaking | 311 Hz   | 2.05 | 1.2 dB  |
| Peaking | 2129 Hz  | 4.73 | -3.1 dB |
| Peaking | 11851 Hz | 3.55 | 3.3 dB  |
| Peaking | 14462 Hz | 3.43 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20II/HyperX%20Cloud%20II.png)