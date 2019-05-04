# Tin Audio T2 (Foam Eartips)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.0; 34 -1.4; 37 -1.7; 41 -2.2; 45 -2.5; 49 -2.8; 54 -3.2; 60 -3.7; 66 -4.1; 72 -4.5; 79 -5.0; 87 -5.5; 96 -6.0; 106 -6.5; 116 -7.0; 128 -7.4; 141 -7.7; 155 -8.0; 170 -8.2; 187 -8.4; 206 -8.5; 227 -8.6; 249 -8.7; 274 -8.7; 302 -8.7; 332 -8.6; 365 -8.5; 402 -8.4; 442 -8.2; 486 -8.1; 535 -7.8; 588 -7.5; 647 -7.2; 712 -6.9; 783 -6.5; 861 -6.3; 947 -6.5; 1042 -6.0; 1146 -6.1; 1261 -6.1; 1387 -5.9; 1526 -5.4; 1678 -4.8; 1846 -4.1; 2031 -3.7; 2234 -3.9; 2457 -4.6; 2703 -5.1; 2973 -4.7; 3270 -3.7; 3597 -3.0; 3957 -3.1; 4353 -3.8; 4788 -5.5; 5267 -6.2; 5793 -4.2; 6373 -2.5; 7010 -3.9; 7711 -8.8; 8482 -10.8; 9330 -9.0; 10263 -9.7; 11289 -13.1; 12418 -14.3; 13660 -12.2; 15026 -7.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 (Foam Eartips) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 (Foam Eartips) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.93 | 6.4 dB  |
| Peaking | 3206 Hz  | 0.89 | 2.9 dB  |
| Peaking | 6616 Hz  | 4.88 | 4.8 dB  |
| Peaking | 8235 Hz  | 4.29 | -4.4 dB |
| Peaking | 12278 Hz | 2.26 | -8.6 dB |
| Peaking | 66 Hz    | 1.6  | 1.4 dB  |
| Peaking | 252 Hz   | 0.59 | -2.5 dB |
| Peaking | 2057 Hz  | 1.79 | 2.6 dB  |
| Peaking | 2951 Hz  | 1.24 | -3.0 dB |
| Peaking | 3665 Hz  | 3.04 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Tin%20Audio%20T2%20(Foam%20Eartips)/Tin%20Audio%20T2%20(Foam%20Eartips).png)