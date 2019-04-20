# Sennheiser HD 555
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.9; 49 -1.2; 54 -1.3; 60 -1.2; 66 -1.6; 72 -2.4; 79 -3.3; 87 -4.1; 96 -4.8; 106 -5.4; 116 -5.9; 128 -6.4; 141 -6.8; 155 -7.2; 170 -7.5; 187 -7.7; 206 -7.9; 227 -8.0; 249 -8.0; 274 -8.0; 302 -7.9; 332 -7.7; 365 -7.5; 402 -7.5; 442 -7.6; 486 -7.5; 535 -7.3; 588 -7.1; 647 -7.1; 712 -7.4; 783 -7.6; 861 -7.8; 947 -8.0; 1042 -8.2; 1146 -8.2; 1261 -8.1; 1387 -7.5; 1526 -6.5; 1678 -5.6; 1846 -5.3; 2031 -6.0; 2234 -7.2; 2457 -8.3; 2703 -9.1; 2973 -9.3; 3270 -9.8; 3597 -9.3; 3957 -6.3; 4353 -3.7; 4788 -3.8; 5267 -5.3; 5793 -1.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -8.6; 16529 -9.8; 18182 -12.2; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 555 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 555 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.37 | 7.2 dB  |
| Peaking | 158 Hz  | 0.39 | -3.2 dB |
| Peaking | 3356 Hz | 2.18 | -4.3 dB |
| Peaking | 4376 Hz | 4    | 4.5 dB  |
| Peaking | 6229 Hz | 5.12 | 6.4 dB  |
| Peaking | 172 Hz  | 0.64 | -1.0 dB |
| Peaking | 267 Hz  | 0.28 | 1.0 dB  |
| Peaking | 1185 Hz | 1.25 | -2.2 dB |
| Peaking | 1776 Hz | 2.41 | 2.6 dB  |
| Peaking | 2523 Hz | 5.48 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20555/Sennheiser%20HD%20555.png)