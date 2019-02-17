# Bang & Olufsen Beoplay Earset 3i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -1.6; 72 -2.6; 79 -3.6; 87 -4.5; 96 -5.4; 106 -6.0; 116 -6.5; 128 -6.9; 141 -7.1; 155 -7.2; 170 -7.3; 187 -7.3; 206 -7.4; 227 -7.5; 249 -7.5; 274 -7.7; 302 -7.8; 332 -7.8; 365 -7.9; 402 -6.3; 442 -6.6; 486 -6.6; 535 -6.7; 588 -6.4; 647 -6.2; 712 -6.5; 783 -6.6; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.7; 1387 -6.8; 1526 -6.9; 1678 -6.9; 1846 -6.6; 2031 -5.5; 2234 -3.5; 2457 -1.4; 2703 -0.5; 2973 -0.8; 3270 -2.0; 3597 -3.4; 3957 -4.7; 4353 -6.1; 4788 -7.0; 5267 -8.2; 5793 -8.1; 6373 -6.2; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay Earset 3i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay Earset 3i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 51 Hz   |  0.37 | 9.1 dB  |
| Peaking | 117 Hz  |  0.51 | -6.0 dB |
| Peaking | 2846 Hz |  2.5  | 6.6 dB  |
| Peaking | 5378 Hz |  5.76 | -2.7 dB |
| Peaking | 18 Hz   |  2.4  | 1.3 dB  |
| Peaking | 591 Hz  |  2.3  | 0.5 dB  |
| Peaking | 1748 Hz |  2.07 | -1.3 dB |
| Peaking | 2375 Hz |  6.87 | 1.6 dB  |
| Peaking | 6960 Hz | 10.05 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%203i/Bang%20&%20Olufsen%20Beoplay%20Earset%203i.png)