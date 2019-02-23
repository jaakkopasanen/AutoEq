# TIN Audio T2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.3; 25 -6.3; 28 -6.3; 31 -6.3; 34 -6.2; 37 -6.2; 41 -6.1; 45 -6.0; 49 -5.9; 54 -5.9; 60 -6.1; 66 -6.4; 72 -6.6; 79 -6.7; 87 -7.0; 96 -7.3; 106 -7.7; 116 -8.1; 128 -8.4; 141 -8.7; 155 -8.8; 170 -8.8; 187 -8.8; 206 -8.8; 227 -8.7; 249 -8.4; 274 -8.2; 302 -7.8; 332 -7.5; 365 -7.2; 402 -6.8; 442 -6.4; 486 -6.0; 535 -5.5; 588 -5.0; 647 -4.6; 712 -4.3; 783 -4.0; 861 -4.0; 947 -4.3; 1042 -5.0; 1146 -5.5; 1261 -5.2; 1387 -4.9; 1526 -4.9; 1678 -4.9; 1846 -5.1; 2031 -5.2; 2234 -4.8; 2457 -4.2; 2703 -3.3; 2973 -1.7; 3270 -0.5; 3597 -0.7; 3957 -2.1; 4353 -3.4; 4788 -5.2; 5267 -4.7; 5793 -1.9; 6373 -1.3; 7010 -3.0; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -7.3; 11289 -10.0; 12418 -10.1; 13660 -7.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TIN Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TIN Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 185 Hz   |  0.62 | -3.6 dB |
| Peaking | 749 Hz   |  1.77 | 2.0 dB  |
| Peaking | 3379 Hz  |  2.87 | 5.3 dB  |
| Peaking | 6334 Hz  |  4.58 | 4.5 dB  |
| Peaking | 11932 Hz |  2.86 | -5.6 dB |
| Peaking | 23 Hz    |  1.61 | -0.8 dB |
| Peaking | 5014 Hz  | 11.33 | -1.5 dB |
| Peaking | 14777 Hz |  5.49 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/TIN%20Audio%20T2/TIN%20Audio%20T2.png)