# AKG K240 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.2; 34 -1.9; 37 -2.6; 41 -3.2; 45 -3.6; 49 -4.1; 54 -4.8; 60 -4.6; 66 -5.0; 72 -6.5; 79 -7.6; 87 -8.4; 96 -9.2; 106 -9.7; 116 -10.1; 128 -10.3; 141 -10.5; 155 -10.2; 170 -9.9; 187 -9.7; 206 -9.4; 227 -8.9; 249 -8.4; 274 -8.3; 302 -8.2; 332 -8.0; 365 -7.6; 402 -7.3; 442 -7.2; 486 -7.1; 535 -3.7; 588 -4.8; 647 -4.9; 712 -4.7; 783 -4.5; 861 -4.1; 947 -3.8; 1042 -3.6; 1146 -3.3; 1261 -3.3; 1387 -3.9; 1526 -4.7; 1678 -5.5; 1846 -6.6; 2031 -6.8; 2234 -7.7; 2457 -7.2; 2703 -5.3; 2973 -4.4; 3270 -2.5; 3597 -1.8; 3957 -3.3; 4353 -4.3; 4788 -4.6; 5267 -2.2; 5793 -2.1; 6373 -4.1; 7010 -6.2; 7711 -9.0; 8482 -12.6; 9330 -13.3; 10263 -9.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.23 | 6.7 dB  |
| Peaking | 131 Hz  | 0.54 | -6.2 dB |
| Peaking | 1855 Hz | 0.12 | 2.0 dB  |
| Peaking | 5670 Hz | 3.29 | 3.7 dB  |
| Peaking | 8898 Hz | 2.9  | -9.3 dB |
| Peaking | 482 Hz  | 2.83 | -2.3 dB |
| Peaking | 544 Hz  | 6.21 | 3.4 dB  |
| Peaking | 1239 Hz | 1.2  | 2.4 dB  |
| Peaking | 2147 Hz | 1.41 | -3.9 dB |
| Peaking | 3418 Hz | 3.86 | 3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K240%20MKII/AKG%20K240%20MKII.png)