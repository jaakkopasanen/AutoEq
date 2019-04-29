# KZ AS10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -8.9; 25 -9.1; 28 -9.4; 31 -9.6; 34 -9.8; 37 -9.9; 41 -9.9; 45 -10.0; 49 -10.2; 54 -10.3; 60 -10.3; 66 -10.5; 72 -10.7; 79 -10.8; 87 -11.0; 96 -11.1; 106 -11.3; 116 -11.3; 128 -11.3; 141 -11.2; 155 -11.0; 170 -10.8; 187 -10.5; 206 -10.1; 227 -9.8; 249 -9.4; 274 -8.9; 302 -8.4; 332 -7.7; 365 -7.1; 402 -6.5; 442 -6.0; 486 -5.4; 535 -4.8; 588 -4.3; 647 -3.7; 712 -3.0; 783 -2.4; 861 -2.0; 947 -1.8; 1042 -1.9; 1146 -2.3; 1261 -2.5; 1387 -2.3; 1526 -1.9; 1678 -1.6; 1846 -1.4; 2031 -1.4; 2234 -1.7; 2457 -3.1; 2703 -5.8; 2973 -7.2; 3270 -5.6; 3597 -4.5; 3957 -4.6; 4353 -1.4; 4788 -5.7; 5267 -7.1; 5793 -1.8; 6373 -0.5; 7010 -2.8; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.8; 11289 -6.9; 12418 -7.6; 13660 -9.9; 15026 -11.0; 16529 -12.2; 18182 -13.5; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ AS10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ AS10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 30 Hz    |  0.48 | -3.1 dB |
| Peaking | 145 Hz   |  0.44 | -5.6 dB |
| Peaking | 1087 Hz  |  0.61 | 4.2 dB  |
| Peaking | 6422 Hz  |  5.14 | 5.6 dB  |
| Peaking | 17729 Hz |  0.68 | -8.5 dB |
| Peaking | 2162 Hz  |  3.31 | 2.3 dB  |
| Peaking | 2932 Hz  |  4.68 | -3.8 dB |
| Peaking | 4416 Hz  |  8.5  | 4.0 dB  |
| Peaking | 5077 Hz  | 10.11 | -4.4 dB |
| Peaking | 9669 Hz  |  4.09 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -9.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20AS10/KZ%20AS10.png)