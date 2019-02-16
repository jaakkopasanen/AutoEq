# SteelSeries Arctis Pro Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.5; 28 -5.7; 31 -5.5; 34 -5.0; 37 -4.4; 41 -3.7; 45 -3.6; 49 -3.9; 54 -4.3; 60 -4.8; 66 -5.1; 72 -5.3; 79 -5.4; 87 -5.6; 96 -5.8; 106 -5.9; 116 -5.9; 128 -6.0; 141 -5.9; 155 -5.9; 170 -5.7; 187 -5.4; 206 -5.2; 227 -4.9; 249 -4.7; 274 -4.6; 302 -4.5; 332 -4.3; 365 -3.9; 402 -4.0; 442 -4.6; 486 -4.8; 535 -4.9; 588 -5.0; 647 -5.0; 712 -5.1; 783 -5.1; 861 -4.9; 947 -4.4; 1042 -3.7; 1146 -3.4; 1261 -3.7; 1387 -3.9; 1526 -3.8; 1678 -5.9; 1846 -7.7; 2031 -7.9; 2234 -7.8; 2457 -7.4; 2703 -7.3; 2973 -7.2; 3270 -5.1; 3597 -0.5; 3957 -1.2; 4353 -4.3; 4788 -4.5; 5267 -5.6; 5793 -8.1; 6373 -8.7; 7010 -8.3; 7711 -6.2; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.3; 12418 -9.5; 13660 -11.6; 15026 -10.8; 16529 -8.0; 18182 -4.2; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis Pro Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis Pro Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 123 Hz   | 0.76 | -2.0 dB |
| Peaking | 2400 Hz  | 1.66 | -4.3 dB |
| Peaking | 3727 Hz  | 6.62 | 6.4 dB  |
| Peaking | 6366 Hz  | 3.72 | -5.0 dB |
| Peaking | 14368 Hz | 1.89 | -8.4 dB |
| Peaking | 26 Hz    | 2.61 | -1.7 dB |
| Peaking | 734 Hz   | 1.93 | -1.3 dB |
| Peaking | 1371 Hz  | 1.52 | 1.7 dB  |
| Peaking | 1839 Hz  | 5.43 | -2.3 dB |
| Peaking | 10209 Hz | 3.74 | 2.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%20Pro%20Wireless/SteelSeries%20Arctis%20Pro%20Wireless.png)