# Sennheiser RS 175
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.9; 23 -14.8; 25 -14.8; 28 -14.5; 31 -14.1; 34 -13.7; 37 -13.2; 41 -12.6; 45 -12.1; 49 -11.5; 54 -10.9; 60 -10.6; 66 -10.7; 72 -10.9; 79 -11.2; 87 -11.5; 96 -11.6; 106 -11.6; 116 -11.2; 128 -10.6; 141 -9.6; 155 -8.4; 170 -6.9; 187 -5.3; 206 -3.8; 227 -2.7; 249 -2.1; 274 -2.2; 302 -2.5; 332 -2.8; 365 -2.4; 402 -1.1; 442 -0.5; 486 -1.0; 535 -1.7; 588 -2.3; 647 -2.9; 712 -3.5; 783 -4.1; 861 -4.5; 947 -4.9; 1042 -5.2; 1146 -5.5; 1261 -5.8; 1387 -5.9; 1526 -5.4; 1678 -4.8; 1846 -4.2; 2031 -5.4; 2234 -8.8; 2457 -11.4; 2703 -12.6; 2973 -12.3; 3270 -10.6; 3597 -8.0; 3957 -7.4; 4353 -7.4; 4788 -6.6; 5267 -6.4; 5793 -7.1; 6373 -2.5; 7010 -3.0; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -7.5; 16529 -5.9; 18182 -5.5; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 175 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 175 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.48 | -8.3 dB |
| Peaking | 31 Hz    | 0.75 | -4.8 dB |
| Peaking | 114 Hz   | 0.95 | -7.1 dB |
| Peaking | 304 Hz   | 0.55 | 5.3 dB  |
| Peaking | 2819 Hz  | 2.73 | -8.0 dB |
| Peaking | 491 Hz   | 3.23 | 1.7 dB  |
| Peaking | 1481 Hz  | 0.29 | -0.8 dB |
| Peaking | 1861 Hz  | 4.74 | 3.3 dB  |
| Peaking | 6692 Hz  | 8.15 | 5.0 dB  |
| Peaking | 15581 Hz | 4.8  | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20175/Sennheiser%20RS%20175.png)