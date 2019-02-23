# Sennheiser PXC 450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.9; 25 -9.9; 28 -9.4; 31 -8.7; 34 -8.2; 37 -7.8; 41 -7.6; 45 -7.4; 49 -7.4; 54 -7.3; 60 -7.3; 66 -7.4; 72 -7.6; 79 -7.9; 87 -8.2; 96 -8.5; 106 -8.9; 116 -9.3; 128 -9.6; 141 -9.8; 155 -9.8; 170 -9.6; 187 -9.1; 206 -8.5; 227 -8.5; 249 -8.9; 274 -9.4; 302 -9.9; 332 -10.1; 365 -10.6; 402 -11.0; 442 -11.4; 486 -11.8; 535 -12.1; 588 -12.2; 647 -12.1; 712 -11.7; 783 -11.0; 861 -10.0; 947 -9.0; 1042 -8.3; 1146 -7.4; 1261 -6.8; 1387 -6.2; 1526 -5.2; 1678 -3.9; 1846 -0.5; 2031 -0.5; 2234 -0.6; 2457 -6.7; 2703 -9.1; 2973 -2.9; 3270 -2.3; 3597 -5.4; 3957 -1.4; 4353 -0.5; 4788 -0.5; 5267 -1.5; 5793 -5.4; 6373 -4.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.8; 12418 -12.6; 13660 -12.3; 15026 -9.6; 16529 -11.8; 18182 -16.2; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 479 Hz   |  0.28 | -4.5 dB |
| Peaking | 1897 Hz  |  2.58 | 8.2 dB  |
| Peaking | 4615 Hz  |  1.88 | 6.8 dB  |
| Peaking | 18867 Hz |  0.5  | -9.4 dB |
| Peaking | 22050 Hz |  0.84 | -3.9 dB |
| Peaking | 23 Hz    |  1.45 | -3.3 dB |
| Peaking | 239 Hz   |  3.01 | 1.9 dB  |
| Peaking | 593 Hz   |  3.24 | -1.8 dB |
| Peaking | 2617 Hz  | 13.66 | -5.6 dB |
| Peaking | 12867 Hz |  7.35 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -5.8 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -8.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)