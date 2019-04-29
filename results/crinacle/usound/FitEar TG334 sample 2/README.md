# FitEar TG334 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.0; 25 -5.3; 28 -5.6; 31 -5.9; 34 -6.2; 37 -6.5; 41 -6.7; 45 -6.9; 49 -7.1; 54 -7.3; 60 -7.6; 66 -8.0; 72 -8.3; 79 -8.7; 87 -9.1; 96 -9.6; 106 -9.9; 116 -10.3; 128 -10.6; 141 -10.8; 155 -11.1; 170 -11.2; 187 -11.2; 206 -11.2; 227 -11.1; 249 -11.0; 274 -10.8; 302 -10.6; 332 -10.4; 365 -10.1; 402 -9.8; 442 -9.4; 486 -9.0; 535 -8.6; 588 -8.1; 647 -7.6; 712 -7.0; 783 -6.4; 861 -6.0; 947 -5.6; 1042 -5.8; 1146 -6.3; 1261 -6.8; 1387 -7.1; 1526 -6.8; 1678 -6.1; 1846 -5.0; 2031 -3.7; 2234 -3.2; 2457 -2.8; 2703 -1.7; 2973 -1.0; 3270 -1.4; 3597 -2.2; 3957 -2.6; 4353 -1.0; 4788 -0.5; 5267 -1.4; 5793 -3.3; 6373 -5.0; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar TG334 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar TG334 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  1    | 2.2 dB  |
| Peaking | 162 Hz  |  0.63 | -4.4 dB |
| Peaking | 351 Hz  |  1.26 | -1.9 dB |
| Peaking | 2878 Hz |  1.72 | 5.0 dB  |
| Peaking | 4870 Hz |  2.71 | 5.2 dB  |
| Peaking | 979 Hz  |  2.36 | 2.1 dB  |
| Peaking | 1381 Hz |  1.26 | -1.6 dB |
| Peaking | 2032 Hz |  4.23 | 1.5 dB  |
| Peaking | 6896 Hz | 11.4  | 1.8 dB  |
| Peaking | 8172 Hz |  2.18 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20TG334%20sample%202/FitEar%20TG334%20sample%202.png)