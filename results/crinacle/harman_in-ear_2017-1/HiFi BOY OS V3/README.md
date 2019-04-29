# HiFi BOY OS V3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -9.0; 25 -9.2; 28 -9.4; 31 -9.5; 34 -9.6; 37 -9.7; 41 -9.8; 45 -10.0; 49 -10.1; 54 -10.3; 60 -10.5; 66 -10.7; 72 -10.9; 79 -11.2; 87 -11.5; 96 -11.8; 106 -12.1; 116 -12.4; 128 -12.6; 141 -12.7; 155 -12.7; 170 -12.8; 187 -12.7; 206 -12.6; 227 -12.4; 249 -12.1; 274 -11.9; 302 -11.4; 332 -10.9; 365 -10.4; 402 -9.9; 442 -9.4; 486 -8.7; 535 -8.2; 588 -7.6; 647 -7.0; 712 -6.2; 783 -5.5; 861 -4.9; 947 -4.6; 1042 -4.9; 1146 -6.2; 1261 -6.8; 1387 -6.3; 1526 -5.5; 1678 -4.5; 1846 -3.6; 2031 -2.7; 2234 -1.7; 2457 -1.1; 2703 -1.1; 2973 -1.3; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -2.4; 5267 -2.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.3; 16529 -17.3; 18182 -19.0; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFi BOY OS V3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFi BOY OS V3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 67 Hz    | 0.31 | -3.5 dB  |
| Peaking | 209 Hz   | 0.7  | -4.4 dB  |
| Peaking | 3198 Hz  | 0.85 | 6.1 dB   |
| Peaking | 6013 Hz  | 4.85 | 4.2 dB   |
| Peaking | 17831 Hz | 1.67 | -15.1 dB |
| Peaking | 922 Hz   | 2.57 | 2.3 dB   |
| Peaking | 1282 Hz  | 3.53 | -2.1 dB  |
| Peaking | 8252 Hz  | 6.11 | -3.1 dB  |
| Peaking | 14994 Hz | 1.84 | 3.9 dB   |
| Peaking | 16497 Hz | 3.47 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -8.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/HiFi%20BOY%20OS%20V3/HiFi%20BOY%20OS%20V3.png)