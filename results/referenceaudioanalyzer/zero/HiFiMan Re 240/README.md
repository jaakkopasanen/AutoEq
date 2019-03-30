# HiFiMan Re 240
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.6; 25 -4.6; 28 -4.7; 31 -4.8; 34 -4.9; 37 -5.0; 41 -5.0; 45 -5.0; 49 -5.0; 54 -5.0; 60 -5.1; 66 -5.2; 72 -5.3; 79 -5.3; 87 -5.3; 96 -5.3; 106 -5.3; 116 -5.3; 128 -5.3; 141 -5.3; 155 -5.3; 170 -5.3; 187 -5.3; 206 -5.6; 227 -5.7; 249 -5.6; 274 -5.6; 302 -5.6; 332 -5.6; 365 -5.6; 402 -5.9; 442 -6.0; 486 -6.2; 535 -6.5; 588 -6.6; 647 -6.9; 712 -7.1; 783 -7.5; 861 -8.1; 947 -8.7; 1042 -9.6; 1146 -10.8; 1261 -12.4; 1387 -14.3; 1526 -16.1; 1678 -16.5; 1846 -14.8; 2031 -11.1; 2234 -6.5; 2457 -2.4; 2703 -0.5; 2973 -1.8; 3270 -4.6; 3597 -5.1; 3957 -4.0; 4353 -3.1; 4788 -2.3; 5267 -1.8; 5793 -4.4; 6373 -9.0; 7010 -10.4; 7711 -7.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Re 240 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Re 240 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 30 Hz   |  0.05 | 1.3 dB   |
| Peaking | 1662 Hz |  1.56 | -12.0 dB |
| Peaking | 2610 Hz |  2.74 | 9.8 dB   |
| Peaking | 5187 Hz |  2.2  | 5.9 dB   |
| Peaking | 6707 Hz |  3.81 | -6.3 dB  |
| Peaking | 23 Hz   |  1.3  | 0.6 dB   |
| Peaking | 1325 Hz |  6.95 | -0.2 dB  |
| Peaking | 8247 Hz | 10.72 | 0.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20Re%20240/HiFiMan%20Re%20240.png)