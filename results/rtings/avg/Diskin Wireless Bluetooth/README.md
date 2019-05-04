# Diskin Wireless Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -4.1; 25 -6.1; 28 -8.4; 31 -9.9; 34 -10.6; 37 -10.7; 41 -10.1; 45 -9.4; 49 -8.8; 54 -8.3; 60 -7.9; 66 -7.7; 72 -7.6; 79 -7.6; 87 -7.7; 96 -7.9; 106 -8.0; 116 -8.3; 128 -8.5; 141 -8.7; 155 -8.8; 170 -8.8; 187 -8.8; 206 -8.7; 227 -8.6; 249 -8.6; 274 -8.6; 302 -8.5; 332 -8.3; 365 -7.7; 402 -7.3; 442 -6.2; 486 -4.6; 535 -3.7; 588 -3.3; 647 -3.4; 712 -3.8; 783 -4.3; 861 -4.9; 947 -5.8; 1042 -6.8; 1146 -7.5; 1261 -8.5; 1387 -9.6; 1526 -10.5; 1678 -10.3; 1846 -9.2; 2031 -7.9; 2234 -7.0; 2457 -5.4; 2703 -4.2; 2973 -4.2; 3270 -4.6; 3597 -4.4; 3957 -3.5; 4353 -2.6; 4788 -1.2; 5267 -0.5; 5793 -0.7; 6373 -1.4; 7010 -5.1; 7711 -7.3; 8482 -7.0; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Diskin Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Diskin Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 2.38 | -4.5 dB |
| Peaking | 258 Hz  | 0.43 | -3.1 dB |
| Peaking | 609 Hz  | 1.43 | 5.1 dB  |
| Peaking | 1550 Hz | 2.57 | -4.9 dB |
| Peaking | 5152 Hz | 1.93 | 6.1 dB  |
| Peaking | 51 Hz   | 2.71 | -0.2 dB |
| Peaking | 2591 Hz | 1.32 | -1.5 dB |
| Peaking | 2756 Hz | 2.95 | 3.4 dB  |
| Peaking | 6311 Hz | 5.76 | 2.8 dB  |
| Peaking | 7701 Hz | 3    | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Diskin%20Wireless%20Bluetooth/Diskin%20Wireless%20Bluetooth.png)