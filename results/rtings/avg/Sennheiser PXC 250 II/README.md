# Sennheiser PXC 250 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -1.8; 60 -2.7; 66 -3.3; 72 -3.8; 79 -4.3; 87 -4.7; 96 -5.1; 106 -5.3; 116 -5.5; 128 -5.7; 141 -5.7; 155 -5.6; 170 -5.6; 187 -5.5; 206 -5.3; 227 -5.0; 249 -4.9; 274 -4.9; 302 -4.8; 332 -4.7; 365 -4.6; 402 -4.5; 442 -4.4; 486 -4.4; 535 -4.1; 588 -4.0; 647 -3.9; 712 -3.8; 783 -4.0; 861 -4.3; 947 -5.0; 1042 -6.1; 1146 -7.4; 1261 -9.1; 1387 -10.7; 1526 -11.9; 1678 -11.8; 1846 -12.7; 2031 -13.0; 2234 -12.3; 2457 -11.4; 2703 -10.2; 2973 -9.3; 3270 -8.2; 3597 -5.9; 3957 -2.6; 4353 -0.5; 4788 -2.3; 5267 -3.3; 5793 -2.1; 6373 -4.0; 7010 -8.8; 7711 -11.4; 8482 -10.8; 9330 -10.3; 10263 -13.0; 11289 -14.1; 12418 -8.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 250 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 250 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 31 Hz    |  0.67 | 6.6 dB   |
| Peaking | 905 Hz   |  0.59 | 9.1 dB   |
| Peaking | 1743 Hz  |  0.53 | -12.2 dB |
| Peaking | 4518 Hz  |  1.48 | 10.1 dB  |
| Peaking | 10197 Hz |  1.63 | -6.9 dB  |
| Peaking | 1717 Hz  | 11.92 | 0.5 dB   |
| Peaking | 6089 Hz  |  8.12 | 3.4 dB   |
| Peaking | 7519 Hz  |  6.15 | -3.4 dB  |
| Peaking | 13019 Hz |  8.73 | 2.3 dB   |
| Peaking | 14607 Hz |  3.46 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20250%20II/Sennheiser%20PXC%20250%20II.png)