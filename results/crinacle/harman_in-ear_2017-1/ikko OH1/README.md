# ikko OH1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.9; 25 -5.1; 28 -5.3; 31 -5.4; 34 -5.6; 37 -5.7; 41 -5.9; 45 -6.0; 49 -6.2; 54 -6.4; 60 -6.5; 66 -6.6; 72 -6.8; 79 -6.9; 87 -7.1; 96 -7.3; 106 -7.5; 116 -7.5; 128 -7.5; 141 -7.5; 155 -7.4; 170 -7.2; 187 -6.9; 206 -6.7; 227 -6.4; 249 -6.1; 274 -5.7; 302 -5.3; 332 -4.8; 365 -4.4; 402 -4.1; 442 -4.0; 486 -3.8; 535 -3.5; 588 -3.1; 647 -2.8; 712 -2.5; 783 -2.3; 861 -2.2; 947 -2.4; 1042 -2.8; 1146 -3.6; 1261 -4.3; 1387 -4.6; 1526 -4.7; 1678 -4.7; 1846 -4.8; 2031 -4.9; 2234 -4.7; 2457 -4.5; 2703 -3.8; 2973 -2.8; 3270 -2.0; 3597 -2.1; 3957 -3.3; 4353 -4.7; 4788 -4.9; 5267 -4.5; 5793 -1.9; 6373 -0.5; 7010 -2.7; 7711 -3.7; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -6.0; 15026 -12.5; 16529 -11.1; 18182 -5.0; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ikko OH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ikko OH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 69 Hz    | 0.61 | -2.5 dB  |
| Peaking | 159 Hz   | 1.2  | -2.5 dB  |
| Peaking | 6347 Hz  | 5.78 | 4.0 dB   |
| Peaking | 13027 Hz | 1.8  | 3.9 dB   |
| Peaking | 15404 Hz | 1.62 | -10.9 dB |
| Peaking | 849 Hz   | 0.95 | 5.1 dB   |
| Peaking | 1089 Hz  | 0.53 | -3.5 dB  |
| Peaking | 3402 Hz  | 2.58 | 2.9 dB   |
| Peaking | 4659 Hz  | 4.33 | -1.7 dB  |
| Peaking | 19831 Hz | 3.81 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -8.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/ikko%20OH1/ikko%20OH1.png)