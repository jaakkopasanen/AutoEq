# Sennheiser PXC300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.6; 72 -2.3; 79 -1.8; 87 -2.5; 96 -3.6; 106 -4.2; 116 -4.5; 128 -4.7; 141 -5.1; 155 -5.3; 170 -5.2; 187 -5.1; 206 -4.6; 227 -4.6; 249 -4.6; 274 -4.8; 302 -4.7; 332 -4.4; 365 -4.1; 402 -4.0; 442 -4.1; 486 -4.0; 535 -3.8; 588 -3.9; 647 -4.0; 712 -4.4; 783 -4.9; 861 -5.6; 947 -6.4; 1042 -7.2; 1146 -8.0; 1261 -8.6; 1387 -9.2; 1526 -9.4; 1678 -9.3; 1846 -8.8; 2031 -8.8; 2234 -9.4; 2457 -9.4; 2703 -8.3; 2973 -7.0; 3270 -6.1; 3597 -5.7; 3957 -5.4; 4353 -6.5; 4788 -9.2; 5267 -7.5; 5793 -5.7; 6373 -7.7; 7010 -10.5; 7711 -9.3; 8482 -9.4; 9330 -13.0; 10263 -14.8; 11289 -8.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.48 | 6.6 dB  |
| Peaking | 550 Hz   | 0.76 | 2.9 dB  |
| Peaking | 1424 Hz  | 1.5  | -3.6 dB |
| Peaking | 2346 Hz  | 4.51 | -2.4 dB |
| Peaking | 9837 Hz  | 3.24 | -8.7 dB |
| Peaking | 36 Hz    | 3.38 | -0.7 dB |
| Peaking | 4869 Hz  | 4.96 | -6.8 dB |
| Peaking | 4883 Hz  | 1.87 | 4.3 dB  |
| Peaking | 6966 Hz  | 5.71 | -4.2 dB |
| Peaking | 12024 Hz | 6.31 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC300/Sennheiser%20PXC300.png)