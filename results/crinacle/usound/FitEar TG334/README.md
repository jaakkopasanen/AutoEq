# FitEar TG334
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.3; 25 -5.5; 28 -5.8; 31 -6.0; 34 -6.2; 37 -6.4; 41 -6.6; 45 -6.8; 49 -7.0; 54 -7.3; 60 -7.6; 66 -7.9; 72 -8.3; 79 -8.6; 87 -9.0; 96 -9.5; 106 -9.9; 116 -10.2; 128 -10.5; 141 -10.8; 155 -11.0; 170 -11.1; 187 -11.1; 206 -11.1; 227 -11.0; 249 -10.9; 274 -10.7; 302 -10.5; 332 -10.3; 365 -10.0; 402 -9.7; 442 -9.3; 486 -8.9; 535 -8.5; 588 -8.1; 647 -7.6; 712 -7.0; 783 -6.4; 861 -5.9; 947 -5.6; 1042 -5.8; 1146 -6.3; 1261 -6.8; 1387 -7.1; 1526 -6.9; 1678 -6.2; 1846 -5.0; 2031 -3.7; 2234 -3.1; 2457 -2.8; 2703 -1.7; 2973 -1.0; 3270 -1.3; 3597 -1.8; 3957 -1.9; 4353 -0.7; 4788 -0.5; 5267 -1.4; 5793 -3.8; 6373 -5.8; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar TG334 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar TG334 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.76 | 1.7 dB  |
| Peaking | 162 Hz  | 0.65 | -4.3 dB |
| Peaking | 348 Hz  | 1.22 | -1.9 dB |
| Peaking | 2938 Hz | 1.63 | 5.1 dB  |
| Peaking | 4796 Hz | 3.04 | 5.2 dB  |
| Peaking | 968 Hz  | 2.61 | 1.7 dB  |
| Peaking | 1458 Hz | 1.58 | -1.5 dB |
| Peaking | 2033 Hz | 4.3  | 1.4 dB  |
| Peaking | 8884 Hz | 3.01 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20TG334/FitEar%20TG334.png)