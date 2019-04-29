# Advanced 747
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.5; 25 -11.6; 28 -11.8; 31 -11.9; 34 -12.0; 37 -12.1; 41 -12.2; 45 -12.3; 49 -12.4; 54 -12.5; 60 -12.7; 66 -12.8; 72 -13.1; 79 -13.3; 87 -13.5; 96 -13.8; 106 -13.9; 116 -14.1; 128 -14.1; 141 -14.1; 155 -14.0; 170 -13.9; 187 -13.6; 206 -13.3; 227 -12.9; 249 -12.4; 274 -11.9; 302 -11.3; 332 -10.7; 365 -10.0; 402 -9.3; 442 -8.7; 486 -7.9; 535 -7.1; 588 -6.3; 647 -5.4; 712 -4.3; 783 -3.3; 861 -2.3; 947 -1.5; 1042 -1.0; 1146 -0.7; 1261 -0.5; 1387 -0.8; 1526 -1.3; 1678 -2.1; 1846 -2.5; 2031 -2.6; 2234 -2.5; 2457 -2.8; 2703 -3.4; 2973 -3.9; 3270 -3.7; 3597 -2.7; 3957 -1.8; 4353 -1.7; 4788 -2.6; 5267 -4.5; 5793 -7.7; 6373 -6.4; 7010 -5.3; 7711 -8.3; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -10.3; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced 747 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced 747 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 26 Hz   |  0.25 | -3.9 dB |
| Peaking | 179 Hz  |  0.4  | -6.6 dB |
| Peaking | 1174 Hz |  0.71 | 6.8 dB  |
| Peaking | 4137 Hz |  3.36 | 4.3 dB  |
| Peaking | 26 Hz   |  1.21 | -0.5 dB |
| Peaking | 1766 Hz |  4.56 | -0.6 dB |
| Peaking | 2370 Hz |  4.65 | 0.9 dB  |
| Peaking | 4830 Hz | 11.92 | 1.3 dB  |
| Peaking | 8008 Hz |  7.32 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20747/Advanced%20747.png)