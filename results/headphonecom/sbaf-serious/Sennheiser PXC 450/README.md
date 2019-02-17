# Sennheiser PXC 450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.9; 25 -7.6; 28 -8.1; 31 -8.0; 34 -7.8; 37 -7.6; 41 -7.3; 45 -7.0; 49 -6.7; 54 -6.7; 60 -6.9; 66 -7.0; 72 -7.2; 79 -7.3; 87 -7.4; 96 -7.6; 106 -7.8; 116 -8.0; 128 -8.3; 141 -8.7; 155 -8.8; 170 -8.8; 187 -9.2; 206 -9.3; 227 -9.4; 249 -9.7; 274 -10.2; 302 -10.2; 332 -10.2; 365 -10.4; 402 -10.6; 442 -10.9; 486 -10.9; 535 -10.8; 588 -10.4; 647 -9.7; 712 -8.8; 783 -7.9; 861 -7.1; 947 -6.8; 1042 -6.2; 1146 -5.5; 1261 -5.2; 1387 -4.8; 1526 -5.8; 1678 -6.3; 1846 -4.6; 2031 -0.6; 2234 -0.5; 2457 -4.7; 2703 -8.4; 2973 -4.1; 3270 -1.3; 3597 -2.8; 3957 -1.0; 4353 -0.5; 4788 -0.7; 5267 -1.7; 5793 -1.5; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 231 Hz  |  0.67 | -2.8 dB |
| Peaking | 482 Hz  |  4.14 | 1.9 dB  |
| Peaking | 497 Hz  |  2.03 | -5.1 dB |
| Peaking | 2111 Hz |  5.98 | 6.2 dB  |
| Peaking | 4620 Hz |  1.46 | 6.2 dB  |
| Peaking | 30 Hz   |  2.65 | -1.4 dB |
| Peaking | 1242 Hz |  3.58 | 1.6 dB  |
| Peaking | 2665 Hz | 10.68 | -5.1 dB |
| Peaking | 3201 Hz |  8.91 | 2.7 dB  |
| Peaking | 8560 Hz |  4.27 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -4.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)