# Dunu DN1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.2; 25 -2.4; 28 -2.6; 31 -2.8; 34 -3.0; 37 -3.1; 41 -3.3; 45 -3.5; 49 -3.7; 54 -4.0; 60 -4.3; 66 -4.6; 72 -5.0; 79 -5.3; 87 -5.8; 96 -6.2; 106 -6.7; 116 -7.1; 128 -7.4; 141 -7.8; 155 -8.1; 170 -8.3; 187 -8.5; 206 -8.6; 227 -8.6; 249 -8.7; 274 -8.6; 302 -8.6; 332 -8.5; 365 -8.4; 402 -8.2; 442 -8.0; 486 -7.8; 535 -7.5; 588 -7.2; 647 -6.8; 712 -6.3; 783 -5.7; 861 -5.2; 947 -4.9; 1042 -4.9; 1146 -5.2; 1261 -5.6; 1387 -5.7; 1526 -5.2; 1678 -4.4; 1846 -3.7; 2031 -3.1; 2234 -2.8; 2457 -2.9; 2703 -3.3; 2973 -3.7; 3270 -3.3; 3597 -1.3; 3957 -0.5; 4353 -2.7; 4788 -5.1; 5267 -5.1; 5793 -4.5; 6373 -5.1; 7010 -7.3; 7711 -11.8; 8482 -11.5; 9330 -7.1; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.2  | 4.1 dB  |
| Peaking | 227 Hz  | 0.49 | -3.1 dB |
| Peaking | 2702 Hz | 0.48 | 2.8 dB  |
| Peaking | 3867 Hz | 6.09 | 3.8 dB  |
| Peaking | 8030 Hz | 4.47 | -7.8 dB |
| Peaking | 938 Hz  | 2.26 | 1.5 dB  |
| Peaking | 1396 Hz | 2.8  | -1.1 dB |
| Peaking | 1810 Hz | 0.34 | -0.6 dB |
| Peaking | 2140 Hz | 2.26 | 1.4 dB  |
| Peaking | 6304 Hz | 6.58 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dunu%20DN1000/Dunu%20DN1000.png)