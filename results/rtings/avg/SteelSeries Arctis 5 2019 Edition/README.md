# SteelSeries Arctis 5 2019 Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.4; 25 -4.2; 28 -3.9; 31 -3.7; 34 -3.5; 37 -3.4; 41 -3.5; 45 -3.7; 49 -4.1; 54 -4.8; 60 -5.6; 66 -6.3; 72 -6.9; 79 -7.4; 87 -7.9; 96 -8.3; 106 -8.7; 116 -8.9; 128 -9.1; 141 -9.3; 155 -9.3; 170 -9.2; 187 -8.9; 206 -8.4; 227 -8.1; 249 -8.4; 274 -8.4; 302 -8.0; 332 -7.3; 365 -6.6; 402 -5.9; 442 -5.5; 486 -5.3; 535 -5.1; 588 -4.8; 647 -4.6; 712 -4.3; 783 -3.8; 861 -3.7; 947 -3.4; 1042 -2.9; 1146 -2.3; 1261 -1.4; 1387 -0.5; 1526 -0.8; 1678 -3.5; 1846 -4.6; 2031 -3.9; 2234 -3.0; 2457 -2.9; 2703 -2.8; 2973 -3.5; 3270 -5.1; 3597 -5.9; 3957 -5.0; 4353 -3.6; 4788 -2.1; 5267 -2.3; 5793 -2.9; 6373 -0.6; 7010 -2.6; 7711 -5.3; 8482 -6.6; 9330 -6.0; 10263 -5.8; 11289 -5.2; 12418 -5.1; 13660 -5.1; 15026 -7.2; 16529 -8.4; 18182 -7.3; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis 5 2019 Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis 5 2019 Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 135 Hz   | 1.09 | -4.3 dB |
| Peaking | 275 Hz   | 2.01 | -2.3 dB |
| Peaking | 1334 Hz  | 1.46 | 4.0 dB  |
| Peaking | 6047 Hz  | 2.75 | 3.8 dB  |
| Peaking | 16808 Hz | 1.36 | -3.5 dB |
| Peaking | 37 Hz    | 1.93 | 2.3 dB  |
| Peaking | 1829 Hz  | 5.5  | -2.7 dB |
| Peaking | 3269 Hz  | 1.1  | 3.0 dB  |
| Peaking | 3541 Hz  | 3.26 | -4.5 dB |
| Peaking | 8478 Hz  | 4.01 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%205%202019%20Edition/SteelSeries%20Arctis%205%202019%20Edition.png)