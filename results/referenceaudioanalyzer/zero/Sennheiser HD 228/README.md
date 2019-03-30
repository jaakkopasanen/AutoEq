# Sennheiser HD 228
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.0; 54 -1.7; 60 -2.6; 66 -3.3; 72 -3.7; 79 -4.0; 87 -4.2; 96 -4.3; 106 -4.9; 116 -5.9; 128 -6.7; 141 -7.5; 155 -8.0; 170 -8.3; 187 -8.4; 206 -8.6; 227 -9.4; 249 -9.9; 274 -10.0; 302 -9.6; 332 -9.2; 365 -8.5; 402 -7.9; 442 -7.2; 486 -6.8; 535 -6.7; 588 -6.4; 647 -5.9; 712 -5.6; 783 -5.2; 861 -4.9; 947 -4.6; 1042 -4.3; 1146 -4.1; 1261 -3.7; 1387 -3.3; 1526 -2.9; 1678 -2.5; 1846 -2.0; 2031 -1.4; 2234 -1.0; 2457 -1.0; 2703 -1.6; 2973 -1.6; 3270 -0.7; 3597 -0.9; 3957 -2.1; 4353 -3.4; 4788 -7.6; 5267 -12.3; 5793 -13.4; 6373 -12.5; 7010 -12.7; 7711 -13.9; 8482 -14.1; 9330 -12.1; 10263 -8.8; 11289 -6.8; 12418 -6.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 228 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.48 | 6.4 dB   |
| Peaking | 248 Hz  | 0.96 | -4.0 dB  |
| Peaking | 4187 Hz | 0.4  | 8.1 dB   |
| Peaking | 5558 Hz | 2.63 | -10.9 dB |
| Peaking | 8131 Hz | 1.58 | -11.9 dB |
| Peaking | 101 Hz  | 3.72 | 1.1 dB   |
| Peaking | 145 Hz  | 1.08 | -0.7 dB  |
| Peaking | 202 Hz  | 4.59 | 1.1 dB   |
| Peaking | 2877 Hz | 4.6  | -2.2 dB  |
| Peaking | 3163 Hz | 2.13 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.3 dB |
| Peaking | 16000 Hz | 1.41 | 1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)