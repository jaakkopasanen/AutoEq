# AKG K701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.3; 34 -1.7; 37 -2.0; 41 -2.3; 45 -2.6; 49 -2.9; 54 -3.2; 60 -3.5; 66 -3.9; 72 -4.2; 79 -4.6; 87 -5.0; 96 -5.4; 106 -5.9; 116 -6.3; 128 -6.7; 141 -7.1; 155 -7.3; 170 -7.5; 187 -7.6; 206 -7.6; 227 -7.6; 249 -7.5; 274 -7.7; 302 -7.7; 332 -7.7; 365 -7.7; 402 -7.8; 442 -7.8; 486 -7.6; 535 -6.9; 588 -6.1; 647 -6.1; 712 -5.6; 783 -5.6; 861 -5.8; 947 -6.2; 1042 -6.7; 1146 -7.1; 1261 -7.4; 1387 -7.9; 1526 -8.4; 1678 -9.7; 1846 -11.5; 2031 -12.5; 2234 -13.4; 2457 -12.8; 2703 -12.0; 2973 -11.0; 3270 -10.2; 3597 -9.4; 3957 -9.3; 4353 -9.2; 4788 -9.3; 5267 -10.2; 5793 -11.7; 6373 -13.8; 7010 -14.3; 7711 -14.3; 8482 -14.4; 9330 -11.5; 10263 -9.3; 11289 -11.8; 12418 -11.8; 13660 -7.3; 15026 -6.5; 16529 -10.1; 18182 -15.3; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.71 | 6.0 dB   |
| Peaking | 2293 Hz  | 1.81 | -6.7 dB  |
| Peaking | 6958 Hz  | 2.08 | -4.1 dB  |
| Peaking | 8376 Hz  | 1.03 | -4.5 dB  |
| Peaking | 18996 Hz | 1.16 | -10.3 dB |
| Peaking | 73 Hz    | 1.31 | 1.4 dB   |
| Peaking | 297 Hz   | 0.33 | -1.6 dB  |
| Peaking | 769 Hz   | 1.46 | 2.3 dB   |
| Peaking | 12095 Hz | 6.08 | -4.0 dB  |
| Peaking | 14646 Hz | 2.81 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -8.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K701/AKG%20K701.png)