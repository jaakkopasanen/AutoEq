# Sennheiser PXC 150
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.3; 60 -3.1; 66 -4.6; 72 -5.7; 79 -6.5; 87 -6.3; 96 -5.8; 106 -6.2; 116 -6.9; 128 -7.2; 141 -7.2; 155 -7.0; 170 -6.3; 187 -6.1; 206 -6.2; 227 -6.2; 249 -6.1; 274 -5.7; 302 -5.6; 332 -5.1; 365 -5.0; 402 -4.8; 442 -4.8; 486 -4.6; 535 -4.5; 588 -4.7; 647 -4.9; 712 -5.1; 783 -5.6; 861 -6.1; 947 -6.8; 1042 -7.7; 1146 -8.4; 1261 -9.3; 1387 -9.8; 1526 -11.2; 1678 -12.1; 1846 -12.6; 2031 -12.5; 2234 -10.5; 2457 -8.9; 2703 -7.1; 2973 -5.6; 3270 -4.0; 3597 -2.7; 3957 -3.1; 4353 -7.1; 4788 -7.4; 5267 -5.7; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -11.1; 9330 -14.0; 10263 -13.3; 11289 -8.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 150 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.94 | 7.0 dB  |
| Peaking | 1836 Hz | 2.08 | -6.8 dB |
| Peaking | 3550 Hz | 4.3  | 4.9 dB  |
| Peaking | 6309 Hz | 4.33 | 7.2 dB  |
| Peaking | 9547 Hz | 3.14 | -8.8 dB |
| Peaking | 50 Hz   | 4.13 | 2.4 dB  |
| Peaking | 77 Hz   | 4.09 | -1.7 dB |
| Peaking | 131 Hz  | 3.06 | -1.4 dB |
| Peaking | 500 Hz  | 1.26 | 2.3 dB  |
| Peaking | 4673 Hz | 7.94 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC%20150/Sennheiser%20PXC%20150.png)