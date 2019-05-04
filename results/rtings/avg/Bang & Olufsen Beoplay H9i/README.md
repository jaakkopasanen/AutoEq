# Bang & Olufsen Beoplay H9i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.8; 23 -14.8; 25 -13.8; 28 -12.4; 31 -11.2; 34 -10.2; 37 -9.2; 41 -8.1; 45 -7.1; 49 -6.3; 54 -5.5; 60 -4.8; 66 -4.2; 72 -3.8; 79 -3.4; 87 -3.2; 96 -3.0; 106 -2.7; 116 -2.6; 128 -2.4; 141 -2.2; 155 -2.0; 170 -1.7; 187 -1.4; 206 -1.1; 227 -0.9; 249 -0.7; 274 -0.7; 302 -0.8; 332 -1.0; 365 -1.3; 402 -1.8; 442 -2.4; 486 -3.0; 535 -3.3; 588 -3.5; 647 -3.6; 712 -3.6; 783 -3.9; 861 -4.1; 947 -4.5; 1042 -4.8; 1146 -5.3; 1261 -6.3; 1387 -7.5; 1526 -9.0; 1678 -10.5; 1846 -11.9; 2031 -11.5; 2234 -9.6; 2457 -8.2; 2703 -8.5; 2973 -10.6; 3270 -11.4; 3597 -7.6; 3957 -4.4; 4353 -3.6; 4788 -4.1; 5267 -2.2; 5793 -0.5; 6373 -1.0; 7010 -5.6; 7711 -12.0; 8482 -15.5; 9330 -15.0; 10263 -13.4; 11289 -9.9; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -10.6; 18182 -11.9; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H9i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H9i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 2.02 | -11.0 dB |
| Peaking | 1886 Hz  | 3.07 | -7.4 dB  |
| Peaking | 3127 Hz  | 6.17 | -6.3 dB  |
| Peaking | 9166 Hz  | 3.39 | -11.9 dB |
| Peaking | 17676 Hz | 2.26 | -8.6 dB  |
| Peaking | 35 Hz    | 2.45 | -2.4 dB  |
| Peaking | 231 Hz   | 0.53 | 4.3 dB   |
| Peaking | 6050 Hz  | 2.84 | 6.9 dB   |
| Peaking | 7855 Hz  | 5.04 | -5.4 dB  |
| Peaking | 18662 Hz | 3.66 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20H9i/Bang%20&%20Olufsen%20Beoplay%20H9i.png)