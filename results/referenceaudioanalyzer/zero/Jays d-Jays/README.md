# Jays d-Jays
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.7; 28 -2.5; 31 -3.2; 34 -3.8; 37 -4.2; 41 -4.8; 45 -5.3; 49 -5.8; 54 -6.2; 60 -6.7; 66 -7.0; 72 -7.3; 79 -7.7; 87 -8.0; 96 -8.3; 106 -8.5; 116 -8.8; 128 -8.9; 141 -8.9; 155 -9.0; 170 -9.4; 187 -9.8; 206 -10.1; 227 -10.2; 249 -10.2; 274 -10.0; 302 -9.9; 332 -9.7; 365 -9.5; 402 -9.6; 442 -9.6; 486 -9.4; 535 -9.2; 588 -8.9; 647 -8.7; 712 -8.4; 783 -8.2; 861 -7.9; 947 -7.6; 1042 -7.5; 1146 -7.3; 1261 -7.6; 1387 -7.7; 1526 -8.0; 1678 -8.4; 1846 -8.6; 2031 -8.0; 2234 -6.6; 2457 -5.4; 2703 -5.8; 2973 -7.1; 3270 -7.2; 3597 -5.8; 3957 -5.0; 4353 -6.4; 4788 -7.6; 5267 -6.4; 5793 -2.3; 6373 -0.6; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays d-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays d-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.68 | 6.6 dB  |
| Peaking | 215 Hz  | 0.13 | -2.0 dB |
| Peaking | 250 Hz  | 0.62 | -2.1 dB |
| Peaking | 3848 Hz | 0.31 | -0.3 dB |
| Peaking | 6337 Hz | 5.48 | 6.7 dB  |
| Peaking | 1130 Hz | 1.84 | 1.0 dB  |
| Peaking | 2215 Hz | 1.21 | -2.4 dB |
| Peaking | 2443 Hz | 3.73 | 3.9 dB  |
| Peaking | 3908 Hz | 5.71 | 2.2 dB  |
| Peaking | 4842 Hz | 7.76 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Jays%20d-Jays/Jays%20d-Jays.png)