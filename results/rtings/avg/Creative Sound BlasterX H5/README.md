# Creative Sound BlasterX H5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -1.8; 25 -1.7; 28 -1.6; 31 -1.5; 34 -1.4; 37 -1.2; 41 -0.9; 45 -0.6; 49 -0.7; 54 -1.2; 60 -2.1; 66 -3.1; 72 -3.9; 79 -4.9; 87 -5.9; 96 -7.0; 106 -7.8; 116 -8.5; 128 -9.1; 141 -9.6; 155 -10.0; 170 -10.2; 187 -10.3; 206 -10.4; 227 -10.3; 249 -10.1; 274 -10.0; 302 -9.5; 332 -9.5; 365 -9.2; 402 -8.9; 442 -8.4; 486 -8.1; 535 -7.5; 588 -6.8; 647 -5.9; 712 -4.8; 783 -3.6; 861 -2.3; 947 -1.4; 1042 -0.6; 1146 -0.5; 1261 -0.5; 1387 -0.6; 1526 -1.3; 1678 -2.1; 1846 -3.6; 2031 -5.7; 2234 -7.3; 2457 -7.9; 2703 -8.2; 2973 -8.3; 3270 -9.0; 3597 -7.6; 3957 -2.9; 4353 -0.9; 4788 -1.0; 5267 -5.8; 5793 -7.3; 6373 -5.8; 7010 -8.1; 7711 -9.8; 8482 -8.7; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Sound BlasterX H5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Sound BlasterX H5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.88 | 3.2 dB  |
| Peaking | 52 Hz   | 0.83 | 6.6 dB  |
| Peaking | 175 Hz  | 0.43 | -4.8 dB |
| Peaking | 1127 Hz | 1.49 | 7.4 dB  |
| Peaking | 4512 Hz | 6.67 | 6.7 dB  |
| Peaking | 1637 Hz | 3.79 | 2.7 dB  |
| Peaking | 3074 Hz | 1.47 | -3.7 dB |
| Peaking | 4050 Hz | 5.15 | 4.0 dB  |
| Peaking | 7833 Hz | 5.13 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Sound%20BlasterX%20H5/Creative%20Sound%20BlasterX%20H5.png)