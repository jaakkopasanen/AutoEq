# AKG K240 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.5; 54 -2.3; 60 -3.4; 66 -4.3; 72 -5.2; 79 -6.0; 87 -7.0; 96 -7.8; 106 -8.7; 116 -9.3; 128 -9.9; 141 -10.4; 155 -10.6; 170 -10.6; 187 -10.5; 206 -10.0; 227 -9.9; 249 -9.8; 274 -10.0; 302 -10.1; 332 -10.1; 365 -10.0; 402 -9.9; 442 -9.8; 486 -8.8; 535 -8.0; 588 -8.3; 647 -8.1; 712 -7.7; 783 -7.4; 861 -7.0; 947 -6.7; 1042 -6.3; 1146 -5.8; 1261 -5.5; 1387 -5.0; 1526 -4.3; 1678 -4.7; 1846 -5.6; 2031 -6.8; 2234 -7.6; 2457 -7.9; 2703 -8.2; 2973 -7.5; 3270 -5.8; 3597 -2.8; 3957 -6.3; 4353 -5.9; 4788 -5.2; 5267 -3.2; 5793 -3.2; 6373 -5.6; 7010 -7.3; 7711 -9.4; 8482 -11.9; 9330 -13.0; 10263 -10.8; 11289 -7.3; 12418 -6.5; 13660 -8.0; 15026 -7.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.46 | 7.0 dB  |
| Peaking | 137 Hz  | 0.69 | -5.4 dB |
| Peaking | 381 Hz  | 1.54 | -2.5 dB |
| Peaking | 5563 Hz | 2.87 | 4.2 dB  |
| Peaking | 9057 Hz | 2.55 | -7.1 dB |
| Peaking | 1591 Hz | 1.8  | 4.1 dB  |
| Peaking | 2437 Hz | 0.83 | -2.9 dB |
| Peaking | 3595 Hz | 5.83 | 5.6 dB  |
| Peaking | 3933 Hz | 6.77 | -1.3 dB |
| Peaking | 5506 Hz | 2.73 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K240%20MKII/AKG%20K240%20MKII.png)