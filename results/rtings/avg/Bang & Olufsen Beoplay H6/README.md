# Bang & Olufsen Beoplay H6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.0; 25 -10.1; 28 -10.3; 31 -10.5; 34 -10.5; 37 -10.5; 41 -10.3; 45 -10.1; 49 -9.8; 54 -9.4; 60 -9.1; 66 -9.0; 72 -9.0; 79 -9.1; 87 -9.2; 96 -9.3; 106 -9.3; 116 -9.2; 128 -8.9; 141 -8.3; 155 -7.4; 170 -6.2; 187 -4.6; 206 -3.2; 227 -2.3; 249 -1.9; 274 -2.4; 302 -3.6; 332 -4.7; 365 -5.7; 402 -6.5; 442 -6.9; 486 -7.4; 535 -7.6; 588 -7.8; 647 -7.9; 712 -8.0; 783 -8.1; 861 -8.1; 947 -8.1; 1042 -8.1; 1146 -7.9; 1261 -7.9; 1387 -8.0; 1526 -8.3; 1678 -8.8; 1846 -9.7; 2031 -10.4; 2234 -10.2; 2457 -8.9; 2703 -7.2; 2973 -5.1; 3270 -4.1; 3597 -4.1; 3957 -2.2; 4353 -2.1; 4788 -2.3; 5267 -0.5; 5793 -0.5; 6373 -2.4; 7010 -7.0; 7711 -11.2; 8482 -12.2; 9330 -9.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.1; 18182 -11.3; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 120 Hz   | 0.02 | -3.3 dB  |
| Peaking | 256 Hz   | 1.26 | 7.9 dB   |
| Peaking | 5660 Hz  | 0.98 | 9.8 dB   |
| Peaking | 8022 Hz  | 2.57 | -10.9 dB |
| Peaking | 18414 Hz | 1.33 | -5.3 dB  |
| Peaking | 34 Hz    | 2.62 | -0.8 dB  |
| Peaking | 126 Hz   | 3.37 | -1.0 dB  |
| Peaking | 1315 Hz  | 0.87 | 1.7 dB   |
| Peaking | 2162 Hz  | 1.91 | -3.8 dB  |
| Peaking | 3087 Hz  | 3.24 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 5.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20H6/Bang%20&%20Olufsen%20Beoplay%20H6.png)