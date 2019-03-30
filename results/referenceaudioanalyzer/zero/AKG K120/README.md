# AKG K120
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.7; 302 -0.8; 332 -1.1; 365 -1.3; 402 -1.4; 442 -1.7; 486 -1.9; 535 -2.9; 588 -5.1; 647 -7.8; 712 -9.6; 783 -10.4; 861 -10.7; 947 -10.8; 1042 -10.8; 1146 -10.6; 1261 -9.7; 1387 -8.1; 1526 -7.6; 1678 -8.6; 1846 -10.6; 2031 -13.5; 2234 -15.1; 2457 -14.6; 2703 -14.2; 2973 -15.7; 3270 -17.1; 3597 -18.2; 3957 -19.0; 4353 -18.7; 4788 -17.6; 5267 -15.3; 5793 -7.4; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 165 Hz  | 0.05 | 6.4 dB   |
| Peaking | 869 Hz  | 1.45 | -9.6 dB  |
| Peaking | 2485 Hz | 1.02 | -8.4 dB  |
| Peaking | 4484 Hz | 1.4  | -13.4 dB |
| Peaking | 6429 Hz | 2.81 | 10.0 dB  |
| Peaking | 508 Hz  | 3.25 | 1.3 dB   |
| Peaking | 671 Hz  | 4.05 | -2.5 dB  |
| Peaking | 1184 Hz | 3.16 | -4.9 dB  |
| Peaking | 1248 Hz | 1.2  | 3.4 dB   |
| Peaking | 2105 Hz | 5.7  | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 4.3 dB   |
| Peaking | 125 Hz   | 1.41 | 4.5 dB   |
| Peaking | 250 Hz   | 1.41 | 5.3 dB   |
| Peaking | 500 Hz   | 1.41 | 3.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -13.6 dB |
| Peaking | 8000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K120/AKG%20K120.png)