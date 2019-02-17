# HiFiMan Edition X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.3; 31 -1.8; 34 -2.2; 37 -2.5; 41 -2.9; 45 -3.2; 49 -3.4; 54 -3.7; 60 -3.9; 66 -4.2; 72 -4.4; 79 -4.5; 87 -4.7; 96 -5.0; 106 -5.3; 116 -5.5; 128 -5.9; 141 -6.1; 155 -6.4; 170 -6.6; 187 -6.8; 206 -6.8; 227 -6.2; 249 -6.4; 274 -6.5; 302 -6.2; 332 -6.0; 365 -5.4; 402 -6.1; 442 -6.8; 486 -7.0; 535 -7.0; 588 -7.2; 647 -7.6; 712 -5.7; 783 -3.9; 861 -5.5; 947 -5.9; 1042 -5.5; 1146 -1.8; 1261 -4.1; 1387 -4.0; 1526 -2.6; 1678 -4.5; 1846 -4.9; 2031 -6.0; 2234 -5.6; 2457 -6.2; 2703 -6.1; 2973 -7.2; 3270 -6.4; 3597 -6.1; 3957 -6.0; 4353 -6.4; 4788 -5.5; 5267 -3.4; 5793 -3.0; 6373 -6.4; 7010 -6.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.5; 18182 -13.0; 20000 -16.2
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

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.65 | 5.9 dB   |
| Peaking | 72 Hz    | 1.48 | 1.1 dB   |
| Peaking | 1138 Hz  | 7.72 | 4.0 dB   |
| Peaking | 1517 Hz  | 3.61 | 3.4 dB   |
| Peaking | 5532 Hz  | 6.3  | 4.3 dB   |
| Peaking | 186 Hz   | 4.64 | -0.7 dB  |
| Peaking | 365 Hz   | 6.57 | 1.2 dB   |
| Peaking | 698 Hz   | 2.6  | -2.8 dB  |
| Peaking | 756 Hz   | 5.91 | 5.1 dB   |
| Peaking | 19468 Hz | 1.22 | -10.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Edition%20X/HiFiMan%20Edition%20X.png)