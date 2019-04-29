# Vision Ears VE5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.8; 25 -2.0; 28 -2.3; 31 -2.6; 34 -2.9; 37 -3.1; 41 -3.4; 45 -3.6; 49 -3.9; 54 -4.2; 60 -4.5; 66 -4.9; 72 -5.3; 79 -5.7; 87 -6.1; 96 -6.7; 106 -7.1; 116 -7.5; 128 -7.9; 141 -8.2; 155 -8.5; 170 -8.7; 187 -8.9; 206 -9.0; 227 -9.1; 249 -9.1; 274 -9.1; 302 -9.0; 332 -9.0; 365 -8.9; 402 -8.8; 442 -8.7; 486 -8.6; 535 -8.4; 588 -8.2; 647 -8.0; 712 -7.6; 783 -7.3; 861 -7.1; 947 -6.9; 1042 -7.1; 1146 -7.5; 1261 -7.8; 1387 -7.8; 1526 -7.2; 1678 -6.5; 1846 -5.7; 2031 -5.2; 2234 -5.3; 2457 -5.8; 2703 -6.2; 2973 -4.9; 3270 -3.1; 3597 -4.2; 3957 -6.7; 4353 -7.1; 4788 -4.9; 5267 -3.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -7.2; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears VE5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears VE5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.4  | 5.1 dB  |
| Peaking | 63 Hz   | 0.97 | 1.1 dB  |
| Peaking | 241 Hz  | 0.42 | -2.9 dB |
| Peaking | 3279 Hz | 5.94 | 3.5 dB  |
| Peaking | 5989 Hz | 4.39 | 6.8 dB  |
| Peaking | 1362 Hz | 4.55 | -1.2 dB |
| Peaking | 2044 Hz | 3.59 | 1.5 dB  |
| Peaking | 4185 Hz | 8.87 | -2.0 dB |
| Peaking | 6943 Hz | 4.17 | 1.5 dB  |
| Peaking | 8014 Hz | 5.45 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vision%20Ears%20VE5/Vision%20Ears%20VE5.png)