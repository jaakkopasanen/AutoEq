# VSonic GR07 Mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.1; 25 -1.5; 28 -2.0; 31 -2.4; 34 -2.8; 37 -3.1; 41 -3.4; 45 -3.8; 49 -4.1; 54 -4.4; 60 -4.8; 66 -5.2; 72 -5.6; 79 -6.0; 87 -6.5; 96 -6.9; 106 -7.4; 116 -7.7; 128 -8.0; 141 -8.4; 155 -8.6; 170 -8.8; 187 -8.9; 206 -9.0; 227 -9.0; 249 -9.0; 274 -9.0; 302 -9.0; 332 -8.9; 365 -8.8; 402 -8.8; 442 -8.7; 486 -8.6; 535 -8.4; 588 -8.3; 647 -8.0; 712 -7.6; 783 -7.2; 861 -6.9; 947 -6.6; 1042 -6.6; 1146 -7.0; 1261 -7.4; 1387 -7.5; 1526 -7.1; 1678 -6.4; 1846 -4.9; 2031 -4.0; 2234 -4.4; 2457 -4.1; 2703 -3.6; 2973 -2.8; 3270 -1.9; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -2.5; 5793 -5.6; 6373 -7.2; 7010 -6.4; 7711 -9.2; 8482 -10.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.3; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic GR07 Mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 Mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.52 | 6.2 dB  |
| Peaking | 61 Hz   | 0.82 | 1.4 dB  |
| Peaking | 225 Hz  | 0.36 | -2.8 dB |
| Peaking | 3966 Hz | 1.29 | 6.5 dB  |
| Peaking | 7978 Hz | 3.11 | -4.6 dB |
| Peaking | 988 Hz  | 1.78 | 1.9 dB  |
| Peaking | 1516 Hz | 0.86 | -2.5 dB |
| Peaking | 1985 Hz | 2.63 | 3.0 dB  |
| Peaking | 5816 Hz | 2.05 | 2.7 dB  |
| Peaking | 6106 Hz | 5.01 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/VSonic%20GR07%20Mk2/VSonic%20GR07%20Mk2.png)