# Jomo Flamenco Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.7; 25 -6.0; 28 -6.4; 31 -6.8; 34 -7.1; 37 -7.4; 41 -7.7; 45 -7.9; 49 -8.2; 54 -8.5; 60 -8.8; 66 -9.2; 72 -9.6; 79 -10.0; 87 -10.4; 96 -10.9; 106 -11.3; 116 -11.6; 128 -11.9; 141 -12.2; 155 -12.4; 170 -12.6; 187 -12.6; 206 -12.6; 227 -12.5; 249 -12.3; 274 -12.1; 302 -11.8; 332 -11.4; 365 -10.9; 402 -10.4; 442 -9.9; 486 -9.3; 535 -8.6; 588 -7.9; 647 -7.0; 712 -6.0; 783 -5.0; 861 -4.0; 947 -3.3; 1042 -3.0; 1146 -3.2; 1261 -3.4; 1387 -3.4; 1526 -3.2; 1678 -3.1; 1846 -3.5; 2031 -4.2; 2234 -4.7; 2457 -4.2; 2703 -3.0; 2973 -2.5; 3270 -3.4; 3597 -4.2; 3957 -1.8; 4353 -0.5; 4788 -0.6; 5267 -4.5; 5793 -4.2; 6373 -4.4; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.4; 15026 -24.3; 16529 -28.9; 18182 -24.3; 20000 -15.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 208 Hz   | 0.41 | -6.4 dB  |
| Peaking | 1027 Hz  | 1.04 | 4.3 dB   |
| Peaking | 5028 Hz  | 0.61 | 8.1 dB   |
| Peaking | 12552 Hz | 1.17 | 16.5 dB  |
| Peaking | 16052 Hz | 0.57 | -29.9 dB |
| Peaking | 18 Hz    | 1.72 | 1.6 dB   |
| Peaking | 3603 Hz  | 6.46 | -2.8 dB  |
| Peaking | 4615 Hz  | 2.35 | 2.9 dB   |
| Peaking | 5376 Hz  | 6.4  | -3.1 dB  |
| Peaking | 5423 Hz  | 4.63 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -23.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Flamenco%20Bass/Jomo%20Flamenco%20Bass.png)