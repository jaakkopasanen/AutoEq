# Sennheiser HD 800 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.6; 31 -1.9; 34 -2.2; 37 -2.4; 41 -2.6; 45 -2.7; 49 -2.9; 54 -3.0; 60 -2.9; 66 -3.2; 72 -3.7; 79 -4.5; 87 -5.1; 96 -5.7; 106 -6.3; 116 -6.7; 128 -7.1; 141 -7.4; 155 -7.7; 170 -7.9; 187 -8.0; 206 -8.1; 227 -8.2; 249 -8.1; 274 -8.0; 302 -7.8; 332 -7.5; 365 -7.3; 402 -7.2; 442 -7.1; 486 -7.0; 535 -6.9; 588 -6.8; 647 -6.7; 712 -6.6; 783 -6.6; 861 -6.6; 947 -6.5; 1042 -6.3; 1146 -5.9; 1261 -5.1; 1387 -4.3; 1526 -4.1; 1678 -4.1; 1846 -4.3; 2031 -4.2; 2234 -4.3; 2457 -5.0; 2703 -5.4; 2973 -5.2; 3270 -4.3; 3597 -4.5; 3957 -5.8; 4353 -5.5; 4788 -6.8; 5267 -10.1; 5793 -10.4; 6373 -8.7; 7010 -7.5; 7711 -7.0; 8482 -6.3; 9330 -6.3; 10263 -6.6; 11289 -11.7; 12418 -13.6; 13660 -12.1; 15026 -10.5; 16529 -11.8; 18182 -13.6; 20000 -13.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.11 | 5.6 dB  |
| Peaking | 57 Hz    | 2.45 | 2.8 dB  |
| Peaking | 5628 Hz  | 6.41 | -4.8 dB |
| Peaking | 12497 Hz | 3.3  | -6.5 dB |
| Peaking | 18955 Hz | 0.64 | -8.1 dB |
| Peaking | 81 Hz    | 1.92 | 1.3 dB  |
| Peaking | 209 Hz   | 0.6  | -1.9 dB |
| Peaking | 1743 Hz  | 1.59 | 2.6 dB  |
| Peaking | 3424 Hz  | 3.79 | 2.0 dB  |
| Peaking | 16387 Hz | 2.9  | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -8.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)