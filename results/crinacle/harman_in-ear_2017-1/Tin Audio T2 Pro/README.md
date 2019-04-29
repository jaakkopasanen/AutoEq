# Tin Audio T2 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.0; 49 -1.4; 54 -1.8; 60 -2.3; 66 -2.8; 72 -3.2; 79 -3.8; 87 -4.4; 96 -5.0; 106 -5.7; 116 -6.3; 128 -6.8; 141 -7.4; 155 -7.9; 170 -8.2; 187 -8.6; 206 -8.9; 227 -9.1; 249 -9.3; 274 -9.3; 302 -9.2; 332 -9.1; 365 -8.9; 402 -8.8; 442 -8.5; 486 -8.2; 535 -7.8; 588 -7.3; 647 -6.8; 712 -6.2; 783 -5.7; 861 -5.2; 947 -4.9; 1042 -5.0; 1146 -5.4; 1261 -5.5; 1387 -5.4; 1526 -5.1; 1678 -4.7; 1846 -4.4; 2031 -4.1; 2234 -3.7; 2457 -3.4; 2703 -2.9; 2973 -1.9; 3270 -1.2; 3597 -1.3; 3957 -2.1; 4353 -3.6; 4788 -5.6; 5267 -6.1; 5793 -4.3; 6373 -3.4; 7010 -6.6; 7711 -12.2; 8482 -14.6; 9330 -13.9; 10263 -9.8; 11289 -6.5; 12418 -7.1; 13660 -15.5; 15026 -21.3; 16529 -22.4; 18182 -23.9; 20000 -23.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.38 | 6.4 dB   |
| Peaking | 246 Hz   | 0.54 | -3.7 dB  |
| Peaking | 8657 Hz  | 2.34 | -16.4 dB |
| Peaking | 9885 Hz  | 0.32 | 25.0 dB  |
| Peaking | 16791 Hz | 0.24 | -31.0 dB |
| Peaking | 3659 Hz  | 1.75 | 6.6 dB   |
| Peaking | 4683 Hz  | 0.89 | -5.7 dB  |
| Peaking | 6333 Hz  | 3.97 | 5.3 dB   |
| Peaking | 12254 Hz | 3.63 | 4.4 dB   |
| Peaking | 14402 Hz | 4.05 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB   |
| Peaking | 62 Hz    | 1.41 | 3.3 dB   |
| Peaking | 125 Hz   | 1.41 | -0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 16000 Hz | 1.41 | -20.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Tin%20Audio%20T2%20Pro/Tin%20Audio%20T2%20Pro.png)