# AKG K240 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -1.8; 66 -2.7; 72 -3.5; 79 -4.4; 87 -5.3; 96 -6.2; 106 -7.0; 116 -7.7; 128 -8.3; 141 -8.8; 155 -9.0; 170 -9.1; 187 -8.9; 206 -8.5; 227 -8.4; 249 -8.5; 274 -8.6; 302 -8.7; 332 -8.7; 365 -8.6; 402 -8.5; 442 -8.4; 486 -7.5; 535 -6.7; 588 -7.0; 647 -6.9; 712 -6.5; 783 -6.2; 861 -5.7; 947 -5.4; 1042 -5.1; 1146 -4.6; 1261 -4.3; 1387 -3.7; 1526 -3.2; 1678 -3.5; 1846 -4.6; 2031 -6.0; 2234 -7.1; 2457 -7.6; 2703 -7.4; 2973 -6.2; 3270 -4.0; 3597 -1.6; 3957 -4.4; 4353 -4.3; 4788 -4.0; 5267 -2.3; 5793 -1.8; 6373 -3.2; 7010 -6.0; 7711 -8.9; 8482 -10.2; 9330 -9.9; 10263 -8.9; 11289 -6.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 1.06 | 7.3 dB  |
| Peaking | 1469 Hz | 2.88 | 3.5 dB  |
| Peaking | 3568 Hz | 7.77 | 4.7 dB  |
| Peaking | 5777 Hz | 2.58 | 5.8 dB  |
| Peaking | 8588 Hz | 2.2  | -4.8 dB |
| Peaking | 61 Hz   | 2.21 | 2.4 dB  |
| Peaking | 151 Hz  | 1.25 | -2.9 dB |
| Peaking | 360 Hz  | 1.18 | -2.4 dB |
| Peaking | 981 Hz  | 0.28 | 0.7 dB  |
| Peaking | 2498 Hz | 3.32 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K240%20MKII/AKG%20K240%20MKII.png)