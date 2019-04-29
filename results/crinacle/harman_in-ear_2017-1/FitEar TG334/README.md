# FitEar TG334
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.4; 25 -6.6; 28 -6.9; 31 -7.2; 34 -7.4; 37 -7.6; 41 -7.8; 45 -8.0; 49 -8.2; 54 -8.4; 60 -8.7; 66 -9.0; 72 -9.4; 79 -9.8; 87 -10.2; 96 -10.6; 106 -11.0; 116 -11.3; 128 -11.6; 141 -11.9; 155 -12.1; 170 -12.2; 187 -12.3; 206 -12.3; 227 -12.2; 249 -12.1; 274 -11.9; 302 -11.6; 332 -11.2; 365 -10.8; 402 -10.5; 442 -10.1; 486 -9.7; 535 -9.2; 588 -8.7; 647 -8.2; 712 -7.7; 783 -7.1; 861 -6.6; 947 -6.4; 1042 -6.6; 1146 -7.0; 1261 -7.3; 1387 -7.3; 1526 -6.8; 1678 -6.0; 1846 -4.8; 2031 -3.2; 2234 -2.0; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.8; 5793 -2.7; 6373 -4.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.3; 15026 -15.8; 16529 -10.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar TG334 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar TG334 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 111 Hz   | 0.66 | -2.5 dB  |
| Peaking | 254 Hz   | 0.57 | -4.7 dB  |
| Peaking | 1490 Hz  | 2.43 | -2.8 dB  |
| Peaking | 3323 Hz  | 0.72 | 6.9 dB   |
| Peaking | 15090 Hz | 2.8  | -10.5 dB |
| Peaking | 17 Hz    | 1.57 | 1.0 dB   |
| Peaking | 3447 Hz  | 5.34 | -0.8 dB  |
| Peaking | 5080 Hz  | 5.05 | 1.7 dB   |
| Peaking | 8215 Hz  | 2.96 | -1.6 dB  |
| Peaking | 12731 Hz | 7.1  | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -6.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20TG334/FitEar%20TG334.png)