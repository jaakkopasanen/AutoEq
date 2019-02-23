# Sennheiser HD 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.2; 45 -1.7; 49 -2.1; 54 -2.6; 60 -3.1; 66 -3.7; 72 -4.2; 79 -4.6; 87 -5.2; 96 -5.7; 106 -6.3; 116 -6.7; 128 -7.1; 141 -7.5; 155 -7.7; 170 -7.8; 187 -7.8; 206 -7.7; 227 -7.5; 249 -7.4; 274 -7.3; 302 -7.3; 332 -7.3; 365 -7.1; 402 -7.1; 442 -7.1; 486 -7.1; 535 -7.0; 588 -6.9; 647 -6.7; 712 -6.6; 783 -6.5; 861 -6.4; 947 -5.9; 1042 -6.0; 1146 -6.4; 1261 -6.7; 1387 -7.1; 1526 -7.2; 1678 -7.5; 1846 -7.7; 2031 -7.8; 2234 -7.1; 2457 -6.8; 2703 -6.9; 2973 -7.4; 3270 -7.6; 3597 -7.2; 3957 -6.5; 4353 -5.8; 4788 -6.0; 5267 -5.6; 5793 -4.4; 6373 -3.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.1; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.4  | 6.3 dB  |
| Peaking | 149 Hz  | 0.66 | -2.3 dB |
| Peaking | 1883 Hz | 3.16 | -1.4 dB |
| Peaking | 3239 Hz | 5.48 | -1.2 dB |
| Peaking | 6390 Hz | 4.12 | 3.7 dB  |
| Peaking | 994 Hz  | 6.57 | 1.0 dB  |
| Peaking | 4401 Hz | 7.94 | 0.6 dB  |
| Peaking | 8178 Hz | 5.32 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)