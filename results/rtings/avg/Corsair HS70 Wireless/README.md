# Corsair HS70 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.6; 25 -3.1; 28 -3.7; 31 -4.1; 34 -4.5; 37 -4.7; 41 -5.0; 45 -5.2; 49 -5.3; 54 -5.5; 60 -5.9; 66 -6.3; 72 -6.8; 79 -7.3; 87 -7.7; 96 -8.0; 106 -8.0; 116 -7.9; 128 -7.6; 141 -7.2; 155 -6.6; 170 -6.0; 187 -5.3; 206 -4.6; 227 -4.0; 249 -3.5; 274 -3.6; 302 -3.7; 332 -3.7; 365 -3.7; 402 -3.8; 442 -3.8; 486 -3.9; 535 -3.7; 588 -3.5; 647 -3.1; 712 -2.1; 783 -1.5; 861 -2.8; 947 -1.6; 1042 -1.0; 1146 -0.8; 1261 -0.5; 1387 -0.7; 1526 -1.2; 1678 -2.2; 1846 -3.1; 2031 -3.6; 2234 -3.3; 2457 -3.2; 2703 -3.6; 2973 -4.1; 3270 -3.9; 3597 -3.6; 3957 -3.2; 4353 -3.2; 4788 -5.3; 5267 -4.0; 5793 -2.1; 6373 -1.1; 7010 -1.4; 7711 -5.3; 8482 -11.0; 9330 -11.1; 10263 -8.8; 11289 -10.3; 12418 -12.7; 13660 -9.8; 15026 -4.3; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair HS70 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair HS70 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 102 Hz   | 1.13 | -4.4 dB |
| Peaking | 1176 Hz  | 1.31 | 3.4 dB  |
| Peaking | 6815 Hz  | 3.45 | 5.9 dB  |
| Peaking | 8801 Hz  | 2.82 | -8.1 dB |
| Peaking | 12464 Hz | 2.76 | -8.7 dB |
| Peaking | 21 Hz    | 2.62 | 2.1 dB  |
| Peaking | 256 Hz   | 3.84 | 1.1 dB  |
| Peaking | 1508 Hz  | 5.01 | 0.6 dB  |
| Peaking | 1952 Hz  | 3.89 | -0.8 dB |
| Peaking | 15498 Hz | 4.79 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20HS70%20Wireless/Corsair%20HS70%20Wireless.png)