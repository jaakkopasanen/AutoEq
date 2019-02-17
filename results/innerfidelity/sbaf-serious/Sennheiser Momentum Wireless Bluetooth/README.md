# Sennheiser Momentum Wireless Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.9; 25 -3.6; 28 -4.1; 31 -4.0; 34 -3.7; 37 -3.3; 41 -3.0; 45 -2.7; 49 -2.4; 54 -2.2; 60 -2.0; 66 -1.9; 72 -1.8; 79 -1.7; 87 -1.7; 96 -1.7; 106 -1.6; 116 -1.4; 128 -1.5; 141 -1.2; 155 -1.2; 170 -0.9; 187 -0.6; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.6; 535 -1.4; 588 -2.1; 647 -3.0; 712 -4.0; 783 -4.6; 861 -5.4; 947 -6.0; 1042 -6.7; 1146 -7.3; 1261 -8.2; 1387 -9.4; 1526 -10.8; 1678 -11.9; 1846 -12.3; 2031 -11.9; 2234 -10.4; 2457 -7.7; 2703 -5.5; 2973 -2.8; 3270 -0.8; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -4.9; 5267 -3.9; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 97 Hz   |  0.22 | 4.5 dB  |
| Peaking | 415 Hz  |  0.71 | 3.8 dB  |
| Peaking | 1890 Hz |  1.28 | -8.0 dB |
| Peaking | 3483 Hz |  1.65 | 8.4 dB  |
| Peaking | 6127 Hz |  5.2  | 5.3 dB  |
| Peaking | 32 Hz   |  2.81 | -0.6 dB |
| Peaking | 864 Hz  |  4.73 | -0.4 dB |
| Peaking | 4619 Hz |  6.04 | 3.3 dB  |
| Peaking | 4910 Hz | 12.43 | -6.2 dB |
| Peaking | 8330 Hz |  4.34 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 3.7 dB  |
| Peaking | 250 Hz   | 1.41 | 4.9 dB  |
| Peaking | 500 Hz   | 1.41 | 5.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20Wireless%20Bluetooth/Sennheiser%20Momentum%20Wireless%20Bluetooth.png)