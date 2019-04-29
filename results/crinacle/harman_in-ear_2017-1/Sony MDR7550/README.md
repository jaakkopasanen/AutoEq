# Sony MDR7550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.2; 25 -2.6; 28 -3.0; 31 -3.4; 34 -3.6; 37 -3.9; 41 -4.2; 45 -4.5; 49 -4.7; 54 -5.0; 60 -5.3; 66 -5.7; 72 -6.1; 79 -6.6; 87 -7.1; 96 -7.5; 106 -7.9; 116 -8.4; 128 -8.8; 141 -9.1; 155 -9.5; 170 -9.7; 187 -9.9; 206 -10.1; 227 -10.1; 249 -10.2; 274 -10.3; 302 -10.2; 332 -10.0; 365 -9.8; 402 -9.7; 442 -9.5; 486 -9.3; 535 -9.0; 588 -8.7; 647 -8.3; 712 -7.8; 783 -7.3; 861 -7.5; 947 -7.6; 1042 -7.5; 1146 -7.9; 1261 -8.2; 1387 -8.2; 1526 -8.3; 1678 -8.2; 1846 -7.6; 2031 -6.3; 2234 -4.4; 2457 -2.2; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.2; 5267 -7.6; 5793 -7.8; 6373 -2.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -10.2; 18182 -16.9; 20000 -13.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR7550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.19 | 4.7 dB   |
| Peaking | 232 Hz   | 0.28 | -3.9 dB  |
| Peaking | 3423 Hz  | 1.57 | 7.3 dB   |
| Peaking | 15458 Hz | 1.04 | 5.8 dB   |
| Peaking | 18446 Hz | 0.72 | -13.0 dB |
| Peaking | 1693 Hz  | 2.76 | -2.2 dB  |
| Peaking | 2593 Hz  | 6.24 | 2.5 dB   |
| Peaking | 4582 Hz  | 5.76 | 4.2 dB   |
| Peaking | 5511 Hz  | 3.62 | -5.7 dB  |
| Peaking | 6540 Hz  | 5.97 | 5.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MDR7550/Sony%20MDR7550.png)