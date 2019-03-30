# AKG Y20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.8; 23 -16.8; 25 -16.8; 28 -16.8; 31 -16.8; 34 -16.8; 37 -16.8; 41 -16.7; 45 -16.6; 49 -16.5; 54 -16.4; 60 -16.3; 66 -16.1; 72 -16.0; 79 -15.8; 87 -15.6; 96 -15.3; 106 -15.0; 116 -14.7; 128 -14.4; 141 -13.9; 155 -13.5; 170 -13.0; 187 -12.4; 206 -11.9; 227 -11.3; 249 -10.7; 274 -10.2; 302 -9.7; 332 -9.3; 365 -8.8; 402 -8.1; 442 -7.4; 486 -6.6; 535 -5.9; 588 -5.2; 647 -4.4; 712 -3.7; 783 -3.1; 861 -2.4; 947 -1.8; 1042 -1.2; 1146 -0.6; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -1.1; 2457 -2.3; 2703 -3.9; 2973 -5.7; 3270 -7.2; 3597 -7.8; 3957 -8.0; 4353 -8.4; 4788 -9.0; 5267 -11.0; 5793 -13.8; 6373 -14.0; 7010 -9.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Y20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Y20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.13 | -10.3 dB |
| Peaking | 1472 Hz  | 0.6  | 7.5 dB   |
| Peaking | 6365 Hz  | 1.36 | -20.5 dB |
| Peaking | 7180 Hz  | 1.24 | 13.9 dB  |
| Peaking | 1531 Hz  | 3.19 | -0.9 dB  |
| Peaking | 2266 Hz  | 2.13 | 1.6 dB   |
| Peaking | 3244 Hz  | 2.59 | -1.9 dB  |
| Peaking | 4749 Hz  | 5.65 | 1.2 dB   |
| Peaking | 13711 Hz | 1.78 | 0.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.7 dB |
| Peaking | 62 Hz    | 1.41 | -7.1 dB  |
| Peaking | 125 Hz   | 1.41 | -6.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 16000 Hz | 1.41 | 0.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20Y20/AKG%20Y20.png)