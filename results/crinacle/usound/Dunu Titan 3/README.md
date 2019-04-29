# Dunu Titan 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -0.8; 66 -1.2; 72 -1.6; 79 -2.0; 87 -2.4; 96 -3.0; 106 -3.5; 116 -4.0; 128 -4.5; 141 -4.9; 155 -5.3; 170 -5.6; 187 -6.0; 206 -6.2; 227 -6.5; 249 -6.7; 274 -6.9; 302 -7.1; 332 -7.2; 365 -5.9; 402 -7.2; 442 -7.3; 486 -7.4; 535 -7.3; 588 -7.1; 647 -6.7; 712 -6.1; 783 -5.5; 861 -5.2; 947 -5.0; 1042 -5.2; 1146 -6.0; 1261 -6.9; 1387 -7.7; 1526 -7.9; 1678 -7.9; 1846 -7.9; 2031 -8.3; 2234 -9.1; 2457 -10.1; 2703 -10.4; 2973 -9.5; 3270 -7.9; 3597 -6.9; 3957 -6.8; 4353 -8.0; 4788 -11.3; 5267 -12.1; 5793 -6.3; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Titan 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.5  | 6.7 dB  |
| Peaking | 942 Hz  | 4.59 | 1.9 dB  |
| Peaking | 2515 Hz | 2.13 | -3.8 dB |
| Peaking | 5116 Hz | 5.69 | -7.2 dB |
| Peaking | 6448 Hz | 5.05 | 5.7 dB  |
| Peaking | 20 Hz   | 2.38 | 1.5 dB  |
| Peaking | 267 Hz  | 2.08 | -1.0 dB |
| Peaking | 488 Hz  | 3.5  | -1.1 dB |
| Peaking | 1486 Hz | 5.74 | -1.1 dB |
| Peaking | 3773 Hz | 6.76 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | 1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Dunu%20Titan%203/Dunu%20Titan%203.png)