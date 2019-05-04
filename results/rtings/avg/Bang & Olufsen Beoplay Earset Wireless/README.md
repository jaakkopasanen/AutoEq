# Bang & Olufsen Beoplay Earset Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.3; 34 -2.7; 37 -4.3; 41 -6.2; 45 -7.8; 49 -9.3; 54 -10.7; 60 -12.0; 66 -13.0; 72 -13.7; 79 -14.2; 87 -14.4; 96 -14.1; 106 -13.5; 116 -12.7; 128 -11.6; 141 -10.4; 155 -9.3; 170 -8.5; 187 -7.9; 206 -7.6; 227 -7.4; 249 -7.2; 274 -7.0; 302 -6.6; 332 -6.1; 365 -5.5; 402 -4.9; 442 -4.3; 486 -3.7; 535 -3.0; 588 -2.5; 647 -2.0; 712 -1.7; 783 -1.3; 861 -1.0; 947 -0.6; 1042 -0.6; 1146 -1.2; 1261 -1.8; 1387 -2.5; 1526 -3.2; 1678 -3.8; 1846 -4.1; 2031 -3.7; 2234 -2.3; 2457 -0.6; 2703 -0.6; 2973 -3.1; 3270 -6.7; 3597 -9.0; 3957 -10.4; 4353 -12.4; 4788 -15.2; 5267 -16.3; 5793 -13.8; 6373 -10.9; 7010 -10.2; 7711 -9.9; 8482 -10.2; 9330 -11.1; 10263 -12.4; 11289 -13.4; 12418 -12.5; 13660 -8.8; 15026 -6.6; 16529 -8.5; 18182 -7.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay Earset Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay Earset Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.91 | 8.5 dB   |
| Peaking | 79 Hz    | 0.73 | -9.4 dB  |
| Peaking | 1664 Hz  | 0.25 | 5.6 dB   |
| Peaking | 4997 Hz  | 1.72 | -13.1 dB |
| Peaking | 11250 Hz | 1.59 | -7.2 dB  |
| Peaking | 962 Hz   | 1.98 | 1.7 dB   |
| Peaking | 1913 Hz  | 1.49 | -4.0 dB  |
| Peaking | 2633 Hz  | 2.23 | 5.6 dB   |
| Peaking | 3472 Hz  | 4.22 | -3.0 dB  |
| Peaking | 17477 Hz | 4.2  | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -8.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20Earset%20Wireless/Bang%20&%20Olufsen%20Beoplay%20Earset%20Wireless.png)