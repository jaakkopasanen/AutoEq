# Bang & Olufsen Beoplay Earset Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -2.1; 25 -3.5; 28 -5.5; 31 -7.4; 34 -9.0; 37 -10.5; 41 -12.2; 45 -13.8; 49 -15.0; 54 -16.4; 60 -17.7; 66 -18.7; 72 -19.3; 79 -19.6; 87 -19.7; 96 -19.3; 106 -18.8; 116 -18.0; 128 -17.0; 141 -15.9; 155 -14.9; 170 -14.2; 187 -13.7; 206 -13.4; 227 -13.3; 249 -13.1; 274 -12.7; 302 -12.3; 332 -11.7; 365 -11.0; 402 -10.5; 442 -9.8; 486 -9.2; 535 -8.5; 588 -7.9; 647 -7.4; 712 -7.0; 783 -6.7; 861 -6.3; 947 -6.0; 1042 -6.0; 1146 -6.4; 1261 -7.1; 1387 -7.8; 1526 -8.4; 1678 -9.0; 1846 -9.2; 2031 -8.8; 2234 -7.0; 2457 -5.2; 2703 -5.4; 2973 -8.3; 3270 -12.2; 3597 -14.8; 3957 -16.2; 4353 -18.2; 4788 -20.1; 5267 -21.4; 5793 -19.4; 6373 -17.3; 7010 -15.6; 7711 -14.7; 8482 -16.0; 9330 -18.2; 10263 -18.4; 11289 -18.0; 12418 -17.9; 13660 -15.1; 15026 -12.5; 16529 -14.1; 18182 -13.7; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay Earset Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay Earset Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 76 Hz    | 1.02 | -10.6 dB |
| Peaking | 171 Hz   | 0.47 | -6.4 dB  |
| Peaking | 4991 Hz  | 1.74 | -13.3 dB |
| Peaking | 11072 Hz | 0.91 | -11.4 dB |
| Peaking | 17718 Hz | 1.44 | -7.2 dB  |
| Peaking | 19 Hz    | 1.41 | 7.8 dB   |
| Peaking | 47 Hz    | 2.1  | -2.4 dB  |
| Peaking | 1933 Hz  | 1.92 | -7.3 dB  |
| Peaking | 2592 Hz  | 1.18 | 10.1 dB  |
| Peaking | 3418 Hz  | 1.92 | -7.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB   |
| Peaking | 62 Hz    | 1.41 | -13.3 dB |
| Peaking | 125 Hz   | 1.41 | -8.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | -9.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -12.2 dB |
| Peaking | 16000 Hz | 1.41 | -11.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20Earset%20Wireless/Bang%20&%20Olufsen%20Beoplay%20Earset%20Wireless.png)