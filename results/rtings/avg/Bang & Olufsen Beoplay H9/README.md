# Bang & Olufsen Beoplay H9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.8; 23 -18.5; 25 -18.3; 28 -17.9; 31 -17.3; 34 -16.8; 37 -16.2; 41 -15.4; 45 -14.7; 49 -14.2; 54 -13.7; 60 -13.3; 66 -13.1; 72 -12.9; 79 -12.7; 87 -12.6; 96 -12.3; 106 -12.2; 116 -12.0; 128 -11.9; 141 -11.7; 155 -11.6; 170 -11.4; 187 -11.0; 206 -10.4; 227 -9.8; 249 -9.1; 274 -8.5; 302 -8.0; 332 -7.3; 365 -6.6; 402 -5.9; 442 -5.3; 486 -4.7; 535 -4.2; 588 -3.8; 647 -3.5; 712 -3.2; 783 -3.0; 861 -3.4; 947 -4.3; 1042 -5.2; 1146 -5.8; 1261 -6.4; 1387 -7.1; 1526 -7.7; 1678 -8.1; 1846 -8.5; 2031 -9.9; 2234 -11.1; 2457 -12.0; 2703 -10.6; 2973 -10.8; 3270 -13.7; 3597 -14.7; 3957 -12.3; 4353 -10.0; 4788 -8.9; 5267 -7.8; 5793 -2.3; 6373 -0.5; 7010 -2.4; 7711 -5.6; 8482 -12.2; 9330 -15.8; 10263 -16.8; 11289 -17.5; 12418 -16.8; 13660 -14.1; 15026 -10.6; 16529 -9.6; 18182 -10.3; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.21 | -14.3 dB |
| Peaking | 163 Hz   | 1.05 | -4.3 dB  |
| Peaking | 2290 Hz  | 2.21 | -5.9 dB  |
| Peaking | 3556 Hz  | 3.84 | -8.9 dB  |
| Peaking | 11842 Hz | 1.42 | -13.9 dB |
| Peaking | 705 Hz   | 2.33 | 2.6 dB   |
| Peaking | 5152 Hz  | 1.95 | -6.4 dB  |
| Peaking | 6309 Hz  | 1.99 | 11.7 dB  |
| Peaking | 9089 Hz  | 3.62 | -6.6 dB  |
| Peaking | 18467 Hz | 1.24 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 16000 Hz | 1.41 | -11.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20H9/Bang%20&%20Olufsen%20Beoplay%20H9.png)