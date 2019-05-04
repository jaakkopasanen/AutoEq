# Panasonic RP-HJE120
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.1; 25 -8.4; 28 -8.8; 31 -9.1; 34 -9.3; 37 -9.5; 41 -9.8; 45 -10.0; 49 -10.1; 54 -10.3; 60 -10.5; 66 -10.8; 72 -11.0; 79 -11.2; 87 -11.4; 96 -11.6; 106 -11.7; 116 -11.8; 128 -11.8; 141 -11.7; 155 -11.5; 170 -11.3; 187 -10.9; 206 -10.5; 227 -10.0; 249 -9.4; 274 -8.8; 302 -8.4; 332 -8.0; 365 -7.4; 402 -6.7; 442 -5.9; 486 -5.1; 535 -4.1; 588 -3.2; 647 -1.9; 712 -0.9; 783 -0.5; 861 -0.7; 947 -1.1; 1042 -1.4; 1146 -1.7; 1261 -1.9; 1387 -2.0; 1526 -2.1; 1678 -2.5; 1846 -3.0; 2031 -3.5; 2234 -3.7; 2457 -3.5; 2703 -3.2; 2973 -2.8; 3270 -2.6; 3597 -2.7; 3957 -3.1; 4353 -4.2; 4788 -6.2; 5267 -7.8; 5793 -5.7; 6373 -1.7; 7010 -2.4; 7711 -4.6; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HJE120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HJE120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 47 Hz   |  0.29 | -3.2 dB |
| Peaking | 276 Hz  |  0.25 | -6.3 dB |
| Peaking | 781 Hz  |  0.57 | 8.4 dB  |
| Peaking | 6628 Hz | 10.15 | 4.3 dB  |
| Peaking | 748 Hz  |  4.54 | 1.1 dB  |
| Peaking | 2256 Hz |  0.28 | -0.5 dB |
| Peaking | 3613 Hz |  1.82 | 2.5 dB  |
| Peaking | 5344 Hz |  3.51 | -4.7 dB |
| Peaking | 6151 Hz |  3.73 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HJE120/Panasonic%20RP-HJE120.png)