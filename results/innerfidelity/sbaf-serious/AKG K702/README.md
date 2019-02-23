# AKG K702
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.2; 31 -2.7; 34 -3.2; 37 -3.5; 41 -3.9; 45 -4.3; 49 -4.6; 54 -4.9; 60 -5.2; 66 -5.5; 72 -5.8; 79 -5.5; 87 -5.8; 96 -6.2; 106 -6.1; 116 -6.5; 128 -7.2; 141 -7.7; 155 -7.8; 170 -7.5; 187 -7.7; 206 -7.7; 227 -7.6; 249 -7.6; 274 -7.4; 302 -7.1; 332 -6.8; 365 -6.5; 402 -6.1; 442 -5.5; 486 -5.2; 535 -3.6; 588 -2.6; 647 -2.3; 712 -1.8; 783 -1.7; 861 -2.2; 947 -2.6; 1042 -3.1; 1146 -3.6; 1261 -3.5; 1387 -4.1; 1526 -5.2; 1678 -6.4; 1846 -6.9; 2031 -8.2; 2234 -8.3; 2457 -7.5; 2703 -5.7; 2973 -4.1; 3270 -2.6; 3597 -2.8; 3957 -3.8; 4353 -6.1; 4788 -6.3; 5267 -5.4; 5793 -6.8; 6373 -8.9; 7010 -9.4; 7711 -9.5; 8482 -9.9; 9330 -7.1; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -6.1; 18182 -8.3; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.36 | 5.1 dB  |
| Peaking | 813 Hz   | 1.6  | 4.4 dB  |
| Peaking | 2191 Hz  | 3.17 | -3.6 dB |
| Peaking | 3388 Hz  | 3.06 | 4.0 dB  |
| Peaking | 7549 Hz  | 2.26 | -4.3 dB |
| Peaking | 212 Hz   | 0.86 | -2.2 dB |
| Peaking | 579 Hz   | 5.32 | 1.8 dB  |
| Peaking | 1294 Hz  | 5.77 | 1.3 dB  |
| Peaking | 10423 Hz | 4.77 | 1.1 dB  |
| Peaking | 18696 Hz | 1.74 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K702/AKG%20K702.png)