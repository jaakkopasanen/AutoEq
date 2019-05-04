# HiFiMan Edition X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -1.9; 31 -2.5; 34 -2.9; 37 -3.2; 41 -3.6; 45 -3.9; 49 -4.1; 54 -4.4; 60 -4.6; 66 -4.8; 72 -4.9; 79 -5.1; 87 -5.3; 96 -5.6; 106 -5.9; 116 -6.2; 128 -6.5; 141 -6.7; 155 -7.0; 170 -7.3; 187 -7.5; 206 -7.4; 227 -7.0; 249 -7.1; 274 -7.3; 302 -7.0; 332 -6.7; 365 -6.2; 402 -6.9; 442 -7.6; 486 -7.9; 535 -7.9; 588 -8.1; 647 -8.6; 712 -6.5; 783 -4.9; 861 -6.4; 947 -7.1; 1042 -6.1; 1146 -3.1; 1261 -5.2; 1387 -4.9; 1526 -3.9; 1678 -5.6; 1846 -5.9; 2031 -7.2; 2234 -7.4; 2457 -7.8; 2703 -7.7; 2973 -7.9; 3270 -7.0; 3597 -6.7; 3957 -6.5; 4353 -6.8; 4788 -6.6; 5267 -4.5; 5793 -3.5; 6373 -6.0; 7010 -7.7; 7711 -7.4; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -8.0; 18182 -13.7; 20000 -16.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Edition X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.73 | 6.0 dB  |
| Peaking | 101 Hz   | 0.89 | 1.1 dB  |
| Peaking | 1307 Hz  | 1.68 | 3.5 dB  |
| Peaking | 3196 Hz  | 0.04 | -1.3 dB |
| Peaking | 5649 Hz  | 3.24 | 3.3 dB  |
| Peaking | 149 Hz   | 1.15 | -0.9 dB |
| Peaking | 360 Hz   | 4.39 | 1.4 dB  |
| Peaking | 704 Hz   | 2.29 | -2.5 dB |
| Peaking | 760 Hz   | 6.26 | 4.6 dB  |
| Peaking | 11472 Hz | 1.71 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Edition%20X/HiFiMan%20Edition%20X.png)