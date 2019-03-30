# Sennheiser HD 215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.6; 25 -12.6; 28 -12.7; 31 -12.8; 34 -12.8; 37 -12.7; 41 -12.6; 45 -12.4; 49 -12.2; 54 -11.8; 60 -11.0; 66 -10.1; 72 -9.1; 79 -8.1; 87 -7.6; 96 -8.2; 106 -9.3; 116 -10.2; 128 -10.8; 141 -10.7; 155 -10.2; 170 -9.3; 187 -8.2; 206 -6.6; 227 -4.6; 249 -3.3; 274 -3.1; 302 -3.6; 332 -4.5; 365 -5.5; 402 -5.9; 442 -5.9; 486 -6.1; 535 -6.6; 588 -7.1; 647 -7.5; 712 -8.0; 783 -8.4; 861 -8.3; 947 -6.5; 1042 -4.0; 1146 -4.0; 1261 -5.6; 1387 -6.6; 1526 -7.3; 1678 -7.9; 1846 -8.3; 2031 -8.6; 2234 -8.1; 2457 -7.2; 2703 -5.9; 2973 -4.4; 3270 -2.7; 3597 -0.8; 3957 -0.5; 4353 -4.0; 4788 -7.7; 5267 -9.3; 5793 -11.1; 6373 -12.5; 7010 -10.8; 7711 -6.4; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -7.3; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.71 | -6.9 dB |
| Peaking | 145 Hz  | 2.04 | -4.2 dB |
| Peaking | 266 Hz  | 2.56 | 4.5 dB  |
| Peaking | 3774 Hz | 3.9  | 7.4 dB  |
| Peaking | 6133 Hz | 2.92 | -6.6 dB |
| Peaking | 86 Hz   | 6.93 | 1.5 dB  |
| Peaking | 819 Hz  | 2.64 | -2.7 dB |
| Peaking | 1084 Hz | 4.24 | 3.9 dB  |
| Peaking | 1956 Hz | 2.87 | -2.5 dB |
| Peaking | 8002 Hz | 7.05 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20215/Sennheiser%20HD%20215.png)