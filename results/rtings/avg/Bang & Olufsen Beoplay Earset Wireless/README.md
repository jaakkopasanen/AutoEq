# Bang & Olufsen Beoplay Earset Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.9; 34 -3.5; 37 -5.0; 41 -6.8; 45 -8.3; 49 -9.6; 54 -10.9; 60 -12.2; 66 -13.2; 72 -13.8; 79 -14.1; 87 -14.2; 96 -13.9; 106 -13.3; 116 -12.5; 128 -11.5; 141 -10.4; 155 -9.5; 170 -8.7; 187 -8.2; 206 -7.9; 227 -7.8; 249 -7.6; 274 -7.3; 302 -6.8; 332 -6.2; 365 -5.6; 402 -5.0; 442 -4.3; 486 -3.7; 535 -3.0; 588 -2.5; 647 -2.0; 712 -1.6; 783 -1.3; 861 -0.8; 947 -0.5; 1042 -0.5; 1146 -1.0; 1261 -1.6; 1387 -2.3; 1526 -3.0; 1678 -3.5; 1846 -3.8; 2031 -3.3; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -2.8; 3270 -6.7; 3597 -9.3; 3957 -10.7; 4353 -12.7; 4788 -14.6; 5267 -16.0; 5793 -13.9; 6373 -11.9; 7010 -10.1; 7711 -9.2; 8482 -10.5; 9330 -12.7; 10263 -13.0; 11289 -12.5; 12418 -12.4; 13660 -9.6; 15026 -7.0; 16529 -8.6; 18182 -8.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay Earset Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay Earset Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.76 | 8.9 dB   |
| Peaking | 74 Hz    | 0.63 | -9.7 dB  |
| Peaking | 2179 Hz  | 0.21 | 6.3 dB   |
| Peaking | 4968 Hz  | 1.55 | -13.8 dB |
| Peaking | 10889 Hz | 1.15 | -7.9 dB  |
| Peaking | 953 Hz   | 1.88 | 1.6 dB   |
| Peaking | 1887 Hz  | 1.52 | -4.4 dB  |
| Peaking | 2653 Hz  | 1.75 | 6.1 dB   |
| Peaking | 3434 Hz  | 3.43 | -4.2 dB  |
| Peaking | 17483 Hz | 3.85 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -8.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.0 dB |
| Peaking | 8000 Hz  | 1.41 | -6.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20Earset%20Wireless/Bang%20&%20Olufsen%20Beoplay%20Earset%20Wireless.png)