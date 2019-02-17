# AKG K 550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.8; 25 -5.1; 28 -5.5; 31 -5.8; 34 -6.0; 37 -6.2; 41 -6.4; 45 -6.5; 49 -6.5; 54 -6.5; 60 -6.5; 66 -6.7; 72 -6.5; 79 -5.9; 87 -4.7; 96 -4.4; 106 -5.8; 116 -7.0; 128 -7.9; 141 -8.1; 155 -7.8; 170 -6.3; 187 -8.0; 206 -8.2; 227 -8.2; 249 -8.3; 274 -8.0; 302 -7.9; 332 -7.7; 365 -7.3; 402 -7.0; 442 -6.8; 486 -6.5; 535 -6.2; 588 -5.7; 647 -5.2; 712 -5.0; 783 -4.9; 861 -5.9; 947 -6.1; 1042 -6.5; 1146 -6.9; 1261 -7.2; 1387 -7.6; 1526 -8.3; 1678 -8.0; 1846 -7.1; 2031 -6.4; 2234 -5.8; 2457 -5.4; 2703 -5.1; 2973 -4.0; 3270 -2.5; 3597 -0.9; 3957 -0.5; 4353 -2.1; 4788 -3.1; 5267 -6.5; 5793 -7.0; 6373 -2.7; 7010 -3.9; 7711 -6.2; 8482 -11.5; 9330 -13.0; 10263 -7.6; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K 550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 1.29 | 3.5 dB  |
| Peaking | 236 Hz   | 1.55 | -2.1 dB |
| Peaking | 3809 Hz  | 2.88 | 6.4 dB  |
| Peaking | 6695 Hz  | 8.09 | 4.8 dB  |
| Peaking | 9040 Hz  | 5.04 | -8.0 dB |
| Peaking | 94 Hz    | 5.17 | 2.5 dB  |
| Peaking | 132 Hz   | 4.79 | -1.6 dB |
| Peaking | 717 Hz   | 3.01 | 1.7 dB  |
| Peaking | 1540 Hz  | 3.25 | -2.2 dB |
| Peaking | 10970 Hz | 4.48 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K550/AKG%20K%20550.png)