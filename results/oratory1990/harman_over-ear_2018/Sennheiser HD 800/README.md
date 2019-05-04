# Sennheiser HD 800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.9; 34 -1.2; 37 -1.5; 41 -1.9; 45 -2.1; 49 -2.3; 54 -2.2; 60 -2.1; 66 -2.4; 72 -3.2; 79 -3.9; 87 -4.5; 96 -5.1; 106 -5.7; 116 -6.1; 128 -6.6; 141 -6.9; 155 -7.2; 170 -7.4; 187 -7.5; 206 -7.7; 227 -7.8; 249 -7.7; 274 -7.6; 302 -7.4; 332 -7.2; 365 -7.0; 402 -6.9; 442 -6.9; 486 -6.8; 535 -6.7; 588 -6.6; 647 -6.5; 712 -6.4; 783 -6.3; 861 -6.3; 947 -6.1; 1042 -5.9; 1146 -5.7; 1261 -5.1; 1387 -4.3; 1526 -3.7; 1678 -3.4; 1846 -3.5; 2031 -3.3; 2234 -3.6; 2457 -4.9; 2703 -5.7; 2973 -5.9; 3270 -5.1; 3597 -4.9; 3957 -5.9; 4353 -7.3; 4788 -8.7; 5267 -11.6; 5793 -14.2; 6373 -10.8; 7010 -8.6; 7711 -10.0; 8482 -6.8; 9330 -6.5; 10263 -6.6; 11289 -11.2; 12418 -12.6; 13660 -11.6; 15026 -10.0; 16529 -9.9; 18182 -11.7; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.01 | 6.2 dB  |
| Peaking | 61 Hz    | 2.2  | 3.3 dB  |
| Peaking | 1910 Hz  | 1.35 | 3.4 dB  |
| Peaking | 5727 Hz  | 4.6  | -7.6 dB |
| Peaking | 20674 Hz | 0.13 | -6.5 dB |
| Peaking | 228 Hz   | 1.18 | -1.5 dB |
| Peaking | 3625 Hz  | 6.28 | 1.9 dB  |
| Peaking | 9933 Hz  | 2.46 | 6.7 dB  |
| Peaking | 11585 Hz | 1.13 | -5.9 dB |
| Peaking | 15720 Hz | 1.49 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)