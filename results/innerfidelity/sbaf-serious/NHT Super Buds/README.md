# NHT Super Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.1; 23 -16.2; 25 -16.2; 28 -16.2; 31 -16.1; 34 -16.0; 37 -15.9; 41 -15.8; 45 -15.7; 49 -15.5; 54 -15.4; 60 -15.3; 66 -15.1; 72 -15.0; 79 -14.9; 87 -14.8; 96 -14.7; 106 -14.4; 116 -14.1; 128 -13.8; 141 -13.6; 155 -13.2; 170 -12.7; 187 -12.2; 206 -11.8; 227 -11.1; 249 -10.6; 274 -10.0; 302 -9.4; 332 -8.8; 365 -8.2; 402 -7.6; 442 -7.0; 486 -6.6; 535 -6.1; 588 -5.4; 647 -5.3; 712 -5.1; 783 -4.9; 861 -5.2; 947 -5.6; 1042 -6.1; 1146 -6.5; 1261 -7.2; 1387 -8.1; 1526 -9.1; 1678 -9.9; 1846 -10.2; 2031 -10.1; 2234 -9.6; 2457 -8.5; 2703 -7.4; 2973 -5.5; 3270 -3.2; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NHT Super Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NHT Super Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.1  | -9.4 dB |
| Peaking | 714 Hz  | 0.65 | 3.3 dB  |
| Peaking | 2005 Hz | 1.1  | -6.2 dB |
| Peaking | 4328 Hz | 1.18 | 8.1 dB  |
| Peaking | 3560 Hz | 7.03 | 1.8 dB  |
| Peaking | 4448 Hz | 3.79 | -1.0 dB |
| Peaking | 6348 Hz | 2.64 | 4.3 dB  |
| Peaking | 7133 Hz | 0.73 | -1.3 dB |
| Peaking | 7493 Hz | 2.97 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NHT%20Super%20Buds/NHT%20Super%20Buds.png)