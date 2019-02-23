# Sennheiser PXC 450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -7.5; 25 -8.2; 28 -8.6; 31 -8.5; 34 -8.4; 37 -8.2; 41 -7.9; 45 -7.5; 49 -7.3; 54 -7.2; 60 -7.4; 66 -7.6; 72 -7.8; 79 -7.8; 87 -8.0; 96 -8.2; 106 -8.4; 116 -8.6; 128 -8.9; 141 -9.3; 155 -9.4; 170 -9.3; 187 -9.7; 206 -9.9; 227 -9.9; 249 -10.2; 274 -10.7; 302 -10.8; 332 -10.8; 365 -10.9; 402 -11.1; 442 -11.4; 486 -11.5; 535 -11.3; 588 -11.0; 647 -10.2; 712 -9.3; 783 -8.4; 861 -7.6; 947 -7.4; 1042 -6.7; 1146 -6.1; 1261 -5.7; 1387 -5.3; 1526 -6.4; 1678 -6.8; 1846 -5.2; 2031 -0.6; 2234 -0.5; 2457 -5.2; 2703 -8.9; 2973 -4.6; 3270 -1.8; 3597 -3.3; 3957 -1.5; 4353 -0.5; 4788 -1.0; 5267 -2.3; 5793 -2.1; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 39 Hz   |  0.09 | -1.0 dB |
| Peaking | 1152 Hz |  0.94 | 7.8 dB  |
| Peaking | 1405 Hz |  0.21 | -8.2 dB |
| Peaking | 2125 Hz |  5.14 | 8.8 dB  |
| Peaking | 4438 Hz |  0.97 | 11.0 dB |
| Peaking | 31 Hz   |  3.06 | -0.9 dB |
| Peaking | 2670 Hz | 12.71 | -4.4 dB |
| Peaking | 3203 Hz |  9.48 | 3.0 dB  |
| Peaking | 6460 Hz |  3.81 | 4.6 dB  |
| Peaking | 6632 Hz |  1.93 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -4.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)