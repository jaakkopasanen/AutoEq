# Vision Ears Erlkönig 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.5; 25 -4.8; 28 -5.1; 31 -5.3; 34 -5.5; 37 -5.7; 41 -5.9; 45 -6.1; 49 -6.3; 54 -6.6; 60 -6.8; 66 -7.1; 72 -7.4; 79 -7.7; 87 -8.0; 96 -8.4; 106 -8.6; 116 -8.9; 128 -9.1; 141 -9.2; 155 -9.2; 170 -9.1; 187 -9.0; 206 -8.9; 227 -8.7; 249 -8.4; 274 -8.1; 302 -7.8; 332 -7.4; 365 -7.0; 402 -6.5; 442 -6.1; 486 -5.7; 535 -5.2; 588 -4.6; 647 -4.0; 712 -3.4; 783 -2.8; 861 -2.3; 947 -2.0; 1042 -2.1; 1146 -2.7; 1261 -3.3; 1387 -3.5; 1526 -3.3; 1678 -2.8; 1846 -2.3; 2031 -2.3; 2234 -2.6; 2457 -3.0; 2703 -2.9; 2973 -2.1; 3270 -2.2; 3597 -2.5; 3957 -2.3; 4353 -1.9; 4788 -1.7; 5267 -1.3; 5793 -0.5; 6373 -0.9; 7010 -2.9; 7711 -4.2; 8482 -4.4; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears Erlkönig 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears Erlkönig 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 93 Hz   | 0.57 | -1.5 dB |
| Peaking | 189 Hz  | 0.51 | -3.9 dB |
| Peaking | 887 Hz  | 1.56 | 2.7 dB  |
| Peaking | 2920 Hz | 0.76 | 2.0 dB  |
| Peaking | 5812 Hz | 3.17 | 3.4 dB  |
| Peaking | 14 Hz   | 1.73 | 1.1 dB  |
| Peaking | 1927 Hz | 3.11 | 2.1 dB  |
| Peaking | 2087 Hz | 1.13 | -2.3 dB |
| Peaking | 2725 Hz | 0.5  | 0.9 dB  |
| Peaking | 8473 Hz | 2    | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vision%20Ears%20Erlk%C3%B6nig%202/Vision%20Ears%20Erlk%C3%B6nig%202.png)