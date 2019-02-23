# Advanced Alpha Shallow Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.0; 25 -3.0; 28 -3.0; 31 -3.0; 34 -2.9; 37 -2.9; 41 -2.9; 45 -2.9; 49 -3.0; 54 -3.0; 60 -3.1; 66 -3.2; 72 -3.3; 79 -3.4; 87 -3.8; 96 -4.4; 106 -4.7; 116 -5.0; 128 -5.5; 141 -5.8; 155 -6.2; 170 -6.3; 187 -6.6; 206 -6.7; 227 -6.7; 249 -6.8; 274 -6.9; 302 -6.7; 332 -6.7; 365 -6.4; 402 -6.0; 442 -5.6; 486 -5.4; 535 -5.3; 588 -4.5; 647 -4.2; 712 -4.1; 783 -4.0; 861 -4.2; 947 -4.4; 1042 -4.2; 1146 -4.4; 1261 -4.7; 1387 -3.8; 1526 -3.9; 1678 -4.1; 1846 -3.0; 2031 -5.1; 2234 -7.2; 2457 -9.0; 2703 -10.5; 2973 -11.2; 3270 -9.8; 3597 -8.4; 3957 -5.3; 4353 -0.5; 4788 -6.1; 5267 -6.6; 5793 -4.2; 6373 -4.4; 7010 -4.0; 7711 -5.4; 8482 -6.7; 9330 -7.1; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -6.9; 15026 -7.9; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced Alpha Shallow Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced Alpha Shallow Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.74 | 3.3 dB   |
| Peaking | 2054 Hz  | 0.75 | 13.8 dB  |
| Peaking | 2630 Hz  | 0.77 | -16.5 dB |
| Peaking | 4327 Hz  | 5.98 | 8.8 dB   |
| Peaking | 6558 Hz  | 3.06 | 3.9 dB   |
| Peaking | 83 Hz    | 2.18 | 1.1 dB   |
| Peaking | 249 Hz   | 0.82 | -1.5 dB  |
| Peaking | 673 Hz   | 2.26 | 1.4 dB   |
| Peaking | 12661 Hz | 2.41 | 0.9 dB   |
| Peaking | 14490 Hz | 4.77 | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Advanced%20Alpha%20Shallow%20Pads/Advanced%20Alpha%20Shallow%20Pads.png)