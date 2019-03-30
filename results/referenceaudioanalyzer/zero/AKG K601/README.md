# AKG K601
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.4; 54 -1.7; 60 -1.6; 66 -1.7; 72 -2.2; 79 -2.9; 87 -3.2; 96 -3.5; 106 -3.9; 116 -4.2; 128 -4.4; 141 -4.6; 155 -4.6; 170 -4.6; 187 -4.8; 206 -4.9; 227 -4.9; 249 -4.7; 274 -4.6; 302 -4.6; 332 -4.6; 365 -4.4; 402 -4.3; 442 -4.3; 486 -4.3; 535 -4.3; 588 -4.2; 647 -4.0; 712 -4.0; 783 -3.9; 861 -3.6; 947 -3.7; 1042 -4.0; 1146 -4.3; 1261 -4.6; 1387 -4.7; 1526 -5.1; 1678 -5.9; 1846 -6.9; 2031 -7.9; 2234 -8.4; 2457 -8.2; 2703 -7.2; 2973 -5.7; 3270 -5.2; 3597 -7.2; 3957 -8.6; 4353 -8.9; 4788 -9.1; 5267 -9.3; 5793 -10.5; 6373 -14.0; 7010 -16.9; 7711 -17.4; 8482 -15.1; 9330 -11.9; 10263 -9.5; 11289 -9.1; 12418 -9.6; 13660 -8.7; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.39 | 6.2 dB   |
| Peaking | 927 Hz   | 0.34 | 2.7 dB   |
| Peaking | 2152 Hz  | 2.61 | -3.6 dB  |
| Peaking | 7480 Hz  | 1.89 | -11.6 dB |
| Peaking | 12838 Hz | 3.63 | -2.0 dB  |
| Peaking | 3217 Hz  | 4.69 | 3.3 dB   |
| Peaking | 3716 Hz  | 1.72 | -2.0 dB  |
| Peaking | 5555 Hz  | 5.7  | 1.4 dB   |
| Peaking | 15652 Hz | 3.23 | 0.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.6 dB   |
| Peaking | 125 Hz   | 1.41 | 1.1 dB   |
| Peaking | 250 Hz   | 1.41 | 1.1 dB   |
| Peaking | 500 Hz   | 1.41 | 1.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K601/AKG%20K601.png)