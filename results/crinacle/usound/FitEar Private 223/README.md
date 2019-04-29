# FitEar Private 223
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.7; 31 -0.8; 34 -1.0; 37 -1.1; 41 -1.2; 45 -1.4; 49 -1.6; 54 -1.7; 60 -2.0; 66 -2.4; 72 -2.9; 79 -3.4; 87 -3.6; 96 -4.1; 106 -4.8; 116 -4.9; 128 -5.2; 141 -5.5; 155 -5.8; 170 -6.2; 187 -6.2; 206 -6.3; 227 -6.3; 249 -6.3; 274 -6.3; 302 -6.2; 332 -6.1; 365 -6.0; 402 -5.9; 442 -5.7; 486 -5.6; 535 -5.4; 588 -5.1; 647 -4.9; 712 -4.6; 783 -4.3; 861 -4.2; 947 -4.3; 1042 -4.8; 1146 -5.8; 1261 -6.8; 1387 -7.7; 1526 -8.3; 1678 -8.6; 1846 -8.0; 2031 -6.5; 2234 -6.1; 2457 -6.2; 2703 -5.0; 2973 -3.3; 3270 -2.9; 3597 -4.0; 3957 -7.1; 4353 -7.5; 4788 -7.7; 5267 -12.2; 5793 -16.3; 6373 -12.4; 7010 -10.7; 7711 -6.8; 8482 -6.3; 9330 -6.3; 10263 -7.9; 11289 -8.6; 12418 -7.2; 13660 -10.4; 15026 -11.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Private 223 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Private 223 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.59 | 5.4 dB   |
| Peaking | 58 Hz    | 1.06 | 2.3 dB   |
| Peaking | 3226 Hz  | 4.34 | 4.4 dB   |
| Peaking | 5865 Hz  | 4.01 | -10.5 dB |
| Peaking | 14352 Hz | 3.24 | -6.2 dB  |
| Peaking | 214 Hz   | 1.76 | -0.5 dB  |
| Peaking | 865 Hz   | 1.27 | 2.4 dB   |
| Peaking | 1557 Hz  | 2.51 | -3.1 dB  |
| Peaking | 8763 Hz  | 3.86 | 1.3 dB   |
| Peaking | 10917 Hz | 7.3  | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20Private%20223/FitEar%20Private%20223.png)