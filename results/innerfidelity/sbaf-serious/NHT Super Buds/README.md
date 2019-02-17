# NHT Super Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.7; 23 -16.8; 25 -16.9; 28 -16.8; 31 -16.7; 34 -16.6; 37 -16.6; 41 -16.4; 45 -16.3; 49 -16.1; 54 -16.0; 60 -15.9; 66 -15.8; 72 -15.7; 79 -15.5; 87 -15.5; 96 -15.4; 106 -15.1; 116 -14.7; 128 -14.5; 141 -14.2; 155 -13.8; 170 -13.3; 187 -12.9; 206 -12.4; 227 -11.8; 249 -11.2; 274 -10.6; 302 -10.0; 332 -9.4; 365 -8.8; 402 -8.3; 442 -7.6; 486 -7.2; 535 -6.7; 588 -6.0; 647 -6.0; 712 -5.8; 783 -5.6; 861 -5.8; 947 -6.2; 1042 -6.7; 1146 -7.2; 1261 -7.8; 1387 -8.7; 1526 -9.7; 1678 -10.5; 1846 -10.8; 2031 -10.7; 2234 -10.3; 2457 -9.2; 2703 -8.1; 2973 -6.1; 3270 -3.8; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NHT Super Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NHT Super Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.1  | -10.0 dB |
| Peaking | 719 Hz  | 0.66 | 3.0 dB   |
| Peaking | 2016 Hz | 1.04 | -6.7 dB  |
| Peaking | 4363 Hz | 1.2  | 8.4 dB   |
| Peaking | 3679 Hz | 6.14 | 2.1 dB   |
| Peaking | 4411 Hz | 1.96 | -1.5 dB  |
| Peaking | 6305 Hz | 2.58 | 4.1 dB   |
| Peaking | 7525 Hz | 3.27 | -2.3 dB  |
| Peaking | 8342 Hz | 1.02 | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB  |
| Peaking | 125 Hz   | 1.41 | -6.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NHT%20Super%20Buds/NHT%20Super%20Buds.png)