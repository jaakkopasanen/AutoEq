# Sennheiser HD 820
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.3; 25 -8.6; 28 -9.0; 31 -9.2; 34 -9.5; 37 -9.7; 41 -9.9; 45 -10.1; 49 -10.2; 54 -10.1; 60 -9.8; 66 -8.9; 72 -6.7; 79 -4.8; 87 -6.5; 96 -9.3; 106 -10.8; 116 -11.7; 128 -11.9; 141 -11.7; 155 -11.8; 170 -11.2; 187 -10.0; 206 -7.7; 227 -4.7; 249 -1.0; 274 -0.5; 302 -0.5; 332 -0.5; 365 -1.1; 402 -2.4; 442 -3.4; 486 -3.9; 535 -4.5; 588 -4.8; 647 -5.0; 712 -5.2; 783 -5.5; 861 -6.1; 947 -6.4; 1042 -6.4; 1146 -6.0; 1261 -5.1; 1387 -4.2; 1526 -3.5; 1678 -3.0; 1846 -2.8; 2031 -2.8; 2234 -2.9; 2457 -3.8; 2703 -4.6; 2973 -4.1; 3270 -1.9; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -5.1; 5267 -5.8; 5793 -3.3; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 820 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 820 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 1.49 | -3.7 dB |
| Peaking | 159 Hz  | 1.31 | -8.2 dB |
| Peaking | 288 Hz  | 1.29 | 8.8 dB  |
| Peaking | 1841 Hz | 2.17 | 3.5 dB  |
| Peaking | 3871 Hz | 2.11 | 6.0 dB  |
| Peaking | 81 Hz   | 6.62 | 4.2 dB  |
| Peaking | 108 Hz  | 4.64 | -1.8 dB |
| Peaking | 994 Hz  | 5.38 | -1.1 dB |
| Peaking | 5012 Hz | 9.28 | -3.2 dB |
| Peaking | 6351 Hz | 5.2  | 3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | 5.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20820/Sennheiser%20HD%20820.png)