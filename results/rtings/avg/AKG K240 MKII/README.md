# AKG K240 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.0; 60 -2.0; 66 -3.0; 72 -3.8; 79 -4.7; 87 -5.6; 96 -6.4; 106 -7.3; 116 -8.0; 128 -8.5; 141 -9.0; 155 -9.3; 170 -9.3; 187 -9.1; 206 -8.7; 227 -8.5; 249 -8.5; 274 -8.7; 302 -8.7; 332 -8.7; 365 -8.6; 402 -8.6; 442 -8.4; 486 -7.4; 535 -6.6; 588 -6.9; 647 -6.8; 712 -6.4; 783 -6.0; 861 -5.6; 947 -5.3; 1042 -4.9; 1146 -4.4; 1261 -4.2; 1387 -3.6; 1526 -3.0; 1678 -3.3; 1846 -4.2; 2031 -5.4; 2234 -6.2; 2457 -6.6; 2703 -6.9; 2973 -6.1; 3270 -4.4; 3597 -1.4; 3957 -4.9; 4353 -4.5; 4788 -3.8; 5267 -1.8; 5793 -1.9; 6373 -4.2; 7010 -5.9; 7711 -8.0; 8482 -10.5; 9330 -11.6; 10263 -9.5; 11289 -6.6; 12418 -6.5; 13660 -6.7; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 1.11 | 7.3 dB  |
| Peaking | 1486 Hz | 2.45 | 3.7 dB  |
| Peaking | 3574 Hz | 8.35 | 4.6 dB  |
| Peaking | 5568 Hz | 3.1  | 5.4 dB  |
| Peaking | 9076 Hz | 3.16 | -5.9 dB |
| Peaking | 59 Hz   | 2.12 | 2.6 dB  |
| Peaking | 153 Hz  | 1.18 | -3.0 dB |
| Peaking | 355 Hz  | 1.55 | -2.0 dB |
| Peaking | 971 Hz  | 2.29 | 0.9 dB  |
| Peaking | 2580 Hz | 5.9  | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K240%20MKII/AKG%20K240%20MKII.png)