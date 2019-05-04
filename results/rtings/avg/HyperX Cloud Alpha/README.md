# HyperX Cloud Alpha
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.8; 25 -6.9; 28 -7.0; 31 -7.0; 34 -7.0; 37 -6.9; 41 -6.8; 45 -6.8; 49 -6.7; 54 -6.6; 60 -6.6; 66 -6.6; 72 -6.7; 79 -6.9; 87 -7.2; 96 -7.5; 106 -7.8; 116 -8.1; 128 -8.4; 141 -8.5; 155 -8.6; 170 -8.5; 187 -8.4; 206 -8.4; 227 -8.2; 249 -8.0; 274 -8.0; 302 -8.2; 332 -8.2; 365 -7.8; 402 -7.3; 442 -7.0; 486 -6.8; 535 -6.5; 588 -6.0; 647 -5.7; 712 -5.4; 783 -5.2; 861 -5.1; 947 -5.1; 1042 -5.1; 1146 -5.3; 1261 -5.9; 1387 -6.6; 1526 -7.4; 1678 -8.2; 1846 -8.9; 2031 -9.2; 2234 -8.6; 2457 -7.7; 2703 -6.8; 2973 -6.1; 3270 -5.8; 3597 -4.4; 3957 -2.4; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -3.3; 6373 -3.8; 7010 -5.4; 7711 -9.1; 8482 -9.9; 9330 -8.9; 10263 -8.6; 11289 -6.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.6; 18182 -11.9; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Alpha GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Alpha ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 173 Hz   | 0.92 | -2.2 dB |
| Peaking | 2084 Hz  | 2.75 | -3.4 dB |
| Peaking | 4889 Hz  | 1.75 | 6.9 dB  |
| Peaking | 8443 Hz  | 2.7  | -4.6 dB |
| Peaking | 18362 Hz | 1.63 | -6.2 dB |
| Peaking | 348 Hz   | 2.5  | -1.0 dB |
| Peaking | 946 Hz   | 1.01 | 1.8 dB  |
| Peaking | 1629 Hz  | 3.15 | -1.3 dB |
| Peaking | 3206 Hz  | 5.81 | -1.0 dB |
| Peaking | 14544 Hz | 3.84 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Alpha/HyperX%20Cloud%20Alpha.png)