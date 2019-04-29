# FitEar TG334 sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.2; 25 -6.5; 28 -6.9; 31 -7.2; 34 -7.5; 37 -7.7; 41 -8.0; 45 -8.2; 49 -8.5; 54 -8.8; 60 -9.1; 66 -9.5; 72 -9.8; 79 -10.2; 87 -10.7; 96 -11.1; 106 -11.5; 116 -11.8; 128 -12.1; 141 -12.4; 155 -12.5; 170 -12.6; 187 -12.6; 206 -12.6; 227 -12.5; 249 -12.4; 274 -12.2; 302 -11.9; 332 -11.5; 365 -11.1; 402 -10.8; 442 -10.4; 486 -10.0; 535 -9.5; 588 -9.0; 647 -8.4; 712 -7.9; 783 -7.3; 861 -6.8; 947 -6.6; 1042 -6.7; 1146 -7.0; 1261 -7.3; 1387 -7.2; 1526 -6.7; 1678 -5.9; 1846 -4.7; 2031 -3.0; 2234 -1.7; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.0; 6373 -4.0; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.0; 15026 -13.2; 16529 -9.4; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar TG334 sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar TG334 sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 1.52 | 1.4 dB  |
| Peaking | 102 Hz   | 0.47 | -0.7 dB |
| Peaking | 203 Hz   | 0.42 | -5.7 dB |
| Peaking | 3605 Hz  | 0.88 | 7.0 dB  |
| Peaking | 15037 Hz | 2.66 | -7.5 dB |
| Peaking | 1531 Hz  | 1.69 | -4.1 dB |
| Peaking | 2389 Hz  | 0.59 | 3.7 dB  |
| Peaking | 3501 Hz  | 1.63 | -3.5 dB |
| Peaking | 5299 Hz  | 5.08 | 1.5 dB  |
| Peaking | 8085 Hz  | 2.71 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20TG334%20sample%203/FitEar%20TG334%20sample%203.png)