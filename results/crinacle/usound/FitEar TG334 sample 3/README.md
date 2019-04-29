# FitEar TG334 sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.0; 25 -5.3; 28 -5.7; 31 -6.0; 34 -6.3; 37 -6.5; 41 -6.8; 45 -7.1; 49 -7.3; 54 -7.6; 60 -8.0; 66 -8.3; 72 -8.7; 79 -9.1; 87 -9.5; 96 -9.9; 106 -10.3; 116 -10.7; 128 -11.0; 141 -11.2; 155 -11.4; 170 -11.5; 187 -11.5; 206 -11.5; 227 -11.4; 249 -11.2; 274 -11.0; 302 -10.8; 332 -10.5; 365 -10.2; 402 -9.9; 442 -9.6; 486 -9.2; 535 -8.7; 588 -8.3; 647 -7.8; 712 -7.2; 783 -6.6; 861 -6.1; 947 -5.8; 1042 -5.8; 1146 -6.3; 1261 -6.8; 1387 -7.1; 1526 -6.8; 1678 -6.1; 1846 -4.9; 2031 -3.6; 2234 -2.9; 2457 -2.7; 2703 -1.7; 2973 -0.8; 3270 -0.7; 3597 -1.0; 3957 -1.1; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -3.1; 6373 -5.5; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar TG334 sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar TG334 sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.56 | 2.9 dB  |
| Peaking | 167 Hz  | 0.61 | -2.7 dB |
| Peaking | 380 Hz  | 0.2  | -2.7 dB |
| Peaking | 858 Hz  | 1.73 | 2.7 dB  |
| Peaking | 3493 Hz | 0.93 | 6.9 dB  |
| Peaking | 1520 Hz | 2.66 | -2.1 dB |
| Peaking | 1860 Hz | 1.3  | 1.6 dB  |
| Peaking | 3677 Hz | 4.78 | -1.0 dB |
| Peaking | 5086 Hz | 2.95 | 4.0 dB  |
| Peaking | 6160 Hz | 0.97 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20TG334%20sample%203/FitEar%20TG334%20sample%203.png)