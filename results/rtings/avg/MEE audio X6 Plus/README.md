# MEE audio X6 Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.6; 25 -9.5; 28 -9.1; 31 -8.6; 34 -8.2; 37 -7.9; 41 -7.7; 45 -7.8; 49 -8.0; 54 -8.2; 60 -8.4; 66 -8.2; 72 -7.8; 79 -7.3; 87 -6.8; 96 -6.5; 106 -6.1; 116 -5.8; 128 -5.6; 141 -5.2; 155 -4.9; 170 -4.6; 187 -4.2; 206 -3.8; 227 -3.5; 249 -3.2; 274 -2.9; 302 -2.5; 332 -2.1; 365 -1.6; 402 -1.2; 442 -0.9; 486 -0.8; 535 -0.6; 588 -0.5; 647 -0.6; 712 -0.8; 783 -1.2; 861 -1.9; 947 -2.7; 1042 -3.4; 1146 -3.8; 1261 -4.1; 1387 -4.4; 1526 -5.0; 1678 -5.8; 1846 -6.5; 2031 -7.4; 2234 -8.3; 2457 -9.2; 2703 -10.4; 2973 -10.1; 3270 -8.7; 3597 -7.9; 3957 -8.4; 4353 -10.4; 4788 -14.5; 5267 -15.7; 5793 -9.2; 6373 -4.2; 7010 -3.4; 7711 -4.7; 8482 -4.9; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio X6 Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio X6 Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.09 | -4.5 dB  |
| Peaking | 64 Hz   | 1.03 | -2.8 dB  |
| Peaking | 540 Hz  | 0.73 | 4.7 dB   |
| Peaking | 2687 Hz | 1.71 | -5.4 dB  |
| Peaking | 5045 Hz | 5.23 | -11.6 dB |
| Peaking | 747 Hz  | 7.07 | 0.5 dB   |
| Peaking | 5540 Hz | 6.78 | -2.8 dB  |
| Peaking | 6589 Hz | 3.73 | 3.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | -6.8 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20X6%20Plus/MEE%20audio%20X6%20Plus.png)