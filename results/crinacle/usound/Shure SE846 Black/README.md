# Shure SE846 Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -8.8; 25 -8.9; 28 -9.0; 31 -9.1; 34 -9.1; 37 -9.2; 41 -9.2; 45 -9.3; 49 -9.3; 54 -9.3; 60 -9.4; 66 -9.5; 72 -9.6; 79 -9.7; 87 -9.8; 96 -10.0; 106 -10.1; 116 -10.1; 128 -10.1; 141 -10.0; 155 -10.0; 170 -9.9; 187 -9.7; 206 -9.6; 227 -9.5; 249 -9.3; 274 -9.1; 302 -9.1; 332 -9.0; 365 -8.9; 402 -8.8; 442 -8.8; 486 -8.7; 535 -8.6; 588 -8.3; 647 -8.1; 712 -7.7; 783 -7.2; 861 -6.8; 947 -6.6; 1042 -6.8; 1146 -7.4; 1261 -7.9; 1387 -8.1; 1526 -7.7; 1678 -7.0; 1846 -6.3; 2031 -5.6; 2234 -4.9; 2457 -4.0; 2703 -3.0; 2973 -2.1; 3270 -2.3; 3597 -3.1; 3957 -3.5; 4353 -2.7; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.46 | -1.1 dB |
| Peaking | 142 Hz   | 0.38 | -2.5 dB |
| Peaking | 198 Hz   | 0    | -0.9 dB |
| Peaking | 3034 Hz  | 1.86 | 4.6 dB  |
| Peaking | 5539 Hz  | 2.28 | 6.6 dB  |
| Peaking | 942 Hz   | 3.78 | 1.1 dB  |
| Peaking | 1379 Hz  | 3.61 | -1.3 dB |
| Peaking | 6569 Hz  | 6.16 | 2.7 dB  |
| Peaking | 7530 Hz  | 1.8  | -1.9 dB |
| Peaking | 11851 Hz | 0.23 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shure%20SE846%20Black/Shure%20SE846%20Black.png)