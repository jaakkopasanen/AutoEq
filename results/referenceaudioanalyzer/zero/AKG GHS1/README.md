# AKG GHS1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -3.2; 25 -4.1; 28 -5.2; 31 -6.0; 34 -6.7; 37 -7.3; 41 -7.8; 45 -8.2; 49 -8.4; 54 -8.6; 60 -8.7; 66 -8.8; 72 -9.0; 79 -9.1; 87 -9.3; 96 -9.3; 106 -9.3; 116 -9.3; 128 -9.3; 141 -9.2; 155 -8.9; 170 -8.4; 187 -7.9; 206 -7.2; 227 -6.6; 249 -6.0; 274 -5.4; 302 -4.3; 332 -2.5; 365 -0.6; 402 -0.5; 442 -0.5; 486 -0.5; 535 -1.0; 588 -2.1; 647 -3.2; 712 -4.3; 783 -5.2; 861 -5.8; 947 -6.3; 1042 -6.5; 1146 -6.9; 1261 -7.2; 1387 -7.6; 1526 -7.7; 1678 -7.4; 1846 -6.4; 2031 -5.3; 2234 -4.5; 2457 -4.5; 2703 -5.5; 2973 -7.6; 3270 -9.7; 3597 -10.6; 3957 -10.2; 4353 -8.7; 4788 -8.1; 5267 -9.2; 5793 -9.9; 6373 -9.7; 7010 -9.4; 7711 -8.8; 8482 -8.3; 9330 -9.1; 10263 -10.6; 11289 -11.2; 12418 -10.7; 13660 -9.2; 15026 -6.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG GHS1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG GHS1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 4.04 | 4.5 dB  |
| Peaking | 456 Hz   | 1.89 | 7.0 dB  |
| Peaking | 5039 Hz  | 1.05 | -2.9 dB |
| Peaking | 11557 Hz | 1.79 | -4.6 dB |
| Peaking | 22050 Hz | 2.22 | -2.6 dB |
| Peaking | 64 Hz    | 1.15 | -1.9 dB |
| Peaking | 129 Hz   | 1.09 | -2.7 dB |
| Peaking | 351 Hz   | 5.49 | 2.3 dB  |
| Peaking | 2413 Hz  | 4.09 | 3.3 dB  |
| Peaking | 3500 Hz  | 5.37 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 7.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20GHS1/AKG%20GHS1.png)