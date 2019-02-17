# Rock Jaw Alpha Genus Silver Filters
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.4; 23 -14.5; 25 -14.6; 28 -14.7; 31 -14.6; 34 -14.6; 37 -14.5; 41 -14.5; 45 -14.3; 49 -14.3; 54 -14.1; 60 -14.0; 66 -13.9; 72 -13.8; 79 -13.7; 87 -13.7; 96 -13.5; 106 -13.3; 116 -12.9; 128 -12.7; 141 -12.3; 155 -11.9; 170 -11.5; 187 -11.0; 206 -10.4; 227 -9.8; 249 -9.2; 274 -8.6; 302 -7.9; 332 -7.3; 365 -6.7; 402 -6.0; 442 -5.3; 486 -4.8; 535 -4.2; 588 -3.4; 647 -2.9; 712 -2.6; 783 -2.2; 861 -2.3; 947 -2.5; 1042 -2.8; 1146 -3.2; 1261 -3.7; 1387 -4.5; 1526 -5.4; 1678 -6.6; 1846 -7.5; 2031 -8.0; 2234 -8.6; 2457 -8.6; 2703 -8.3; 2973 -6.3; 3270 -4.0; 3597 -3.2; 3957 -4.3; 4353 -8.3; 4788 -12.5; 5267 -11.4; 5793 -6.5; 6373 -1.8; 7010 -0.5; 7711 -2.4; 8482 -2.7; 9330 -3.3; 10263 -6.0; 11289 -5.2; 12418 -3.8; 13660 -4.1; 15026 -2.7; 16529 -2.7; 18182 -2.7; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Jaw Alpha Genus Silver Filters GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Jaw Alpha Genus Silver Filters ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.1  | -11.8 dB |
| Peaking | 704 Hz   | 0.88 | 2.7 dB   |
| Peaking | 2183 Hz  | 1.72 | -6.3 dB  |
| Peaking | 4928 Hz  | 5.63 | -11.0 dB |
| Peaking | 10852 Hz | 4.92 | -3.5 dB  |
| Peaking | 2773 Hz  | 7.75 | -1.7 dB  |
| Peaking | 3552 Hz  | 5.14 | 2.5 dB   |
| Peaking | 5698 Hz  | 4.84 | -2.9 dB  |
| Peaking | 6741 Hz  | 3.35 | 4.4 dB   |
| Peaking | 8086 Hz  | 0.44 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.4 dB |
| Peaking | 62 Hz    | 1.41 | -8.0 dB  |
| Peaking | 125 Hz   | 1.41 | -8.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 16000 Hz | 1.41 | -0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Rock%20Jaw%20Alpha%20Genus%20Silver%20Filters/Rock%20Jaw%20Alpha%20Genus%20Silver%20Filters.png)