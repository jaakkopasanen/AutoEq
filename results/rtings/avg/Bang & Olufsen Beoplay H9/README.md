# Bang & Olufsen Beoplay H9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.4; 23 -16.1; 25 -15.9; 28 -15.4; 31 -14.9; 34 -14.4; 37 -13.9; 41 -13.1; 45 -12.5; 49 -11.9; 54 -11.4; 60 -11.0; 66 -10.8; 72 -10.5; 79 -10.3; 87 -10.1; 96 -9.9; 106 -9.7; 116 -9.6; 128 -9.5; 141 -9.3; 155 -9.2; 170 -9.0; 187 -8.6; 206 -8.1; 227 -7.5; 249 -6.9; 274 -6.2; 302 -5.7; 332 -5.1; 365 -4.3; 402 -3.7; 442 -3.1; 486 -2.6; 535 -2.1; 588 -1.7; 647 -1.4; 712 -1.1; 783 -1.0; 861 -1.4; 947 -2.3; 1042 -3.1; 1146 -3.7; 1261 -4.4; 1387 -5.1; 1526 -5.8; 1678 -6.2; 1846 -6.6; 2031 -8.2; 2234 -9.8; 2457 -10.6; 2703 -9.0; 2973 -8.7; 3270 -11.3; 3597 -12.3; 3957 -9.7; 4353 -7.4; 4788 -7.1; 5267 -5.9; 5793 -0.6; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -9.8; 9330 -12.1; 10263 -14.3; 11289 -16.3; 12418 -14.7; 13660 -11.0; 15026 -7.9; 16529 -7.2; 18182 -7.9; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.45 | -10.2 dB |
| Peaking | 134 Hz   | 1.8  | -2.4 dB  |
| Peaking | 3435 Hz  | 2    | -5.9 dB  |
| Peaking | 6275 Hz  | 2.93 | 8.6 dB   |
| Peaking | 11242 Hz | 1.46 | -10.8 dB |
| Peaking | 208 Hz   | 1.87 | -1.5 dB  |
| Peaking | 694 Hz   | 0.88 | 5.2 dB   |
| Peaking | 2449 Hz  | 2.34 | -4.3 dB  |
| Peaking | 2871 Hz  | 5.11 | 3.9 dB   |
| Peaking | 18283 Hz | 3.64 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -5.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20H9/Bang%20&%20Olufsen%20Beoplay%20H9.png)