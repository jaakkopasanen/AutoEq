# Sennheiser HD 558
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.3; 37 -1.8; 41 -2.5; 45 -3.0; 49 -3.5; 54 -4.1; 60 -4.6; 66 -5.0; 72 -5.2; 79 -5.7; 87 -4.6; 96 -5.8; 106 -7.1; 116 -7.5; 128 -7.8; 141 -8.2; 155 -8.6; 170 -8.7; 187 -8.8; 206 -8.6; 227 -8.7; 249 -8.8; 274 -8.8; 302 -8.7; 332 -8.4; 365 -8.2; 402 -8.1; 442 -7.9; 486 -7.8; 535 -7.5; 588 -6.9; 647 -6.9; 712 -7.0; 783 -6.4; 861 -6.4; 947 -6.4; 1042 -6.7; 1146 -6.5; 1261 -6.7; 1387 -6.9; 1526 -6.9; 1678 -6.7; 1846 -7.5; 2031 -8.3; 2234 -8.4; 2457 -8.0; 2703 -9.3; 2973 -9.7; 3270 -10.2; 3597 -8.8; 3957 -7.8; 4353 -10.1; 4788 -9.7; 5267 -7.3; 5793 -5.2; 6373 -4.2; 7010 -5.4; 7711 -6.2; 8482 -6.7; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.4; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 558 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 558 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.5  | 6.2 dB  |
| Peaking | 208 Hz   | 0.71 | -2.8 dB |
| Peaking | 3001 Hz  | 2.01 | -3.3 dB |
| Peaking | 4665 Hz  | 5.08 | -3.5 dB |
| Peaking | 6248 Hz  | 4.26 | 2.9 dB  |
| Peaking | 90 Hz    | 1.81 | -1.0 dB |
| Peaking | 91 Hz    | 5.66 | 2.5 dB  |
| Peaking | 883 Hz   | 3.09 | 0.6 dB  |
| Peaking | 2088 Hz  | 9.84 | -1.0 dB |
| Peaking | 19345 Hz | 1.5  | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20558/Sennheiser%20HD%20558.png)