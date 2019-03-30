# Sennheiser Momentum on-ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.2; 25 -7.3; 28 -7.4; 31 -7.5; 34 -7.6; 37 -7.7; 41 -7.7; 45 -7.7; 49 -7.7; 54 -7.7; 60 -7.7; 66 -7.7; 72 -7.7; 79 -7.7; 87 -7.5; 96 -7.3; 106 -7.4; 116 -7.4; 128 -7.3; 141 -7.0; 155 -6.7; 170 -6.4; 187 -5.9; 206 -5.2; 227 -4.4; 249 -3.9; 274 -3.5; 302 -3.3; 332 -3.0; 365 -2.6; 402 -2.1; 442 -1.6; 486 -1.2; 535 -1.2; 588 -1.6; 647 -2.1; 712 -2.6; 783 -3.3; 861 -3.8; 947 -4.2; 1042 -4.7; 1146 -5.3; 1261 -6.0; 1387 -6.7; 1526 -7.6; 1678 -8.4; 1846 -9.1; 2031 -9.3; 2234 -9.2; 2457 -8.4; 2703 -7.4; 2973 -6.2; 3270 -5.0; 3597 -3.2; 3957 -0.5; 4353 -1.4; 4788 -6.1; 5267 -8.5; 5793 -8.6; 6373 -8.2; 7010 -8.0; 7711 -6.3; 8482 -5.0; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum on-ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum on-ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 0.24 | -2.9 dB |
| Peaking | 466 Hz  | 0.69 | 4.6 dB  |
| Peaking | 1998 Hz | 1.22 | -4.9 dB |
| Peaking | 4127 Hz | 3.07 | 8.1 dB  |
| Peaking | 5414 Hz | 1.94 | -5.4 dB |
| Peaking | 246 Hz  | 5.28 | 0.6 dB  |
| Peaking | 360 Hz  | 5.4  | -0.5 dB |
| Peaking | 7104 Hz | 4.79 | -2.3 dB |
| Peaking | 7948 Hz | 2.15 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20Momentum%20on-ear/Sennheiser%20Momentum%20on-ear.png)