# Bang & Olufsen Beoplay H6 2nd Gen
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.2; 25 -10.4; 28 -10.5; 31 -10.6; 34 -10.7; 37 -10.6; 41 -10.5; 45 -10.2; 49 -9.9; 54 -9.5; 60 -9.2; 66 -9.2; 72 -9.2; 79 -9.3; 87 -9.5; 96 -9.6; 106 -9.5; 116 -9.4; 128 -9.1; 141 -8.5; 155 -7.6; 170 -6.3; 187 -4.8; 206 -3.4; 227 -2.4; 249 -2.0; 274 -2.5; 302 -3.6; 332 -4.7; 365 -5.8; 402 -6.5; 442 -6.9; 486 -7.3; 535 -7.5; 588 -7.6; 647 -7.8; 712 -7.9; 783 -7.9; 861 -7.9; 947 -7.9; 1042 -7.9; 1146 -7.8; 1261 -7.7; 1387 -7.8; 1526 -8.1; 1678 -8.6; 1846 -9.4; 2031 -9.9; 2234 -9.4; 2457 -8.0; 2703 -6.6; 2973 -5.0; 3270 -4.4; 3597 -4.3; 3957 -2.6; 4353 -2.5; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -3.3; 7010 -6.9; 7711 -10.4; 8482 -12.7; 9330 -11.3; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -9.3; 18182 -11.6; 20000 -8.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H6 2nd Gen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H6 2nd Gen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.07 | -3.1 dB |
| Peaking | 257 Hz   | 1.64 | 6.7 dB  |
| Peaking | 5327 Hz  | 2.03 | 7.4 dB  |
| Peaking | 8438 Hz  | 3.14 | -7.9 dB |
| Peaking | 18480 Hz | 1.38 | -5.5 dB |
| Peaking | 58 Hz    | 0    | -0.4 dB |
| Peaking | 207 Hz   | 2.73 | 2.0 dB  |
| Peaking | 2251 Hz  | 1.65 | -4.4 dB |
| Peaking | 2987 Hz  | 1.76 | 3.4 dB  |
| Peaking | 11902 Hz | 2.18 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen.png)