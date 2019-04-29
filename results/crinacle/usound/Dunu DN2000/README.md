# Dunu DN2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.4; 25 -7.2; 28 -7.0; 31 -6.8; 34 -6.6; 37 -6.5; 41 -6.4; 45 -6.3; 49 -6.2; 54 -6.2; 60 -6.2; 66 -6.4; 72 -6.6; 79 -6.8; 87 -7.0; 96 -7.4; 106 -7.8; 116 -8.0; 128 -8.3; 141 -8.6; 155 -8.9; 170 -9.1; 187 -9.2; 206 -9.3; 227 -9.4; 249 -9.5; 274 -9.6; 302 -9.6; 332 -9.6; 365 -9.6; 402 -9.5; 442 -9.5; 486 -9.4; 535 -9.3; 588 -9.1; 647 -8.8; 712 -8.4; 783 -7.4; 861 -6.7; 947 -6.5; 1042 -6.4; 1146 -6.5; 1261 -6.6; 1387 -6.3; 1526 -5.4; 1678 -4.1; 1846 -2.7; 2031 -1.4; 2234 -0.6; 2457 -0.7; 2703 -1.9; 2973 -2.6; 3270 -2.6; 3597 -3.1; 3957 -4.4; 4353 -6.0; 4788 -4.8; 5267 -1.7; 5793 -0.5; 6373 -1.5; 7010 -5.9; 7711 -10.0; 8482 -7.8; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.22 | -0.8 dB |
| Peaking | 323 Hz  | 0.5  | -3.5 dB |
| Peaking | 2349 Hz | 1.59 | 6.1 dB  |
| Peaking | 6001 Hz | 3.26 | 6.6 dB  |
| Peaking | 7695 Hz | 4.65 | -5.4 dB |
| Peaking | 59 Hz   | 2.34 | 0.8 dB  |
| Peaking | 923 Hz  | 2.41 | 2.7 dB  |
| Peaking | 960 Hz  | 1.25 | -1.8 dB |
| Peaking | 4206 Hz | 2.12 | 2.0 dB  |
| Peaking | 4394 Hz | 5.31 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dunu%20DN2000/Dunu%20DN2000.png)