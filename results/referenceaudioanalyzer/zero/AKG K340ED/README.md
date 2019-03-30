# AKG K340ED
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.8; 37 -2.5; 41 -3.2; 45 -4.0; 49 -4.6; 54 -5.2; 60 -5.8; 66 -6.3; 72 -6.8; 79 -7.3; 87 -7.7; 96 -8.2; 106 -8.9; 116 -9.5; 128 -9.9; 141 -10.3; 155 -10.4; 170 -10.4; 187 -10.4; 206 -10.4; 227 -10.4; 249 -10.1; 274 -10.1; 302 -9.9; 332 -9.6; 365 -9.1; 402 -8.3; 442 -7.3; 486 -6.1; 535 -4.8; 588 -3.8; 647 -2.9; 712 -2.2; 783 -1.5; 861 -1.1; 947 -1.5; 1042 -2.3; 1146 -2.5; 1261 -1.2; 1387 -0.9; 1526 -2.7; 1678 -4.2; 1846 -4.6; 2031 -5.8; 2234 -8.9; 2457 -11.2; 2703 -11.0; 2973 -8.5; 3270 -5.1; 3597 -3.6; 3957 -5.3; 4353 -6.7; 4788 -6.7; 5267 -5.9; 5793 -6.4; 6373 -8.4; 7010 -8.7; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K340ED GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K340ED ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.6  | 6.5 dB  |
| Peaking | 266 Hz  | 0.33 | -5.2 dB |
| Peaking | 692 Hz  | 1.09 | 4.9 dB  |
| Peaking | 1288 Hz | 0.63 | 4.9 dB  |
| Peaking | 2489 Hz | 3.48 | -8.0 dB |
| Peaking | 1127 Hz | 4.74 | -1.0 dB |
| Peaking | 1334 Hz | 7.16 | 1.8 dB  |
| Peaking | 3443 Hz | 1.89 | -2.2 dB |
| Peaking | 3498 Hz | 4.69 | 5.1 dB  |
| Peaking | 6672 Hz | 6.86 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K340ED/AKG%20K340ED.png)