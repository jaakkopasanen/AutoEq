# Sony IER-M9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.3; 25 -6.6; 28 -7.0; 31 -7.2; 34 -7.4; 37 -7.6; 41 -7.9; 45 -8.1; 49 -8.2; 54 -8.4; 60 -8.6; 66 -8.8; 72 -8.9; 79 -9.1; 87 -9.3; 96 -9.5; 106 -9.7; 116 -9.8; 128 -9.8; 141 -9.9; 155 -9.8; 170 -9.7; 187 -9.6; 206 -9.4; 227 -9.1; 249 -8.9; 274 -8.6; 302 -8.4; 332 -8.1; 365 -7.9; 402 -7.6; 442 -7.3; 486 -7.1; 535 -6.7; 588 -6.4; 647 -6.0; 712 -5.6; 783 -5.2; 861 -4.8; 947 -4.7; 1042 -5.0; 1146 -5.6; 1261 -6.2; 1387 -6.5; 1526 -6.3; 1678 -5.8; 1846 -5.2; 2031 -4.5; 2234 -3.8; 2457 -2.7; 2703 -1.2; 2973 -1.7; 3270 -5.1; 3597 -6.6; 3957 -5.0; 4353 -4.3; 4788 -4.2; 5267 -2.5; 5793 -0.9; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -6.6; 13660 -9.1; 15026 -11.5; 16529 -13.5; 18182 -11.4; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 95 Hz    | 0.52 | -3.2 dB |
| Peaking | 219 Hz   | 0.93 | -1.9 dB |
| Peaking | 2696 Hz  | 3.89 | 5.0 dB  |
| Peaking | 6055 Hz  | 3.21 | 6.0 dB  |
| Peaking | 16725 Hz | 1.3  | -8.3 dB |
| Peaking | 912 Hz   | 2.71 | 1.6 dB  |
| Peaking | 1396 Hz  | 4.28 | -1.0 dB |
| Peaking | 3468 Hz  | 2.23 | 1.5 dB  |
| Peaking | 3507 Hz  | 5.99 | -3.6 dB |
| Peaking | 11651 Hz | 5.42 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -8.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20IER-M9/Sony%20IER-M9.png)