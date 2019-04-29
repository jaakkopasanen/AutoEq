# Shure SE425
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.9; 37 -1.2; 41 -1.6; 45 -2.0; 49 -2.3; 54 -2.7; 60 -3.1; 66 -3.6; 72 -4.1; 79 -4.6; 87 -5.2; 96 -5.8; 106 -6.3; 116 -6.7; 128 -7.2; 141 -7.6; 155 -8.0; 170 -8.3; 187 -8.5; 206 -8.6; 227 -8.7; 249 -8.8; 274 -8.8; 302 -8.8; 332 -8.8; 365 -8.7; 402 -8.6; 442 -8.4; 486 -8.3; 535 -8.0; 588 -7.8; 647 -7.4; 712 -7.0; 783 -6.5; 861 -6.1; 947 -5.9; 1042 -6.0; 1146 -6.6; 1261 -7.1; 1387 -7.2; 1526 -6.9; 1678 -6.2; 1846 -5.7; 2031 -5.4; 2234 -5.5; 2457 -6.0; 2703 -6.5; 2973 -6.8; 3270 -7.3; 3597 -8.1; 3957 -7.9; 4353 -5.3; 4788 -2.3; 5267 -0.6; 5793 -0.5; 6373 -2.2; 7010 -6.5; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.32 | 6.2 dB  |
| Peaking | 219 Hz  | 0.43 | -3.0 dB |
| Peaking | 911 Hz  | 2.35 | 1.4 dB  |
| Peaking | 5385 Hz | 0.98 | -3.5 dB |
| Peaking | 5514 Hz | 2.58 | 10.5 dB |
| Peaking | 1374 Hz | 3.77 | -0.9 dB |
| Peaking | 2043 Hz | 2.57 | 1.5 dB  |
| Peaking | 3770 Hz | 4.71 | -2.4 dB |
| Peaking | 5724 Hz | 0.7  | 0.8 dB  |
| Peaking | 7396 Hz | 5.73 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shure%20SE425/Shure%20SE425.png)