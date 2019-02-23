# V-Moda Crossfade Wireless Bluetooth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.7; 25 -6.7; 28 -7.9; 31 -8.9; 34 -9.6; 37 -10.2; 41 -10.7; 45 -11.1; 49 -11.3; 54 -11.6; 60 -11.6; 66 -11.2; 72 -11.2; 79 -12.2; 87 -13.0; 96 -13.1; 106 -12.5; 116 -13.0; 128 -13.4; 141 -13.4; 155 -13.3; 170 -12.5; 187 -12.3; 206 -11.6; 227 -10.4; 249 -9.1; 274 -7.3; 302 -5.3; 332 -3.7; 365 -2.3; 402 -1.7; 442 -1.8; 486 -1.7; 535 -1.9; 588 -2.2; 647 -2.7; 712 -3.6; 783 -4.5; 861 -5.7; 947 -6.7; 1042 -7.3; 1146 -8.0; 1261 -8.2; 1387 -8.5; 1526 -8.8; 1678 -8.7; 1846 -8.2; 2031 -7.6; 2234 -7.8; 2457 -8.1; 2703 -7.2; 2973 -7.7; 3270 -9.0; 3597 -11.1; 3957 -8.8; 4353 -6.4; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.8; 9330 -11.3; 10263 -11.5; 11289 -7.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade Wireless Bluetooth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 1.38 | 4.9 dB   |
| Peaking | 331 Hz  | 0.17 | -14.4 dB |
| Peaking | 475 Hz  | 0.54 | 19.8 dB  |
| Peaking | 5699 Hz | 2.61 | 8.4 dB   |
| Peaking | 9774 Hz | 3.76 | -6.3 dB  |
| Peaking | 71 Hz   | 3.96 | 1.7 dB   |
| Peaking | 272 Hz  | 0.87 | -2.0 dB  |
| Peaking | 320 Hz  | 2.31 | 3.4 dB   |
| Peaking | 3617 Hz | 1.29 | 2.9 dB   |
| Peaking | 3661 Hz | 3.72 | -6.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 7.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20Wireless%20Bluetooth/V-Moda%20Crossfade%20Wireless%20Bluetooth.png)