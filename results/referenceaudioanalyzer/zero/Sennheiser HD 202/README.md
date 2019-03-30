# Sennheiser HD 202
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.6; 34 -2.7; 37 -3.6; 41 -4.7; 45 -5.6; 49 -6.2; 54 -6.5; 60 -6.6; 66 -6.8; 72 -7.4; 79 -8.1; 87 -8.5; 96 -8.8; 106 -8.8; 116 -8.7; 128 -8.3; 141 -7.8; 155 -7.1; 170 -6.5; 187 -5.8; 206 -5.4; 227 -4.9; 249 -4.6; 274 -4.3; 302 -4.5; 332 -5.2; 365 -5.9; 402 -6.3; 442 -6.6; 486 -6.9; 535 -7.1; 588 -7.4; 647 -7.7; 712 -8.1; 783 -8.4; 861 -8.5; 947 -8.5; 1042 -8.7; 1146 -9.1; 1261 -9.4; 1387 -9.6; 1526 -9.8; 1678 -9.8; 1846 -9.3; 2031 -8.6; 2234 -7.8; 2457 -6.9; 2703 -5.7; 2973 -4.8; 3270 -3.9; 3597 -2.2; 3957 -3.8; 4353 -8.1; 4788 -9.9; 5267 -8.8; 5793 -5.5; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.0; 13660 -8.5; 15026 -6.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 2.04 | 7.2 dB  |
| Peaking | 1471 Hz  | 0.99 | -3.5 dB |
| Peaking | 3707 Hz  | 2.16 | 8.1 dB  |
| Peaking | 4692 Hz  | 2.1  | -7.3 dB |
| Peaking | 6423 Hz  | 4.51 | 6.1 dB  |
| Peaking | 36 Hz    | 3.17 | 1.4 dB  |
| Peaking | 105 Hz   | 1.34 | -2.8 dB |
| Peaking | 260 Hz   | 1.6  | 2.7 dB  |
| Peaking | 692 Hz   | 2.14 | -0.8 dB |
| Peaking | 13358 Hz | 4.11 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20202/Sennheiser%20HD%20202.png)