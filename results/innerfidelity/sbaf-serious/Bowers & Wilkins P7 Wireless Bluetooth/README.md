# Bowers & Wilkins P7 Wireless Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.7; 25 -4.2; 28 -4.7; 31 -5.2; 34 -5.6; 37 -5.9; 41 -6.2; 45 -6.4; 49 -6.6; 54 -6.8; 60 -7.0; 66 -7.2; 72 -7.4; 79 -7.6; 87 -7.8; 96 -8.2; 106 -8.3; 116 -8.3; 128 -8.4; 141 -8.5; 155 -8.7; 170 -8.7; 187 -8.4; 206 -8.5; 227 -8.3; 249 -8.0; 274 -7.5; 302 -6.5; 332 -5.9; 365 -5.5; 402 -5.3; 442 -5.3; 486 -5.4; 535 -5.4; 588 -5.1; 647 -5.2; 712 -5.4; 783 -5.4; 861 -5.8; 947 -6.0; 1042 -5.6; 1146 -5.7; 1261 -6.2; 1387 -6.9; 1526 -7.8; 1678 -8.4; 1846 -8.5; 2031 -7.9; 2234 -7.8; 2457 -8.0; 2703 -7.0; 2973 -3.5; 3270 -0.5; 3597 -2.8; 3957 -5.9; 4353 -6.4; 4788 -5.8; 5267 -4.3; 5793 -4.1; 6373 -3.1; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.01 | 3.1 dB  |
| Peaking | 138 Hz  | 0.89 | -2.9 dB |
| Peaking | 2135 Hz | 1.64 | -2.8 dB |
| Peaking | 3279 Hz | 5.46 | 6.9 dB  |
| Peaking | 6535 Hz | 4.95 | 3.8 dB  |
| Peaking | 240 Hz  | 2.22 | -1.7 dB |
| Peaking | 422 Hz  | 0.7  | 1.4 dB  |
| Peaking | 1181 Hz | 3.34 | 1.1 dB  |
| Peaking | 1685 Hz | 1.46 | -1.4 dB |
| Peaking | 2111 Hz | 5.41 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7%20Wireless%20Bluetooth/Bowers%20&%20Wilkins%20P7%20Wireless%20Bluetooth.png)