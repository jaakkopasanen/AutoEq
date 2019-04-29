# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.5; 25 -7.6; 28 -7.7; 31 -7.7; 34 -7.8; 37 -7.8; 41 -7.9; 45 -8.0; 49 -8.1; 54 -8.2; 60 -8.4; 66 -8.6; 72 -8.8; 79 -9.0; 87 -9.3; 96 -9.6; 106 -9.8; 116 -9.9; 128 -10.0; 141 -10.1; 155 -10.1; 170 -9.9; 187 -9.8; 206 -9.5; 227 -9.2; 249 -8.9; 274 -8.4; 302 -8.0; 332 -7.5; 365 -7.0; 402 -6.5; 442 -6.1; 486 -5.5; 535 -5.1; 588 -4.5; 647 -4.0; 712 -3.5; 783 -2.9; 861 -2.5; 947 -2.5; 1042 -2.8; 1146 -3.7; 1261 -4.6; 1387 -5.3; 1526 -5.6; 1678 -5.5; 1846 -5.6; 2031 -6.1; 2234 -6.9; 2457 -6.9; 2703 -5.6; 2973 -3.8; 3270 -2.4; 3597 -1.8; 3957 -2.3; 4353 -4.3; 4788 -8.0; 5267 -7.9; 5793 -3.1; 6373 -0.5; 7010 -3.1; 7711 -6.2; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.27 | -1.8 dB |
| Peaking | 161 Hz   | 0.67 | -3.6 dB |
| Peaking | 840 Hz   | 1.68 | 3.7 dB  |
| Peaking | 3583 Hz  | 4.47 | 4.3 dB  |
| Peaking | 21405 Hz | 2.28 | 2.2 dB  |
| Peaking | 524 Hz   | 3.97 | 0.5 dB  |
| Peaking | 2318 Hz  | 4.63 | -2.0 dB |
| Peaking | 4231 Hz  | 4.34 | 1.7 dB  |
| Peaking | 5007 Hz  | 5.18 | -5.1 dB |
| Peaking | 6319 Hz  | 5.22 | 5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shure%20SE215/Shure%20SE215.png)