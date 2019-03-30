# AKG K77 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.4; 66 -2.1; 72 -2.5; 79 -3.0; 87 -3.7; 96 -4.4; 106 -4.9; 116 -5.3; 128 -5.7; 141 -6.2; 155 -6.6; 170 -6.9; 187 -7.2; 206 -7.5; 227 -7.6; 249 -7.8; 274 -7.8; 302 -7.8; 332 -7.8; 365 -7.9; 402 -8.1; 442 -8.1; 486 -7.7; 535 -8.4; 588 -10.4; 647 -11.5; 712 -11.0; 783 -10.2; 861 -11.0; 947 -12.2; 1042 -12.4; 1146 -11.8; 1261 -10.8; 1387 -9.2; 1526 -7.4; 1678 -5.5; 1846 -4.5; 2031 -4.0; 2234 -2.9; 2457 -1.8; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -3.0; 5267 -1.5; 5793 -0.5; 6373 -2.1; 7010 -5.7; 7711 -8.6; 8482 -10.5; 9330 -11.3; 10263 -10.6; 11289 -9.5; 12418 -9.1; 13660 -8.7; 15026 -7.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K77 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K77 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.58 | 6.7 dB  |
| Peaking | 1062 Hz  | 2.24 | -3.7 dB |
| Peaking | 2991 Hz  | 0.68 | 14.8 dB |
| Peaking | 3134 Hz  | 0.18 | -8.4 dB |
| Peaking | 5832 Hz  | 3.31 | 7.3 dB  |
| Peaking | 501 Hz   | 4.16 | 1.8 dB  |
| Peaking | 639 Hz   | 6.21 | -2.1 dB |
| Peaking | 6822 Hz  | 4.47 | 1.1 dB  |
| Peaking | 9020 Hz  | 2.72 | -2.5 dB |
| Peaking | 16137 Hz | 1.12 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -7.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K77%20PRO/AKG%20K77%20PRO.png)