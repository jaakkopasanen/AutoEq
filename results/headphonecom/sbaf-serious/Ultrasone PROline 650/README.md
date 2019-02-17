# Ultrasone PROline 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -6.3; 25 -6.8; 28 -7.4; 31 -7.8; 34 -8.2; 37 -8.5; 41 -8.6; 45 -8.0; 49 -6.4; 54 -5.3; 60 -7.2; 66 -8.9; 72 -9.8; 79 -10.0; 87 -9.3; 96 -9.2; 106 -9.2; 116 -8.2; 128 -7.9; 141 -8.1; 155 -7.6; 170 -6.6; 187 -6.0; 206 -4.9; 227 -3.9; 249 -2.7; 274 -1.5; 302 -1.3; 332 -1.8; 365 -2.4; 402 -3.5; 442 -4.1; 486 -3.5; 535 -0.5; 588 -3.4; 647 -4.5; 712 -4.7; 783 -5.0; 861 -5.4; 947 -5.8; 1042 -6.3; 1146 -6.4; 1261 -6.4; 1387 -7.0; 1526 -8.1; 1678 -9.0; 1846 -8.9; 2031 -7.6; 2234 -1.7; 2457 -2.0; 2703 -7.5; 2973 -7.6; 3270 -8.3; 3597 -9.8; 3957 -10.0; 4353 -9.2; 4788 -6.5; 5267 -6.7; 5793 -2.6; 6373 -6.7; 7010 -5.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -7.1; 15026 -13.6; 16529 -13.0; 18182 -6.5; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PROline 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PROline 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 93 Hz    |  0.88 | -3.5 dB |
| Peaking | 295 Hz   |  1.73 | 5.4 dB  |
| Peaking | 537 Hz   |  5.64 | 4.8 dB  |
| Peaking | 3818 Hz  |  4.23 | -4.5 dB |
| Peaking | 15761 Hz |  2.75 | -9.5 dB |
| Peaking | 45 Hz    |  1.54 | -2.6 dB |
| Peaking | 52 Hz    |  4.27 | 4.9 dB  |
| Peaking | 2070 Hz  |  1.81 | -4.4 dB |
| Peaking | 2313 Hz  |  6.53 | 10.6 dB |
| Peaking | 5837 Hz  | 10.19 | 4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -7.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20PROline%20650/Ultrasone%20PROline%20650.png)