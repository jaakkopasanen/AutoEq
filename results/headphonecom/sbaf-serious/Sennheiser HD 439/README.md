# Sennheiser HD 439
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.8; 25 -9.0; 28 -9.3; 31 -9.6; 34 -9.8; 37 -9.9; 41 -10.1; 45 -10.3; 49 -10.4; 54 -10.5; 60 -10.6; 66 -10.6; 72 -10.5; 79 -10.1; 87 -10.9; 96 -10.1; 106 -7.6; 116 -9.2; 128 -11.1; 141 -11.6; 155 -11.6; 170 -11.3; 187 -11.3; 206 -11.5; 227 -11.7; 249 -11.5; 274 -11.0; 302 -10.1; 332 -10.2; 365 -8.5; 402 -8.5; 442 -8.4; 486 -7.9; 535 -7.9; 588 -8.2; 647 -8.6; 712 -8.4; 783 -8.7; 861 -9.1; 947 -9.6; 1042 -8.7; 1146 -8.8; 1261 -8.5; 1387 -10.1; 1526 -10.5; 1678 -10.2; 1846 -9.3; 2031 -7.8; 2234 -5.9; 2457 -4.2; 2703 -3.6; 2973 -3.0; 3270 -2.6; 3597 -2.4; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -1.2; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 439 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.61 | -3.7 dB |
| Peaking | 210 Hz  | 0.91 | -4.8 dB |
| Peaking | 899 Hz  | 1.85 | -2.2 dB |
| Peaking | 1612 Hz | 2.59 | -4.7 dB |
| Peaking | 4450 Hz | 1.1  | 6.5 dB  |
| Peaking | 108 Hz  | 2.28 | -2.6 dB |
| Peaking | 109 Hz  | 6.01 | 5.2 dB  |
| Peaking | 2597 Hz | 5.23 | 1.4 dB  |
| Peaking | 6290 Hz | 3.25 | 5.1 dB  |
| Peaking | 7066 Hz | 1.33 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)