# Mpow Bluetooth Over-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.3; 25 -10.5; 28 -10.8; 31 -11.0; 34 -11.1; 37 -11.0; 41 -11.0; 45 -11.0; 49 -11.2; 54 -11.4; 60 -11.8; 66 -12.1; 72 -12.4; 79 -12.8; 87 -13.3; 96 -13.8; 106 -14.3; 116 -14.8; 128 -15.1; 141 -15.3; 155 -15.5; 170 -15.6; 187 -15.5; 206 -15.2; 227 -14.8; 249 -14.3; 274 -13.6; 302 -13.1; 332 -12.5; 365 -10.8; 402 -8.8; 442 -7.2; 486 -6.5; 535 -5.7; 588 -4.7; 647 -3.5; 712 -2.5; 783 -2.8; 861 -4.2; 947 -5.3; 1042 -6.4; 1146 -6.9; 1261 -6.9; 1387 -6.9; 1526 -6.9; 1678 -7.2; 1846 -7.7; 2031 -7.9; 2234 -7.5; 2457 -8.0; 2703 -8.9; 2973 -10.1; 3270 -11.2; 3597 -10.8; 3957 -8.4; 4353 -6.5; 4788 -4.3; 5267 -5.8; 5793 -3.1; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -8.2; 12418 -11.4; 13660 -11.5; 15026 -11.8; 16529 -9.3; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Bluetooth Over-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Bluetooth Over-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.36 | -5.6 dB |
| Peaking | 192 Hz   | 1.02 | -7.6 dB |
| Peaking | 3241 Hz  | 2.44 | -5.5 dB |
| Peaking | 6292 Hz  | 3.62 | 6.2 dB  |
| Peaking | 14253 Hz | 1.45 | -6.6 dB |
| Peaking | 21 Hz    | 2.26 | -0.8 dB |
| Peaking | 321 Hz   | 4.24 | -2.6 dB |
| Peaking | 697 Hz   | 2.55 | 4.7 dB  |
| Peaking | 17984 Hz | 3.59 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -8.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -6.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20Bluetooth%20Over-Ear/Mpow%20Bluetooth%20Over-Ear.png)