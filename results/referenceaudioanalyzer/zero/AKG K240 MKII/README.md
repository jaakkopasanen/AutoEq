# AKG K240 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.2; 41 -2.1; 45 -2.8; 49 -3.4; 54 -3.9; 60 -4.5; 66 -5.0; 72 -5.5; 79 -6.2; 87 -6.8; 96 -7.3; 106 -7.8; 116 -8.2; 128 -8.5; 141 -8.8; 155 -8.8; 170 -8.3; 187 -7.8; 206 -7.8; 227 -8.0; 249 -8.2; 274 -8.1; 302 -8.1; 332 -8.1; 365 -8.1; 402 -8.2; 442 -8.1; 486 -7.1; 535 -6.2; 588 -6.4; 647 -6.9; 712 -6.8; 783 -6.5; 861 -6.2; 947 -5.8; 1042 -5.3; 1146 -4.7; 1261 -3.9; 1387 -3.0; 1526 -2.1; 1678 -2.0; 1846 -3.1; 2031 -4.9; 2234 -6.8; 2457 -8.2; 2703 -8.4; 2973 -6.9; 3270 -4.5; 3597 -5.7; 3957 -7.5; 4353 -6.4; 4788 -4.8; 5267 -6.0; 5793 -7.6; 6373 -8.7; 7010 -8.8; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -9.2; 12418 -10.1; 13660 -6.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.49 | 7.2 dB  |
| Peaking | 116 Hz   | 0.36 | -3.1 dB |
| Peaking | 1599 Hz  | 1.73 | 4.8 dB  |
| Peaking | 2496 Hz  | 4.27 | -3.5 dB |
| Peaking | 12235 Hz | 4.24 | -4.2 dB |
| Peaking | 407 Hz   | 6.11 | -0.7 dB |
| Peaking | 3388 Hz  | 5.95 | 3.8 dB  |
| Peaking | 3813 Hz  | 2.16 | -2.2 dB |
| Peaking | 4772 Hz  | 5.3  | 2.9 dB  |
| Peaking | 6606 Hz  | 4.87 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K240%20MKII/AKG%20K240%20MKII.png)