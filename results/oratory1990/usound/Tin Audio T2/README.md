# Tin Audio T2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.9; 31 -1.3; 34 -1.7; 37 -2.1; 41 -2.5; 45 -2.9; 49 -3.2; 54 -3.6; 60 -4.1; 66 -4.5; 72 -4.9; 79 -5.4; 87 -5.9; 96 -6.4; 106 -6.9; 116 -7.4; 128 -7.8; 141 -8.1; 155 -8.4; 170 -8.6; 187 -8.7; 206 -8.7; 227 -8.8; 249 -9.0; 274 -9.0; 302 -9.0; 332 -8.9; 365 -8.8; 402 -8.7; 442 -8.5; 486 -8.3; 535 -8.0; 588 -7.8; 647 -7.4; 712 -7.0; 783 -6.6; 861 -6.2; 947 -6.5; 1042 -6.4; 1146 -6.1; 1261 -6.0; 1387 -5.7; 1526 -5.0; 1678 -4.2; 1846 -3.3; 2031 -2.7; 2234 -2.6; 2457 -3.1; 2703 -4.1; 2973 -4.8; 3270 -4.7; 3597 -4.4; 3957 -4.5; 4353 -5.1; 4788 -6.8; 5267 -7.3; 5793 -4.8; 6373 -3.0; 7010 -4.7; 7711 -8.2; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.9; 12418 -8.7; 13660 -8.1; 15026 -8.3; 16529 -6.9; 18182 -6.5; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.66 | 6.0 dB  |
| Peaking | 58 Hz    | 1.16 | 1.2 dB  |
| Peaking | 241 Hz   | 0.52 | -2.8 dB |
| Peaking | 2119 Hz  | 1.65 | 4.0 dB  |
| Peaking | 3808 Hz  | 3.68 | 1.4 dB  |
| Peaking | 459 Hz   | 4.38 | -0.3 dB |
| Peaking | 5213 Hz  | 4.93 | -3.2 dB |
| Peaking | 6425 Hz  | 2.51 | 4.3 dB  |
| Peaking | 7849 Hz  | 5.25 | -3.8 dB |
| Peaking | 13860 Hz | 1.41 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Tin%20Audio%20T2/Tin%20Audio%20T2.png)