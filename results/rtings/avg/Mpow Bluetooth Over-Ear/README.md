# Mpow Bluetooth Over-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.3; 25 -8.5; 28 -8.8; 31 -9.0; 34 -9.1; 37 -9.0; 41 -9.0; 45 -9.0; 49 -9.1; 54 -9.4; 60 -9.7; 66 -10.1; 72 -10.4; 79 -10.8; 87 -11.2; 96 -11.8; 106 -12.3; 116 -12.8; 128 -13.1; 141 -13.3; 155 -13.5; 170 -13.6; 187 -13.4; 206 -13.2; 227 -12.8; 249 -12.3; 274 -11.6; 302 -11.1; 332 -10.5; 365 -8.8; 402 -6.8; 442 -5.1; 486 -4.5; 535 -3.7; 588 -2.7; 647 -1.5; 712 -0.5; 783 -0.7; 861 -2.2; 947 -3.3; 1042 -4.3; 1146 -4.8; 1261 -4.9; 1387 -4.8; 1526 -4.9; 1678 -5.2; 1846 -5.6; 2031 -5.9; 2234 -5.5; 2457 -6.0; 2703 -6.9; 2973 -8.1; 3270 -9.2; 3597 -8.7; 3957 -6.4; 4353 -4.5; 4788 -2.3; 5267 -3.8; 5793 -1.3; 6373 -0.9; 7010 -3.8; 7711 -6.1; 8482 -6.3; 9330 -6.3; 10263 -6.4; 11289 -6.7; 12418 -9.4; 13660 -9.4; 15026 -9.8; 16529 -7.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Bluetooth Over-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Bluetooth Over-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.15 | -1.7 dB |
| Peaking | 187 Hz   | 0.57 | -6.6 dB |
| Peaking | 671 Hz   | 1.22 | 7.2 dB  |
| Peaking | 6072 Hz  | 3.33 | 6.1 dB  |
| Peaking | 14165 Hz | 1.53 | -3.7 dB |
| Peaking | 336 Hz   | 3.05 | -1.8 dB |
| Peaking | 458 Hz   | 1.39 | 2.2 dB  |
| Peaking | 560 Hz   | 3.09 | -2.2 dB |
| Peaking | 3343 Hz  | 4.07 | -3.7 dB |
| Peaking | 4665 Hz  | 7.39 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20Bluetooth%20Over-Ear/Mpow%20Bluetooth%20Over-Ear.png)