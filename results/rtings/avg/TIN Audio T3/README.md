# TIN Audio T3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.0; 25 -12.0; 28 -11.9; 31 -11.7; 34 -11.6; 37 -11.4; 41 -11.2; 45 -11.0; 49 -10.8; 54 -10.6; 60 -10.4; 66 -10.3; 72 -10.1; 79 -10.0; 87 -9.9; 96 -9.8; 106 -9.7; 116 -9.6; 128 -9.4; 141 -9.2; 155 -8.9; 170 -8.6; 187 -8.3; 206 -8.1; 227 -7.9; 249 -7.7; 274 -7.4; 302 -7.1; 332 -6.7; 365 -6.3; 402 -5.9; 442 -5.5; 486 -5.1; 535 -4.5; 588 -3.9; 647 -3.3; 712 -2.8; 783 -2.4; 861 -2.4; 947 -2.6; 1042 -3.0; 1146 -3.5; 1261 -3.9; 1387 -4.2; 1526 -4.4; 1678 -4.7; 1846 -5.1; 2031 -5.4; 2234 -5.3; 2457 -4.4; 2703 -2.9; 2973 -1.0; 3270 -0.5; 3597 -1.2; 3957 -2.4; 4353 -4.1; 4788 -6.1; 5267 -6.5; 5793 -4.7; 6373 -2.9; 7010 -3.4; 7711 -5.5; 8482 -8.8; 9330 -12.4; 10263 -13.4; 11289 -8.6; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TIN Audio T3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TIN Audio T3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.51 | -5.8 dB |
| Peaking | 107 Hz   | 0.38 | -3.4 dB |
| Peaking | 803 Hz   | 1.28 | 3.6 dB  |
| Peaking | 3307 Hz  | 2.93 | 5.3 dB  |
| Peaking | 9931 Hz  | 4.05 | -9.3 dB |
| Peaking | 4149 Hz  | 4.01 | 2.1 dB  |
| Peaking | 5134 Hz  | 1.86 | -3.5 dB |
| Peaking | 6471 Hz  | 2.73 | 4.8 dB  |
| Peaking | 8758 Hz  | 6.17 | -2.0 dB |
| Peaking | 12335 Hz | 6.83 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/TIN%20Audio%20T3/TIN%20Audio%20T3.png)