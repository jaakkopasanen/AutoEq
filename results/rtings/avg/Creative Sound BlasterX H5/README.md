# Creative Sound BlasterX H5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.4; 25 -2.2; 28 -2.1; 31 -2.2; 34 -2.2; 37 -1.9; 41 -1.4; 45 -1.2; 49 -1.2; 54 -1.7; 60 -2.8; 66 -3.8; 72 -4.7; 79 -5.6; 87 -6.4; 96 -7.2; 106 -7.9; 116 -8.5; 128 -8.9; 141 -9.4; 155 -9.8; 170 -10.0; 187 -10.2; 206 -10.4; 227 -10.5; 249 -10.6; 274 -10.5; 302 -9.9; 332 -10.0; 365 -9.7; 402 -9.3; 442 -8.9; 486 -8.5; 535 -7.8; 588 -7.1; 647 -6.2; 712 -5.1; 783 -3.9; 861 -2.7; 947 -1.6; 1042 -1.0; 1146 -0.6; 1261 -0.5; 1387 -0.8; 1526 -1.5; 1678 -2.4; 1846 -3.8; 2031 -5.7; 2234 -6.9; 2457 -7.4; 2703 -8.1; 2973 -8.6; 3270 -9.6; 3597 -8.5; 3957 -3.7; 4353 -1.7; 4788 -0.9; 5267 -6.0; 5793 -7.9; 6373 -7.2; 7010 -8.4; 7711 -9.5; 8482 -9.6; 9330 -9.0; 10263 -6.4; 11289 -2.6; 12418 -2.2; 13660 -5.1; 15026 -4.7; 16529 -1.9; 18182 -3.7; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Sound BlasterX H5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Sound BlasterX H5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 174 Hz   | 0.65 | -8.6 dB  |
| Peaking | 419 Hz   | 1.25 | -5.2 dB  |
| Peaking | 2899 Hz  | 2.14 | -7.8 dB  |
| Peaking | 8106 Hz  | 1.5  | -8.7 dB  |
| Peaking | 20001 Hz | 1.19 | -10.6 dB |
| Peaking | 1239 Hz  | 1.32 | 5.9 dB   |
| Peaking | 1356 Hz  | 0.61 | -3.6 dB  |
| Peaking | 4722 Hz  | 4.02 | 5.1 dB   |
| Peaking | 5517 Hz  | 6.75 | -4.8 dB  |
| Peaking | 17355 Hz | 5.28 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB |
| Peaking | 500 Hz   | 1.41 | -6.8 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | -8.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Sound%20BlasterX%20H5/Creative%20Sound%20BlasterX%20H5.png)