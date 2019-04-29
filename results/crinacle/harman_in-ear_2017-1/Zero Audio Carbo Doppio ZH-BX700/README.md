# Zero Audio Carbo Doppio ZH-BX700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -2.9; 25 -3.1; 28 -3.3; 31 -3.5; 34 -3.6; 37 -3.8; 41 -4.0; 45 -4.2; 49 -4.4; 54 -4.6; 60 -5.0; 66 -5.3; 72 -5.7; 79 -6.0; 87 -6.5; 96 -7.0; 106 -7.5; 116 -7.8; 128 -8.2; 141 -8.6; 155 -8.8; 170 -9.1; 187 -9.3; 206 -9.3; 227 -9.4; 249 -9.4; 274 -9.3; 302 -9.2; 332 -8.9; 365 -8.6; 402 -8.4; 442 -8.3; 486 -8.0; 535 -7.7; 588 -7.4; 647 -7.1; 712 -6.8; 783 -6.5; 861 -6.3; 947 -6.3; 1042 -6.8; 1146 -7.5; 1261 -8.1; 1387 -8.2; 1526 -8.1; 1678 -7.9; 1846 -7.9; 2031 -8.1; 2234 -8.1; 2457 -6.7; 2703 -4.3; 2973 -2.4; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.5; 5267 -8.8; 5793 -5.6; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.9; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zero Audio Carbo Doppio ZH-BX700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zero Audio Carbo Doppio ZH-BX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.3  | 3.7 dB  |
| Peaking | 206 Hz   | 0.64 | -3.3 dB |
| Peaking | 2130 Hz  | 1.33 | -3.7 dB |
| Peaking | 3494 Hz  | 1.56 | 7.8 dB  |
| Peaking | 19634 Hz | 1.6  | -4.3 dB |
| Peaking | 887 Hz   | 2.96 | 1.0 dB  |
| Peaking | 1288 Hz  | 4.58 | -1.0 dB |
| Peaking | 4552 Hz  | 5.46 | 3.6 dB  |
| Peaking | 5348 Hz  | 3.9  | -6.5 dB |
| Peaking | 6301 Hz  | 5.78 | 6.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Zero%20Audio%20Carbo%20Doppio%20ZH-BX700/Zero%20Audio%20Carbo%20Doppio%20ZH-BX700.png)