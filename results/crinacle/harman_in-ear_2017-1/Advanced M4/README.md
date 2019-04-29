# Advanced M4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.0; 25 -4.1; 28 -4.3; 31 -4.4; 34 -4.5; 37 -4.6; 41 -4.7; 45 -4.9; 49 -5.0; 54 -5.2; 60 -5.5; 66 -5.8; 72 -6.1; 79 -6.5; 87 -6.8; 96 -7.2; 106 -7.5; 116 -7.8; 128 -8.0; 141 -8.2; 155 -8.4; 170 -8.4; 187 -8.4; 206 -8.3; 227 -8.1; 249 -7.8; 274 -7.6; 302 -7.2; 332 -6.7; 365 -6.1; 402 -5.7; 442 -5.3; 486 -4.7; 535 -4.2; 588 -3.6; 647 -3.0; 712 -2.4; 783 -1.8; 861 -1.4; 947 -1.2; 1042 -1.4; 1146 -2.0; 1261 -2.4; 1387 -2.4; 1526 -2.0; 1678 -1.5; 1846 -1.0; 2031 -0.6; 2234 -0.5; 2457 -1.0; 2703 -2.0; 2973 -3.0; 3270 -3.0; 3597 -2.3; 3957 -1.4; 4353 -0.9; 4788 -1.0; 5267 -1.7; 5793 -4.1; 6373 -8.8; 7010 -7.3; 7711 -4.1; 8482 -4.5; 9330 -8.1; 10263 -6.6; 11289 -4.4; 12418 -4.4; 13660 -9.2; 15026 -21.0; 16529 -29.1; 18182 -31.8; 20000 -24.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced M4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced M4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 177 Hz   | 0.58 | -4.3 dB  |
| Peaking | 869 Hz   | 1.25 | 3.3 dB   |
| Peaking | 2119 Hz  | 1.89 | 3.6 dB   |
| Peaking | 4568 Hz  | 2.27 | 4.4 dB   |
| Peaking | 18229 Hz | 1.09 | -31.1 dB |
| Peaking | 18 Hz    | 0.93 | 0.8 dB   |
| Peaking | 6529 Hz  | 8.07 | -5.5 dB  |
| Peaking | 12721 Hz | 0.61 | 2.7 dB   |
| Peaking | 12879 Hz | 1.99 | 10.7 dB  |
| Peaking | 15664 Hz | 1.18 | -12.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB   |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 16000 Hz | 1.41 | -27.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20M4/Advanced%20M4.png)