# Sennheiser HD 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.7; 31 -3.3; 34 -3.9; 37 -4.3; 41 -4.3; 45 -3.9; 49 -4.4; 54 -5.5; 60 -6.2; 66 -6.2; 72 -6.4; 79 -7.1; 87 -7.6; 96 -8.0; 106 -8.2; 116 -8.4; 128 -8.6; 141 -8.9; 155 -8.9; 170 -8.9; 187 -8.7; 206 -8.6; 227 -8.4; 249 -8.1; 274 -8.0; 302 -7.7; 332 -7.5; 365 -7.2; 402 -6.9; 442 -6.8; 486 -6.5; 535 -6.3; 588 -5.9; 647 -5.7; 712 -5.7; 783 -5.4; 861 -5.7; 947 -5.6; 1042 -5.8; 1146 -6.1; 1261 -6.2; 1387 -6.3; 1526 -6.5; 1678 -6.7; 1846 -7.0; 2031 -7.1; 2234 -7.0; 2457 -6.8; 2703 -6.7; 2973 -6.4; 3270 -5.9; 3597 -4.6; 3957 -3.8; 4353 -5.3; 4788 -5.4; 5267 -2.8; 5793 -2.9; 6373 -4.1; 7010 -3.8; 7711 -5.4; 8482 -5.8; 9330 -7.2; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.58 | 7.3 dB  |
| Peaking | 153 Hz  |  0.65 | -3.4 dB |
| Peaking | 2219 Hz |  1.5  | -1.5 dB |
| Peaking | 3870 Hz |  5.8  | 1.9 dB  |
| Peaking | 5616 Hz |  3.81 | 3.3 dB  |
| Peaking | 755 Hz  |  2.84 | 0.7 dB  |
| Peaking | 4618 Hz | 10.9  | -1.2 dB |
| Peaking | 6911 Hz |  9.29 | 1.5 dB  |
| Peaking | 9212 Hz |  7.45 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)