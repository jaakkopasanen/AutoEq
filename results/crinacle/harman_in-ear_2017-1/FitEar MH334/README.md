# FitEar MH334
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.1; 25 -5.5; 28 -5.9; 31 -6.3; 34 -6.6; 37 -6.8; 41 -7.1; 45 -7.4; 49 -7.6; 54 -7.9; 60 -8.2; 66 -8.6; 72 -9.0; 79 -9.4; 87 -9.8; 96 -10.3; 106 -10.7; 116 -11.0; 128 -11.4; 141 -11.7; 155 -11.9; 170 -12.0; 187 -12.1; 206 -12.1; 227 -12.1; 249 -12.0; 274 -11.9; 302 -11.6; 332 -11.3; 365 -10.9; 402 -10.6; 442 -10.3; 486 -9.9; 535 -9.4; 588 -8.9; 647 -8.4; 712 -7.8; 783 -7.2; 861 -6.8; 947 -6.5; 1042 -6.6; 1146 -7.1; 1261 -7.5; 1387 -7.6; 1526 -7.3; 1678 -6.8; 1846 -5.8; 2031 -4.4; 2234 -3.3; 2457 -2.6; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.7; 5793 -2.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.2; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -9.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar MH334 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar MH334 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.36 | 2.2 dB  |
| Peaking | 109 Hz   | 0.78 | -1.6 dB |
| Peaking | 237 Hz   | 0.53 | -5.1 dB |
| Peaking | 2952 Hz  | 2.03 | 4.8 dB  |
| Peaking | 4705 Hz  | 1.47 | 5.1 dB  |
| Peaking | 909 Hz   | 3.28 | 1.1 dB  |
| Peaking | 1420 Hz  | 3.51 | -1.5 dB |
| Peaking | 6462 Hz  | 6.39 | 4.1 dB  |
| Peaking | 7734 Hz  | 1.42 | -1.6 dB |
| Peaking | 14808 Hz | 5.51 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20MH334/FitEar%20MH334.png)