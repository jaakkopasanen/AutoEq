# InEar PhoPhile-8 Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.1; 25 -3.3; 28 -3.7; 31 -3.9; 34 -4.1; 37 -4.2; 41 -4.5; 45 -4.7; 49 -4.8; 54 -5.0; 60 -5.2; 66 -5.5; 72 -5.8; 79 -6.1; 87 -6.3; 96 -6.7; 106 -6.8; 116 -7.0; 128 -7.1; 141 -7.1; 155 -7.1; 170 -6.9; 187 -6.7; 206 -6.4; 227 -6.0; 249 -5.7; 274 -5.3; 302 -5.0; 332 -4.8; 365 -4.5; 402 -4.3; 442 -4.2; 486 -4.1; 535 -3.9; 588 -3.8; 647 -3.6; 712 -3.4; 783 -3.2; 861 -3.0; 947 -3.0; 1042 -3.4; 1146 -4.2; 1261 -5.0; 1387 -5.4; 1526 -5.3; 1678 -4.8; 1846 -4.0; 2031 -3.3; 2234 -2.6; 2457 -1.8; 2703 -1.3; 2973 -1.4; 3270 -1.9; 3597 -1.6; 3957 -1.0; 4353 -0.5; 4788 -0.9; 5267 -2.8; 5793 -4.5; 6373 -3.2; 7010 -4.0; 7711 -5.8; 8482 -4.3; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.0; 18182 -7.5; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar PhoPhile-8 Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar PhoPhile-8 Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  1.81 | 1.5 dB  |
| Peaking | 130 Hz  |  0.8  | -3.3 dB |
| Peaking | 2765 Hz |  3.13 | 2.6 dB  |
| Peaking | 4319 Hz |  3.02 | 3.6 dB  |
| Peaking | 7710 Hz |  6.5  | -2.0 dB |
| Peaking | 18 Hz   |  1.36 | 0.3 dB  |
| Peaking | 957 Hz  |  1.36 | 1.7 dB  |
| Peaking | 1387 Hz |  1.97 | -2.5 dB |
| Peaking | 2200 Hz |  3.79 | 0.7 dB  |
| Peaking | 5669 Hz | 14.24 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/InEar%20PhoPhile-8%20Bass/InEar%20PhoPhile-8%20Bass.png)