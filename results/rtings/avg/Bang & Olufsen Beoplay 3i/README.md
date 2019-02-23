# Bang & Olufsen Beoplay Earset 3i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.2; 66 -2.4; 72 -3.4; 79 -4.4; 87 -5.3; 96 -6.1; 106 -6.8; 116 -7.3; 128 -7.7; 141 -7.9; 155 -8.0; 170 -8.0; 187 -8.1; 206 -8.2; 227 -8.2; 249 -8.3; 274 -8.4; 302 -8.6; 332 -8.6; 365 -8.7; 402 -7.1; 442 -7.4; 486 -7.4; 535 -7.5; 588 -7.2; 647 -7.0; 712 -7.3; 783 -7.4; 861 -7.3; 947 -7.3; 1042 -7.3; 1146 -7.3; 1261 -7.5; 1387 -7.6; 1526 -7.7; 1678 -7.7; 1846 -7.4; 2031 -6.3; 2234 -4.3; 2457 -2.2; 2703 -1.2; 2973 -1.5; 3270 -2.7; 3597 -4.2; 3957 -5.5; 4353 -6.9; 4788 -7.8; 5267 -9.0; 5793 -8.9; 6373 -7.0; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay Earset 3i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay Earset 3i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 46 Hz   |  0.42 | 9.6 dB  |
| Peaking | 113 Hz  |  0.42 | -6.0 dB |
| Peaking | 1876 Hz |  1.2  | -3.3 dB |
| Peaking | 2699 Hz |  1.78 | 7.5 dB  |
| Peaking | 5298 Hz |  3.8  | -3.5 dB |
| Peaking | 58 Hz   |  2.42 | 2.1 dB  |
| Peaking | 58 Hz   |  1.01 | -1.4 dB |
| Peaking | 265 Hz  |  0.75 | 0.8 dB  |
| Peaking | 319 Hz  |  3.12 | -1.2 dB |
| Peaking | 6999 Hz | 10.05 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%203i/Bang%20&%20Olufsen%20Beoplay%20Earset%203i.png)