# Pioneer SE-M290
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.5; 28 -3.8; 31 -4.9; 34 -5.9; 37 -6.7; 41 -7.7; 45 -8.4; 49 -9.0; 54 -9.5; 60 -10.0; 66 -10.5; 72 -9.7; 79 -8.5; 87 -9.8; 96 -11.4; 106 -11.9; 116 -12.2; 128 -12.5; 141 -12.6; 155 -12.6; 170 -12.4; 187 -12.6; 206 -12.6; 227 -12.4; 249 -12.1; 274 -11.5; 302 -11.4; 332 -11.2; 365 -10.6; 402 -10.1; 442 -9.4; 486 -9.2; 535 -9.0; 588 -8.9; 647 -9.3; 712 -9.7; 783 -10.0; 861 -9.8; 947 -9.2; 1042 -8.6; 1146 -7.4; 1261 -5.6; 1387 -4.5; 1526 -3.6; 1678 -2.7; 1846 -2.3; 2031 -2.5; 2234 -2.5; 2457 -1.3; 2703 -0.6; 2973 -0.6; 3270 -0.6; 3597 -0.6; 3957 -0.6; 4353 -0.6; 4788 -0.6; 5267 -4.1; 5793 -2.9; 6373 -2.6; 7010 -4.1; 7711 -6.6; 8482 -6.9; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE-M290 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-M290 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.14 | 7.4 dB  |
| Peaking | 179 Hz   | 0.26 | -5.6 dB |
| Peaking | 1717 Hz  | 2.58 | 3.1 dB  |
| Peaking | 3482 Hz  | 0.98 | 6.7 dB  |
| Peaking | 22050 Hz | 2.19 | 2.0 dB  |
| Peaking | 13 Hz    | 1.7  | -0.7 dB |
| Peaking | 493 Hz   | 2.17 | 1.6 dB  |
| Peaking | 854 Hz   | 2.89 | -2.0 dB |
| Peaking | 6718 Hz  | 7.05 | 3.2 dB  |
| Peaking | 8041 Hz  | 2.63 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE-M290/Pioneer%20SE-M290.png)