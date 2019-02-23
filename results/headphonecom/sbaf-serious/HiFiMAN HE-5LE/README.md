# HiFiMAN HE-5LE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.1; 28 -4.3; 31 -4.3; 34 -4.2; 37 -4.0; 41 -3.9; 45 -3.9; 49 -4.0; 54 -4.1; 60 -4.1; 66 -4.0; 72 -4.3; 79 -4.5; 87 -4.6; 96 -5.0; 106 -5.2; 116 -5.4; 128 -6.0; 141 -6.7; 155 -7.5; 170 -8.1; 187 -8.3; 206 -8.3; 227 -8.5; 249 -8.7; 274 -8.7; 302 -8.6; 332 -8.5; 365 -8.5; 402 -8.6; 442 -8.5; 486 -8.7; 535 -9.7; 588 -8.6; 647 -5.2; 712 -3.9; 783 -3.6; 861 -4.6; 947 -5.1; 1042 -4.6; 1146 -3.1; 1261 -2.6; 1387 -1.9; 1526 -1.9; 1678 -1.3; 1846 -0.5; 2031 -1.4; 2234 -2.9; 2457 -1.6; 2703 -1.6; 2973 -3.4; 3270 -3.4; 3597 -2.0; 3957 -4.3; 4353 -7.8; 4788 -8.6; 5267 -5.0; 5793 -6.4; 6373 -9.2; 7010 -8.2; 7711 -8.8; 8482 -11.3; 9330 -12.1; 10263 -7.3; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.4; 18182 -6.9; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-5LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 511 Hz   | 0.6  | -4.1 dB |
| Peaking | 735 Hz   | 3.29 | 4.9 dB  |
| Peaking | 1570 Hz  | 1.15 | 5.6 dB  |
| Peaking | 2779 Hz  | 2.23 | 2.6 dB  |
| Peaking | 8726 Hz  | 2.62 | -6.1 dB |
| Peaking | 21 Hz    | 0.64 | 2.2 dB  |
| Peaking | 68 Hz    | 1.47 | 1.8 dB  |
| Peaking | 3655 Hz  | 9.43 | 3.1 dB  |
| Peaking | 4505 Hz  | 7.09 | -3.7 dB |
| Peaking | 10929 Hz | 6.05 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5LE/HiFiMAN%20HE-5LE.png)