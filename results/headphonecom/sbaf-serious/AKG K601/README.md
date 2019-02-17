# AKG K601
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.9; 31 -2.3; 34 -2.6; 37 -2.9; 41 -3.3; 45 -3.6; 49 -3.8; 54 -4.2; 60 -4.5; 66 -4.8; 72 -3.7; 79 -4.1; 87 -5.3; 96 -5.1; 106 -5.8; 116 -6.2; 128 -6.7; 141 -7.0; 155 -7.2; 170 -7.2; 187 -7.5; 206 -7.5; 227 -7.5; 249 -7.5; 274 -7.4; 302 -7.3; 332 -7.0; 365 -6.9; 402 -6.8; 442 -6.7; 486 -6.7; 535 -6.7; 588 -6.4; 647 -6.0; 712 -6.0; 783 -5.9; 861 -6.0; 947 -6.5; 1042 -6.9; 1146 -7.3; 1261 -7.8; 1387 -8.5; 1526 -9.0; 1678 -8.8; 1846 -9.0; 2031 -8.4; 2234 -8.1; 2457 -8.2; 2703 -8.2; 2973 -7.8; 3270 -7.2; 3597 -7.5; 3957 -8.3; 4353 -8.7; 4788 -8.1; 5267 -6.4; 5793 -8.7; 6373 -9.1; 7010 -6.6; 7711 -6.8; 8482 -6.8; 9330 -7.3; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.69 | 5.9 dB  |
| Peaking | 75 Hz    | 4.32 | 2.0 dB  |
| Peaking | 1716 Hz  | 2.14 | -2.3 dB |
| Peaking | 4806 Hz  | 0.94 | -1.3 dB |
| Peaking | 10604 Hz | 1.83 | 0.2 dB  |
| Peaking | 211 Hz   | 1.46 | -1.0 dB |
| Peaking | 764 Hz   | 1.94 | 1.3 dB  |
| Peaking | 2434 Hz  | 0.25 | -0.3 dB |
| Peaking | 3393 Hz  | 9.67 | 1.3 dB  |
| Peaking | 7375 Hz  | 7.35 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K601/AKG%20K601.png)