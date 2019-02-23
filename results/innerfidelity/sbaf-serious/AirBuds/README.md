# AirBuds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.5; 25 -6.9; 28 -7.1; 31 -7.3; 34 -7.7; 37 -8.3; 41 -8.7; 45 -9.1; 49 -9.5; 54 -10.0; 60 -10.5; 66 -11.1; 72 -11.5; 79 -12.1; 87 -12.6; 96 -13.1; 106 -13.5; 116 -13.6; 128 -14.1; 141 -14.3; 155 -14.4; 170 -14.5; 187 -14.6; 206 -14.5; 227 -14.3; 249 -14.1; 274 -13.9; 302 -13.5; 332 -13.1; 365 -12.6; 402 -12.1; 442 -11.3; 486 -10.8; 535 -10.1; 588 -9.0; 647 -8.3; 712 -7.6; 783 -6.5; 861 -5.7; 947 -5.1; 1042 -4.5; 1146 -1.8; 1261 -1.3; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -1.6; 2031 -2.8; 2234 -1.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.8; 4788 -6.4; 5267 -9.2; 5793 -8.9; 6373 -5.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AirBuds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AirBuds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 93 Hz   | 0.71 | -3.1 dB |
| Peaking | 237 Hz  | 0.48 | -7.1 dB |
| Peaking | 1368 Hz | 1.36 | 5.8 dB  |
| Peaking | 3505 Hz | 0.98 | 6.4 dB  |
| Peaking | 5311 Hz | 4.09 | -7.2 dB |
| Peaking | 17 Hz   | 2.19 | 1.8 dB  |
| Peaking | 2050 Hz | 6.22 | -3.0 dB |
| Peaking | 2107 Hz | 2.74 | 1.7 dB  |
| Peaking | 6799 Hz | 8.43 | 3.6 dB  |
| Peaking | 7728 Hz | 1.21 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -6.7 dB |
| Peaking | 500 Hz   | 1.41 | -3.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AirBuds/AirBuds.png)