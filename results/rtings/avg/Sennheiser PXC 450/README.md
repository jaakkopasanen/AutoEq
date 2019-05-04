# Sennheiser PXC 450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.5; 25 -9.4; 28 -9.1; 31 -8.6; 34 -8.1; 37 -7.7; 41 -7.4; 45 -7.3; 49 -7.2; 54 -7.2; 60 -7.1; 66 -7.2; 72 -7.4; 79 -7.6; 87 -7.9; 96 -8.3; 106 -8.7; 116 -9.1; 128 -9.4; 141 -9.5; 155 -9.6; 170 -9.4; 187 -8.9; 206 -8.4; 227 -8.4; 249 -8.8; 274 -9.3; 302 -9.8; 332 -10.1; 365 -10.5; 402 -11.0; 442 -11.4; 486 -11.8; 535 -12.1; 588 -12.3; 647 -12.2; 712 -11.8; 783 -11.1; 861 -10.1; 947 -9.2; 1042 -8.4; 1146 -7.6; 1261 -7.0; 1387 -6.4; 1526 -5.6; 1678 -4.0; 1846 -0.5; 2031 -0.5; 2234 -0.6; 2457 -7.5; 2703 -9.6; 2973 -3.2; 3270 -2.0; 3597 -5.0; 3957 -1.3; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -5.3; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.9; 12418 -12.7; 13660 -11.5; 15026 -9.1; 16529 -11.5; 18182 -15.9; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 489 Hz   |  0.39 | -4.8 dB |
| Peaking | 1911 Hz  |  3.21 | 7.9 dB  |
| Peaking | 4626 Hz  |  1.82 | 6.6 dB  |
| Peaking | 18900 Hz |  0.51 | -9.0 dB |
| Peaking | 22050 Hz |  0.93 | -3.6 dB |
| Peaking | 251 Hz   |  2.89 | 1.6 dB  |
| Peaking | 615 Hz   |  3.74 | -1.6 dB |
| Peaking | 2617 Hz  | 12.37 | -5.9 dB |
| Peaking | 18318 Hz |  4.42 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -5.8 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -7.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)