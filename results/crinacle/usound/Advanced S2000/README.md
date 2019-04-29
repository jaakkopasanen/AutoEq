# Advanced S2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.8; 25 -11.9; 28 -12.0; 31 -12.0; 34 -12.0; 37 -11.9; 41 -11.9; 45 -11.9; 49 -11.8; 54 -11.7; 60 -11.7; 66 -11.6; 72 -11.6; 79 -11.6; 87 -11.6; 96 -11.6; 106 -11.6; 116 -11.4; 128 -11.3; 141 -11.1; 155 -10.9; 170 -10.5; 187 -10.2; 206 -9.8; 227 -9.3; 249 -8.9; 274 -8.4; 302 -7.9; 332 -7.4; 365 -6.9; 402 -6.5; 442 -6.1; 486 -5.7; 535 -5.2; 588 -4.8; 647 -4.5; 712 -4.1; 783 -4.0; 861 -3.3; 947 -2.5; 1042 -3.4; 1146 -4.6; 1261 -5.8; 1387 -6.8; 1526 -7.4; 1678 -7.8; 1846 -8.5; 2031 -9.7; 2234 -10.9; 2457 -11.3; 2703 -9.7; 2973 -7.7; 3270 -6.5; 3597 -6.5; 3957 -8.1; 4353 -10.5; 4788 -7.6; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.7; 18182 -10.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced S2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced S2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.19 | -5.6 dB |
| Peaking | 809 Hz   | 0.98 | 3.8 dB  |
| Peaking | 2255 Hz  | 2.09 | -5.3 dB |
| Peaking | 4456 Hz  | 6.13 | -5.9 dB |
| Peaking | 5793 Hz  | 3.05 | 7.3 dB  |
| Peaking | 990 Hz   | 7.01 | 1.3 dB  |
| Peaking | 1418 Hz  | 4.24 | -1.1 dB |
| Peaking | 3328 Hz  | 7.13 | 1.3 dB  |
| Peaking | 8021 Hz  | 6    | -1.0 dB |
| Peaking | 18034 Hz | 1.87 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20S2000/Advanced%20S2000.png)