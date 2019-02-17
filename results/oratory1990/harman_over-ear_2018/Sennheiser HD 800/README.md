# Sennheiser HD 800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.4; 34 -1.7; 37 -2.0; 41 -2.4; 45 -2.7; 49 -2.8; 54 -2.7; 60 -2.6; 66 -3.0; 72 -3.8; 79 -4.5; 87 -5.1; 96 -5.7; 106 -6.2; 116 -6.7; 128 -7.1; 141 -7.4; 155 -7.7; 170 -7.9; 187 -8.0; 206 -8.2; 227 -8.3; 249 -8.2; 274 -8.1; 302 -7.9; 332 -7.7; 365 -7.5; 402 -7.4; 442 -7.4; 486 -7.3; 535 -7.2; 588 -7.1; 647 -7.0; 712 -6.9; 783 -6.8; 861 -6.8; 947 -6.6; 1042 -6.4; 1146 -6.2; 1261 -5.6; 1387 -4.8; 1526 -4.3; 1678 -4.0; 1846 -4.0; 2031 -3.8; 2234 -4.1; 2457 -5.4; 2703 -6.2; 2973 -6.4; 3270 -5.6; 3597 -5.3; 3957 -6.0; 4353 -7.2; 4788 -9.0; 5267 -12.1; 5793 -14.7; 6373 -10.9; 7010 -8.7; 7711 -10.0; 8482 -6.9; 9330 -6.5; 10263 -6.6; 11289 -11.3; 12418 -13.2; 13660 -12.5; 15026 -10.5; 16529 -9.7; 18182 -11.0; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.12 | 6.3 dB  |
| Peaking | 59 Hz    | 2.61 | 3.1 dB  |
| Peaking | 1914 Hz  | 1.77 | 3.0 dB  |
| Peaking | 5705 Hz  | 5.05 | -8.0 dB |
| Peaking | 20594 Hz | 0.11 | -5.9 dB |
| Peaking | 241 Hz   | 0.85 | -1.9 dB |
| Peaking | 3705 Hz  | 4.96 | 1.8 dB  |
| Peaking | 9893 Hz  | 2.4  | 7.0 dB  |
| Peaking | 11864 Hz | 1.01 | -6.2 dB |
| Peaking | 16036 Hz | 1.36 | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -6.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)