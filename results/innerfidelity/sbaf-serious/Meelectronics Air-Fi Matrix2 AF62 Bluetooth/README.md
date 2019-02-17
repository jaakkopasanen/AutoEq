# Meelectronics Air-Fi Matrix2 AF62 Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -2.5; 34 -3.8; 37 -4.8; 41 -5.9; 45 -6.7; 49 -7.3; 54 -7.9; 60 -8.3; 66 -8.5; 72 -8.5; 79 -8.4; 87 -8.3; 96 -8.4; 106 -8.1; 116 -7.9; 128 -8.0; 141 -8.1; 155 -8.3; 170 -8.0; 187 -8.0; 206 -8.2; 227 -7.9; 249 -7.7; 274 -8.2; 302 -8.2; 332 -8.2; 365 -8.2; 402 -8.2; 442 -8.0; 486 -8.3; 535 -8.5; 588 -8.4; 647 -8.3; 712 -8.3; 783 -7.5; 861 -6.6; 947 -6.5; 1042 -6.6; 1146 -6.7; 1261 -6.6; 1387 -6.9; 1526 -6.9; 1678 -6.4; 1846 -5.1; 2031 -4.3; 2234 -3.8; 2457 -3.6; 2703 -3.2; 2973 -3.8; 3270 -4.5; 3597 -3.9; 3957 -2.4; 4353 -1.6; 4788 -0.5; 5267 -2.9; 5793 -4.3; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -7.2; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meelectronics Air-Fi Matrix2 AF62 Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meelectronics Air-Fi Matrix2 AF62 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.52 | 8.3 dB  |
| Peaking | 103 Hz   | 0.11 | -2.0 dB |
| Peaking | 2406 Hz  | 2.18 | 2.9 dB  |
| Peaking | 4715 Hz  | 1.99 | 5.4 dB  |
| Peaking | 22050 Hz | 2.29 | 1.5 dB  |
| Peaking | 64 Hz    | 3.38 | -0.8 dB |
| Peaking | 698 Hz   | 2.28 | -1.1 dB |
| Peaking | 880 Hz   | 3.1  | 1.4 dB  |
| Peaking | 6622 Hz  | 6.41 | 4.5 dB  |
| Peaking | 7235 Hz  | 1.45 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Bluetooth/Meelectronics%20Air-Fi%20Matrix2%20AF62%20Bluetooth.png)