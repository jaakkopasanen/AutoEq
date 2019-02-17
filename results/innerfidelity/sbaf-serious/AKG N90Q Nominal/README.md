# AKG N90Q Nominal
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -3.8; 25 -3.7; 28 -3.5; 31 -3.3; 34 -3.1; 37 -2.9; 41 -2.6; 45 -2.4; 49 -2.2; 54 -2.0; 60 -1.9; 66 -2.0; 72 -2.3; 79 -2.7; 87 -3.1; 96 -3.4; 106 -3.7; 116 -3.7; 128 -4.1; 141 -4.3; 155 -4.3; 170 -4.3; 187 -4.4; 206 -4.3; 227 -4.2; 249 -4.3; 274 -4.2; 302 -4.2; 332 -4.1; 365 -4.1; 402 -4.3; 442 -4.3; 486 -4.6; 535 -4.7; 588 -4.2; 647 -3.6; 712 -4.5; 783 -4.4; 861 -4.2; 947 -3.8; 1042 -3.6; 1146 -3.4; 1261 -3.1; 1387 -3.5; 1526 -4.0; 1678 -3.9; 1846 -4.6; 2031 -4.7; 2234 -6.0; 2457 -7.1; 2703 -7.2; 2973 -7.3; 3270 -8.2; 3597 -8.3; 3957 -8.8; 4353 -8.7; 4788 -6.2; 5267 -3.3; 5793 -3.5; 6373 -0.5; 7010 -1.2; 7711 -3.4; 8482 -7.0; 9330 -9.3; 10263 -7.5; 11289 -4.1; 12418 -3.7; 13660 -4.6; 15026 -6.8; 16529 -4.5; 18182 -3.7; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N90Q Nominal GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N90Q Nominal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 58 Hz    | 2.13 | 2.0 dB  |
| Peaking | 3862 Hz  | 1.2  | -6.2 dB |
| Peaking | 6551 Hz  | 1.7  | 5.7 dB  |
| Peaking | 9232 Hz  | 3.23 | -7.1 dB |
| Peaking | 15138 Hz | 3.83 | -3.4 dB |
| Peaking | 171 Hz   | 1.76 | -0.7 dB |
| Peaking | 614 Hz   | 0.64 | -0.8 dB |
| Peaking | 1289 Hz  | 1.45 | 1.2 dB  |
| Peaking | 2468 Hz  | 6.69 | -1.3 dB |
| Peaking | 12017 Hz | 5.6  | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20N90Q%20Nominal/AKG%20N90Q%20Nominal.png)