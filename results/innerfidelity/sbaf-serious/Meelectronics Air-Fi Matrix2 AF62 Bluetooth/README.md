# Meelectronics Air-Fi Matrix2 AF62 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.5; 31 -2.8; 34 -4.1; 37 -5.1; 41 -6.2; 45 -7.0; 49 -7.6; 54 -8.2; 60 -8.6; 66 -8.7; 72 -8.8; 79 -8.7; 87 -8.6; 96 -8.7; 106 -8.4; 116 -8.2; 128 -8.3; 141 -8.4; 155 -8.6; 170 -8.3; 187 -8.2; 206 -8.5; 227 -8.2; 249 -8.0; 274 -8.4; 302 -8.5; 332 -8.5; 365 -8.5; 402 -8.5; 442 -8.3; 486 -8.6; 535 -8.8; 588 -8.7; 647 -8.6; 712 -8.6; 783 -7.8; 861 -6.9; 947 -6.8; 1042 -6.9; 1146 -7.0; 1261 -6.9; 1387 -7.2; 1526 -7.2; 1678 -6.7; 1846 -5.3; 2031 -4.6; 2234 -4.1; 2457 -3.8; 2703 -3.5; 2973 -4.1; 3270 -4.8; 3597 -4.2; 3957 -2.7; 4353 -1.9; 4788 -0.5; 5267 -3.1; 5793 -4.6; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -7.5; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meelectronics Air-Fi Matrix2 AF62 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meelectronics Air-Fi Matrix2 AF62 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.52 | 8.6 dB  |
| Peaking | 108 Hz   | 0.11 | -2.3 dB |
| Peaking | 2408 Hz  | 2.23 | 2.8 dB  |
| Peaking | 4697 Hz  | 2.22 | 5.5 dB  |
| Peaking | 22050 Hz | 2.24 | 1.4 dB  |
| Peaking | 60 Hz    | 3.72 | -0.7 dB |
| Peaking | 712 Hz   | 2.15 | -1.1 dB |
| Peaking | 871 Hz   | 3.21 | 1.5 dB  |
| Peaking | 6668 Hz  | 6.19 | 4.5 dB  |
| Peaking | 7435 Hz  | 1.35 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Bluetooth/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Bluetooth.png)