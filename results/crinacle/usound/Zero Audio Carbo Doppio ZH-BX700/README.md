# Zero Audio Carbo Doppio ZH-BX700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.7; 25 -1.9; 28 -2.1; 31 -2.3; 34 -2.4; 37 -2.6; 41 -2.8; 45 -3.0; 49 -3.2; 54 -3.4; 60 -3.8; 66 -4.1; 72 -4.5; 79 -4.8; 87 -5.3; 96 -5.8; 106 -6.3; 116 -6.6; 128 -7.0; 141 -7.4; 155 -7.6; 170 -7.9; 187 -8.1; 206 -8.1; 227 -8.2; 249 -8.2; 274 -8.1; 302 -8.1; 332 -7.9; 365 -7.7; 402 -7.6; 442 -7.4; 486 -7.2; 535 -7.0; 588 -6.7; 647 -6.4; 712 -6.1; 783 -5.8; 861 -5.5; 947 -5.5; 1042 -5.9; 1146 -6.7; 1261 -7.5; 1387 -8.0; 1526 -8.1; 1678 -8.0; 1846 -8.1; 2031 -8.6; 2234 -9.2; 2457 -8.3; 2703 -6.3; 2973 -4.6; 3270 -2.7; 3597 -1.1; 3957 -0.5; 4353 -1.2; 4788 -4.3; 5267 -9.6; 5793 -6.6; 6373 -1.6; 7010 -3.9; 7711 -6.3; 8482 -7.8; 9330 -6.5; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zero Audio Carbo Doppio ZH-BX700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zero Audio Carbo Doppio ZH-BX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.19 | 4.8 dB  |
| Peaking | 52 Hz    | 1.95 | 2.5 dB  |
| Peaking | 2140 Hz  | 1.68 | -3.2 dB |
| Peaking | 3758 Hz  | 2.56 | 7.0 dB  |
| Peaking | 22050 Hz | 2.37 | 1.2 dB  |
| Peaking | 246 Hz   | 0.94 | -2.0 dB |
| Peaking | 871 Hz   | 3.29 | 1.5 dB  |
| Peaking | 5410 Hz  | 7.41 | -6.8 dB |
| Peaking | 6429 Hz  | 3.62 | 5.2 dB  |
| Peaking | 8179 Hz  | 4.09 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Zero%20Audio%20Carbo%20Doppio%20ZH-BX700/Zero%20Audio%20Carbo%20Doppio%20ZH-BX700.png)