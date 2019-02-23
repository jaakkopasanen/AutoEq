# Bowers & Wilkins P7 Wireless Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.7; 25 -4.2; 28 -4.7; 31 -5.2; 34 -5.6; 37 -5.9; 41 -6.2; 45 -6.4; 49 -6.6; 54 -6.8; 60 -7.0; 66 -7.2; 72 -7.4; 79 -7.6; 87 -7.8; 96 -8.2; 106 -8.3; 116 -8.3; 128 -8.4; 141 -8.5; 155 -8.7; 170 -8.7; 187 -8.4; 206 -8.5; 227 -8.3; 249 -8.0; 274 -7.5; 302 -6.5; 332 -5.9; 365 -5.5; 402 -5.3; 442 -5.3; 486 -5.4; 535 -5.4; 588 -5.1; 647 -5.2; 712 -5.4; 783 -5.4; 861 -5.8; 947 -6.0; 1042 -5.6; 1146 -5.7; 1261 -6.2; 1387 -6.9; 1526 -7.8; 1678 -8.4; 1846 -8.5; 2031 -7.9; 2234 -7.8; 2457 -8.0; 2703 -7.0; 2973 -3.5; 3270 -0.5; 3597 -2.8; 3957 -5.9; 4353 -6.4; 4788 -5.8; 5267 -4.3; 5793 -4.1; 6373 -3.1; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 2.16 | 2.9 dB  |
| Peaking | 134 Hz  | 0.86 | -3.0 dB |
| Peaking | 2126 Hz | 1.6  | -2.9 dB |
| Peaking | 3265 Hz | 5.53 | 6.8 dB  |
| Peaking | 6564 Hz | 5.21 | 3.8 dB  |
| Peaking | 240 Hz  | 1.96 | -2.0 dB |
| Peaking | 383 Hz  | 0.64 | 1.5 dB  |
| Peaking | 1187 Hz | 3.54 | 1.0 dB  |
| Peaking | 1724 Hz | 1.42 | -1.3 dB |
| Peaking | 2082 Hz | 5.39 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7%20Wireless%20Bluetooth/Bowers%20&%20Wilkins%20P7%20Wireless%20Bluetooth.png)