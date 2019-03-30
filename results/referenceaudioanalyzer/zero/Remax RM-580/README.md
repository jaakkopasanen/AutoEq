# Remax RM-580
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.0; 23 -18.0; 25 -17.9; 28 -17.8; 31 -17.7; 34 -17.5; 37 -17.4; 41 -17.1; 45 -16.9; 49 -16.7; 54 -16.3; 60 -15.9; 66 -15.4; 72 -14.9; 79 -14.4; 87 -14.0; 96 -13.8; 106 -13.6; 116 -12.9; 128 -12.2; 141 -11.5; 155 -10.7; 170 -10.1; 187 -9.9; 206 -9.7; 227 -8.9; 249 -8.1; 274 -7.5; 302 -6.9; 332 -6.3; 365 -5.6; 402 -5.0; 442 -4.5; 486 -4.1; 535 -3.8; 588 -3.5; 647 -3.1; 712 -2.1; 783 -1.5; 861 -1.8; 947 -2.2; 1042 -2.6; 1146 -3.2; 1261 -3.9; 1387 -4.9; 1526 -5.9; 1678 -7.1; 1846 -8.1; 2031 -9.1; 2234 -9.4; 2457 -8.4; 2703 -6.8; 2973 -5.9; 3270 -6.2; 3597 -7.9; 3957 -9.2; 4353 -8.9; 4788 -6.5; 5267 -2.9; 5793 -0.5; 6373 -1.7; 7010 -3.3; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Remax RM-580 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Remax RM-580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.25 | -10.1 dB |
| Peaking | 1022 Hz | 0.61 | 9.5 dB   |
| Peaking | 1699 Hz | 0.55 | -8.0 dB  |
| Peaking | 5952 Hz | 3.91 | 6.8 dB   |
| Peaking | 16 Hz   | 0.67 | -3.6 dB  |
| Peaking | 21 Hz   | 0.54 | -0.4 dB  |
| Peaking | 2228 Hz | 2.53 | -3.2 dB  |
| Peaking | 3121 Hz | 1.24 | 4.3 dB   |
| Peaking | 4025 Hz | 2.99 | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.1 dB |
| Peaking | 62 Hz    | 1.41 | -7.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Remax%20RM-580/Remax%20RM-580.png)