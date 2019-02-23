# Bang & Olufsen Beoplay H9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.6; 23 -16.4; 25 -16.1; 28 -15.7; 31 -15.2; 34 -14.6; 37 -14.0; 41 -13.2; 45 -12.5; 49 -12.0; 54 -11.5; 60 -11.2; 66 -10.9; 72 -10.7; 79 -10.5; 87 -10.4; 96 -10.1; 106 -10.0; 116 -9.8; 128 -9.7; 141 -9.5; 155 -9.4; 170 -9.2; 187 -8.8; 206 -8.3; 227 -7.6; 249 -6.9; 274 -6.3; 302 -5.8; 332 -5.1; 365 -4.4; 402 -3.8; 442 -3.1; 486 -2.5; 535 -2.0; 588 -1.7; 647 -1.3; 712 -1.0; 783 -0.9; 861 -1.2; 947 -2.2; 1042 -3.0; 1146 -3.6; 1261 -4.2; 1387 -4.9; 1526 -5.5; 1678 -6.0; 1846 -6.3; 2031 -7.7; 2234 -9.0; 2457 -9.8; 2703 -8.4; 2973 -8.6; 3270 -11.5; 3597 -12.5; 3957 -10.1; 4353 -7.8; 4788 -6.7; 5267 -5.6; 5793 -0.7; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -10.0; 9330 -13.6; 10263 -14.7; 11289 -15.3; 12418 -14.6; 13660 -11.9; 15026 -8.4; 16529 -7.4; 18182 -8.1; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.38 | -10.8 dB |
| Peaking | 147 Hz   | 0.92 | -2.7 dB  |
| Peaking | 669 Hz   | 1.05 | 5.5 dB   |
| Peaking | 3399 Hz  | 3.28 | -6.7 dB  |
| Peaking | 11547 Hz | 1.95 | -10.7 dB |
| Peaking | 902 Hz   | 4.13 | 0.7 dB   |
| Peaking | 2290 Hz  | 4.23 | -3.3 dB  |
| Peaking | 5151 Hz  | 2.16 | -3.4 dB  |
| Peaking | 6111 Hz  | 2.48 | 9.4 dB   |
| Peaking | 9266 Hz  | 4.36 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -5.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20H9/Bang%20&%20Olufsen%20Beoplay%20H9.png)