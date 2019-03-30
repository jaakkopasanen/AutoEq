# Sennheiser HD 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.7; 28 -2.5; 31 -3.2; 34 -3.8; 37 -4.3; 41 -4.9; 45 -5.4; 49 -5.9; 54 -6.2; 60 -6.1; 66 -6.1; 72 -6.4; 79 -6.8; 87 -7.3; 96 -7.8; 106 -8.0; 116 -8.0; 128 -8.0; 141 -8.0; 155 -8.0; 170 -7.7; 187 -7.6; 206 -7.4; 227 -7.1; 249 -6.9; 274 -6.7; 302 -6.4; 332 -6.3; 365 -6.1; 402 -6.0; 442 -5.7; 486 -5.7; 535 -5.4; 588 -5.4; 647 -5.4; 712 -5.4; 783 -5.3; 861 -5.1; 947 -5.1; 1042 -5.4; 1146 -5.8; 1261 -6.0; 1387 -5.9; 1526 -5.6; 1678 -5.0; 1846 -4.6; 2031 -4.4; 2234 -4.8; 2457 -5.4; 2703 -6.1; 2973 -7.0; 3270 -8.0; 3597 -8.7; 3957 -9.0; 4353 -9.6; 4788 -10.9; 5267 -12.1; 5793 -11.8; 6373 -9.1; 7010 -4.6; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.05 | 5.9 dB  |
| Peaking | 132 Hz  | 0.85 | -2.1 dB |
| Peaking | 702 Hz  | 0.95 | 1.1 dB  |
| Peaking | 2015 Hz | 3.4  | 2.1 dB  |
| Peaking | 5123 Hz | 2.42 | -6.2 dB |
| Peaking | 3665 Hz | 2.61 | -2.6 dB |
| Peaking | 4998 Hz | 1.04 | 2.1 dB  |
| Peaking | 5926 Hz | 3.67 | -3.5 dB |
| Peaking | 6961 Hz | 6.44 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)