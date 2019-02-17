# Oppo PM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.5; 25 -3.8; 28 -4.1; 31 -4.3; 34 -4.5; 37 -4.5; 41 -4.4; 45 -4.0; 49 -3.4; 54 -4.5; 60 -6.2; 66 -6.4; 72 -6.5; 79 -6.9; 87 -7.2; 96 -7.6; 106 -7.8; 116 -8.0; 128 -8.1; 141 -8.4; 155 -8.6; 170 -8.6; 187 -8.8; 206 -8.6; 227 -8.4; 249 -8.4; 274 -8.8; 302 -8.8; 332 -8.6; 365 -7.7; 402 -6.8; 442 -6.8; 486 -7.5; 535 -7.7; 588 -7.5; 647 -7.3; 712 -7.5; 783 -7.7; 861 -7.9; 947 -7.0; 1042 -6.0; 1146 -5.5; 1261 -5.4; 1387 -6.6; 1526 -6.4; 1678 -6.4; 1846 -5.7; 2031 -5.3; 2234 -4.7; 2457 -3.8; 2703 -3.6; 2973 -3.4; 3270 -3.4; 3597 -3.4; 3957 -3.4; 4353 -3.2; 4788 -2.0; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.5; 9330 -8.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.43 | 3.7 dB  |
| Peaking | 134 Hz  | 0.35 | -3.0 dB |
| Peaking | 2928 Hz | 1.58 | 2.6 dB  |
| Peaking | 5730 Hz | 1.98 | 6.2 dB  |
| Peaking | 8878 Hz | 3.29 | -3.5 dB |
| Peaking | 310 Hz  | 5.13 | -0.7 dB |
| Peaking | 414 Hz  | 5.93 | 1.4 dB  |
| Peaking | 869 Hz  | 2.36 | -1.9 dB |
| Peaking | 1148 Hz | 1.97 | 2.3 dB  |
| Peaking | 1469 Hz | 2.81 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Oppo%20PM1/Oppo%20PM1.png)