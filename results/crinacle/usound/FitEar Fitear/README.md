# FitEar Fitear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.1; 25 -8.1; 28 -8.2; 31 -8.3; 34 -8.4; 37 -8.5; 41 -8.6; 45 -8.7; 49 -8.9; 54 -9.0; 60 -9.2; 66 -9.5; 72 -9.8; 79 -10.2; 87 -10.5; 96 -10.9; 106 -11.2; 116 -11.5; 128 -11.8; 141 -12.0; 155 -12.2; 170 -12.2; 187 -12.2; 206 -12.2; 227 -12.1; 249 -12.0; 274 -11.8; 302 -11.6; 332 -11.3; 365 -11.0; 402 -10.6; 442 -10.3; 486 -9.8; 535 -9.4; 588 -8.9; 647 -8.3; 712 -7.6; 783 -7.0; 861 -6.3; 947 -5.9; 1042 -5.8; 1146 -6.1; 1261 -6.5; 1387 -6.6; 1526 -6.1; 1678 -5.2; 1846 -4.2; 2031 -3.5; 2234 -3.0; 2457 -2.9; 2703 -3.2; 2973 -3.6; 3270 -3.7; 3597 -2.9; 3957 -1.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.8; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Fitear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Fitear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.25 | -1.5 dB |
| Peaking | 173 Hz  | 0.62 | -4.6 dB |
| Peaking | 384 Hz  | 1.24 | -2.2 dB |
| Peaking | 2319 Hz | 1.64 | 3.1 dB  |
| Peaking | 5002 Hz | 1.77 | 6.6 dB  |
| Peaking | 967 Hz  | 3.62 | 1.2 dB  |
| Peaking | 1394 Hz | 4.86 | -0.9 dB |
| Peaking | 6367 Hz | 5.42 | 2.8 dB  |
| Peaking | 7725 Hz | 6.51 | -3.0 dB |
| Peaking | 8040 Hz | 0.96 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20Fitear/FitEar%20Fitear.png)