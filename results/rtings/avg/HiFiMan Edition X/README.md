# HiFiMan Edition X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.5; 31 -3.0; 34 -3.4; 37 -3.7; 41 -4.1; 45 -4.4; 49 -4.6; 54 -4.8; 60 -5.1; 66 -5.4; 72 -5.6; 79 -5.7; 87 -5.9; 96 -6.2; 106 -6.5; 116 -6.7; 128 -7.1; 141 -7.3; 155 -7.6; 170 -7.8; 187 -8.0; 206 -8.0; 227 -7.4; 249 -7.5; 274 -7.7; 302 -7.4; 332 -7.2; 365 -6.6; 402 -7.3; 442 -8.0; 486 -8.2; 535 -8.2; 588 -8.4; 647 -8.8; 712 -6.9; 783 -5.1; 861 -6.7; 947 -7.1; 1042 -6.7; 1146 -3.0; 1261 -5.3; 1387 -5.2; 1526 -3.8; 1678 -5.7; 1846 -6.1; 2031 -7.2; 2234 -6.8; 2457 -7.4; 2703 -7.3; 2973 -8.4; 3270 -7.6; 3597 -7.3; 3957 -7.2; 4353 -7.6; 4788 -6.7; 5267 -4.6; 5793 -4.1; 6373 -7.6; 7010 -8.0; 7711 -6.9; 8482 -6.7; 9330 -6.8; 10263 -6.8; 11289 -6.8; 12418 -6.8; 13660 -6.8; 15026 -6.8; 16529 -8.5; 18182 -14.2; 20000 -17.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Edition X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.2  | 6.1 dB   |
| Peaking | 48 Hz    | 1.7  | 1.4 dB   |
| Peaking | 1356 Hz  | 2.82 | 2.4 dB   |
| Peaking | 5553 Hz  | 9.28 | 3.5 dB   |
| Peaking | 19519 Hz | 1.15 | -11.2 dB |
| Peaking | 192 Hz   | 1.83 | -1.3 dB  |
| Peaking | 556 Hz   | 2.97 | -1.9 dB  |
| Peaking | 3010 Hz  | 3.02 | -1.4 dB  |
| Peaking | 6740 Hz  | 9.61 | -1.9 dB  |
| Peaking | 14887 Hz | 2.31 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Edition%20X/HiFiMan%20Edition%20X.png)