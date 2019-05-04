# Mpow Bluetooth Over-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.0; 25 -8.2; 28 -8.5; 31 -8.7; 34 -8.7; 37 -8.7; 41 -8.7; 45 -8.7; 49 -8.9; 54 -9.1; 60 -9.5; 66 -9.8; 72 -10.1; 79 -10.4; 87 -10.9; 96 -11.4; 106 -11.9; 116 -12.4; 128 -12.8; 141 -13.0; 155 -13.2; 170 -13.3; 187 -13.1; 206 -12.9; 227 -12.6; 249 -12.1; 274 -11.5; 302 -10.9; 332 -10.4; 365 -8.6; 402 -6.6; 442 -5.0; 486 -4.4; 535 -3.7; 588 -2.7; 647 -1.5; 712 -0.5; 783 -0.8; 861 -2.1; 947 -3.3; 1042 -4.4; 1146 -4.8; 1261 -4.9; 1387 -4.9; 1526 -5.1; 1678 -5.4; 1846 -5.8; 2031 -6.2; 2234 -6.3; 2457 -6.8; 2703 -7.5; 2973 -8.1; 3270 -8.8; 3597 -8.3; 3957 -5.9; 4353 -3.9; 4788 -2.7; 5267 -3.9; 5793 -1.0; 6373 -0.8; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -7.3; 12418 -9.4; 13660 -8.5; 15026 -9.2; 16529 -7.1; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Bluetooth Over-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Bluetooth Over-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.19 | -1.6 dB |
| Peaking | 187 Hz   | 0.59 | -6.5 dB |
| Peaking | 670 Hz   | 1.3  | 7.0 dB  |
| Peaking | 6090 Hz  | 3.44 | 6.2 dB  |
| Peaking | 13832 Hz | 1.29 | -3.1 dB |
| Peaking | 338 Hz   | 2.67 | -2.0 dB |
| Peaking | 452 Hz   | 1.32 | 2.4 dB  |
| Peaking | 561 Hz   | 3.08 | -2.3 dB |
| Peaking | 3310 Hz  | 2.59 | -3.2 dB |
| Peaking | 4545 Hz  | 5.18 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20Bluetooth%20Over-Ear/Mpow%20Bluetooth%20Over-Ear.png)