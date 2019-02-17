# Status SM-CB1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.5; 28 -2.4; 31 -3.4; 34 -4.2; 37 -4.9; 41 -5.7; 45 -6.4; 49 -7.0; 54 -7.5; 60 -8.0; 66 -8.3; 72 -8.4; 79 -8.7; 87 -8.9; 96 -8.9; 106 -8.5; 116 -8.4; 128 -8.8; 141 -9.0; 155 -9.2; 170 -8.6; 187 -8.9; 206 -9.0; 227 -8.9; 249 -8.8; 274 -8.2; 302 -7.6; 332 -7.3; 365 -6.8; 402 -6.1; 442 -5.5; 486 -5.3; 535 -5.6; 588 -6.0; 647 -6.6; 712 -7.1; 783 -7.2; 861 -7.4; 947 -6.6; 1042 -7.1; 1146 -7.8; 1261 -7.9; 1387 -8.0; 1526 -8.2; 1678 -8.2; 1846 -8.1; 2031 -7.1; 2234 -6.1; 2457 -4.6; 2703 -3.5; 2973 -4.7; 3270 -5.8; 3597 -5.7; 3957 -5.1; 4353 -4.4; 4788 -3.1; 5267 -2.7; 5793 -4.7; 6373 -4.3; 7010 -3.9; 7711 -6.1; 8482 -9.4; 9330 -10.6; 10263 -6.5; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Status SM-CB1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Status SM-CB1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.12 | 6.3 dB  |
| Peaking | 109 Hz  | 0.47 | -2.9 dB |
| Peaking | 4996 Hz | 2.46 | 3.4 dB  |
| Peaking | 6763 Hz | 7.59 | 2.9 dB  |
| Peaking | 8962 Hz | 5.84 | -5.5 dB |
| Peaking | 237 Hz  | 3.18 | -0.9 dB |
| Peaking | 477 Hz  | 2.22 | 2.2 dB  |
| Peaking | 1279 Hz | 0.46 | -0.8 dB |
| Peaking | 1657 Hz | 1.99 | -1.5 dB |
| Peaking | 2645 Hz | 4.09 | 3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Status%20SM-CB1/Status%20SM-CB1.png)