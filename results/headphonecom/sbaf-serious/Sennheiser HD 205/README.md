# Sennheiser HD 205
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.7; 25 -0.9; 28 -1.3; 31 -1.7; 34 -2.2; 37 -2.6; 41 -2.9; 45 -3.0; 49 -3.4; 54 -4.2; 60 -4.6; 66 -4.6; 72 -4.6; 79 -5.5; 87 -6.1; 96 -6.6; 106 -6.9; 116 -7.1; 128 -7.3; 141 -6.7; 155 -5.8; 170 -6.5; 187 -6.6; 206 -6.1; 227 -5.5; 249 -5.9; 274 -5.7; 302 -5.3; 332 -4.7; 365 -3.6; 402 -2.5; 442 -2.4; 486 -4.0; 535 -5.7; 588 -5.9; 647 -4.3; 712 -2.1; 783 -2.8; 861 -4.6; 947 -6.0; 1042 -6.9; 1146 -7.4; 1261 -7.8; 1387 -8.2; 1526 -8.7; 1678 -8.8; 1846 -8.3; 2031 -7.7; 2234 -6.7; 2457 -5.3; 2703 -3.4; 2973 -3.0; 3270 -2.3; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -3.4; 5267 -6.2; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 205 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 205 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.81 | 5.8 dB  |
| Peaking | 411 Hz   | 3.35 | 4.4 dB  |
| Peaking | 741 Hz   | 5.71 | 4.5 dB  |
| Peaking | 4013 Hz  | 1.84 | 6.4 dB  |
| Peaking | 22050 Hz | 2.48 | 2.6 dB  |
| Peaking | 117 Hz   | 3.79 | -1.3 dB |
| Peaking | 1671 Hz  | 1.78 | -3.1 dB |
| Peaking | 2798 Hz  | 3.9  | 1.8 dB  |
| Peaking | 5150 Hz  | 8.88 | -4.7 dB |
| Peaking | 6131 Hz  | 5.07 | 5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20205/Sennheiser%20HD%20205.png)