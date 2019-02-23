# Diskin Wireless Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -4.5; 25 -6.5; 28 -8.9; 31 -10.5; 34 -11.2; 37 -11.1; 41 -10.5; 45 -9.8; 49 -9.2; 54 -8.7; 60 -8.3; 66 -8.1; 72 -8.0; 79 -8.1; 87 -8.2; 96 -8.3; 106 -8.5; 116 -8.7; 128 -9.0; 141 -9.1; 155 -9.2; 170 -9.2; 187 -9.2; 206 -9.1; 227 -8.9; 249 -8.9; 274 -8.9; 302 -8.8; 332 -8.6; 365 -8.0; 402 -7.6; 442 -6.4; 486 -4.8; 535 -3.9; 588 -3.5; 647 -3.5; 712 -3.9; 783 -4.4; 861 -5.1; 947 -6.0; 1042 -6.9; 1146 -7.6; 1261 -8.6; 1387 -9.7; 1526 -10.6; 1678 -10.4; 1846 -9.2; 2031 -7.7; 2234 -6.4; 2457 -4.7; 2703 -3.9; 2973 -4.3; 3270 -5.0; 3597 -4.9; 3957 -4.1; 4353 -3.2; 4788 -1.0; 5267 -0.5; 5793 -1.0; 6373 -2.6; 7010 -5.2; 7711 -6.7; 8482 -7.7; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Diskin Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Diskin Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 2.42 | -4.6 dB |
| Peaking | 238 Hz  | 0.42 | -3.1 dB |
| Peaking | 610 Hz  | 1.48 | 5.1 dB  |
| Peaking | 1538 Hz | 2.94 | -4.8 dB |
| Peaking | 5157 Hz | 2.09 | 6.3 dB  |
| Peaking | 51 Hz   | 3.59 | -0.4 dB |
| Peaking | 1867 Hz | 5.26 | -1.0 dB |
| Peaking | 2674 Hz | 4.39 | 2.6 dB  |
| Peaking | 6195 Hz | 6.62 | 1.6 dB  |
| Peaking | 8202 Hz | 2.68 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Diskin%20Wireless%20Bluetooth/Diskin%20Wireless%20Bluetooth.png)