# MEE audio X6 Plus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.0; 25 -4.9; 28 -4.4; 31 -3.8; 34 -3.4; 37 -3.1; 41 -2.9; 45 -3.0; 49 -3.2; 54 -3.6; 60 -4.0; 66 -4.0; 72 -3.8; 79 -3.6; 87 -3.5; 96 -3.4; 106 -3.5; 116 -3.8; 128 -3.8; 141 -4.1; 155 -4.2; 170 -4.1; 187 -4.0; 206 -3.8; 227 -3.6; 249 -3.4; 274 -3.1; 302 -2.6; 332 -2.2; 365 -1.8; 402 -1.3; 442 -1.0; 486 -0.9; 535 -0.7; 588 -0.5; 647 -0.6; 712 -0.8; 783 -1.2; 861 -1.9; 947 -2.7; 1042 -3.4; 1146 -3.8; 1261 -4.1; 1387 -4.3; 1526 -5.0; 1678 -5.7; 1846 -6.3; 2031 -7.1; 2234 -7.5; 2457 -8.5; 2703 -10.0; 2973 -10.2; 3270 -9.1; 3597 -8.4; 3957 -8.8; 4353 -10.7; 4788 -14.1; 5267 -15.8; 5793 -9.6; 6373 -5.4; 7010 -3.5; 7711 -4.6; 8482 -4.8; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio X6 Plus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio X6 Plus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 53 Hz   | 0.59 | 1.4 dB   |
| Peaking | 568 Hz  | 0.85 | 4.5 dB   |
| Peaking | 2753 Hz | 1.7  | -4.8 dB  |
| Peaking | 5151 Hz | 3.29 | -11.9 dB |
| Peaking | 6663 Hz | 2.74 | 3.9 dB   |
| Peaking | 23 Hz   | 0.78 | -1.0 dB  |
| Peaking | 40 Hz   | 1.73 | 1.3 dB   |
| Peaking | 63 Hz   | 2.8  | -0.8 dB  |
| Peaking | 95 Hz   | 3.63 | 0.5 dB   |
| Peaking | 1804 Hz | 6.18 | -0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 4.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | -7.3 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20X6%20Plus/MEE%20audio%20X6%20Plus.png)