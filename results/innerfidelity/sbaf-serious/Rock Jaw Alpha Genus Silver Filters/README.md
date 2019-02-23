# Rock Jaw Alpha Genus Silver Filters
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -13.1; 25 -13.2; 28 -13.3; 31 -13.3; 34 -13.2; 37 -13.2; 41 -13.1; 45 -13.0; 49 -12.9; 54 -12.8; 60 -12.6; 66 -12.5; 72 -12.4; 79 -12.4; 87 -12.3; 96 -12.2; 106 -11.9; 116 -11.5; 128 -11.3; 141 -11.0; 155 -10.6; 170 -10.1; 187 -9.6; 206 -9.1; 227 -8.5; 249 -7.8; 274 -7.2; 302 -6.6; 332 -5.9; 365 -5.3; 402 -4.7; 442 -3.9; 486 -3.4; 535 -2.8; 588 -2.0; 647 -1.5; 712 -1.2; 783 -0.8; 861 -0.9; 947 -1.2; 1042 -1.4; 1146 -1.8; 1261 -2.3; 1387 -3.1; 1526 -4.1; 1678 -5.2; 1846 -6.1; 2031 -6.7; 2234 -7.2; 2457 -7.3; 2703 -6.9; 2973 -5.0; 3270 -2.6; 3597 -1.8; 3957 -2.9; 4353 -6.9; 4788 -11.2; 5267 -10.0; 5793 -5.1; 6373 -0.5; 7010 -2.6; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Jaw Alpha Genus Silver Filters GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Jaw Alpha Genus Silver Filters ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 34 Hz   | 0.15 | -8.1 dB  |
| Peaking | 819 Hz  | 0.73 | 6.0 dB   |
| Peaking | 3726 Hz | 2.61 | 10.4 dB  |
| Peaking | 5102 Hz | 0.98 | -24.2 dB |
| Peaking | 6119 Hz | 1.17 | 20.4 dB  |
| Peaking | 1359 Hz | 2.56 | 1.2 dB   |
| Peaking | 2468 Hz | 0.8  | -1.4 dB  |
| Peaking | 3170 Hz | 6.47 | 1.8 dB   |
| Peaking | 7893 Hz | 3.95 | -1.9 dB  |
| Peaking | 8795 Hz | 0.28 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Rock%20Jaw%20Alpha%20Genus%20Silver%20Filters/Rock%20Jaw%20Alpha%20Genus%20Silver%20Filters.png)