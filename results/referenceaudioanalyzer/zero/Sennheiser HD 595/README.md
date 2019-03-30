# Sennheiser HD 595
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.5; 34 -2.3; 37 -2.9; 41 -3.5; 45 -3.9; 49 -4.1; 54 -4.4; 60 -4.9; 66 -5.5; 72 -5.9; 79 -6.1; 87 -6.3; 96 -6.6; 106 -6.7; 116 -6.9; 128 -7.0; 141 -7.2; 155 -7.4; 170 -7.5; 187 -7.6; 206 -7.6; 227 -7.6; 249 -7.6; 274 -7.6; 302 -7.6; 332 -7.6; 365 -7.4; 402 -7.3; 442 -7.3; 486 -7.2; 535 -7.0; 588 -7.0; 647 -6.8; 712 -6.5; 783 -6.3; 861 -6.3; 947 -6.4; 1042 -6.7; 1146 -7.1; 1261 -7.4; 1387 -7.4; 1526 -7.3; 1678 -6.8; 1846 -5.8; 2031 -4.6; 2234 -4.2; 2457 -4.9; 2703 -6.0; 2973 -6.4; 3270 -5.9; 3597 -4.7; 3957 -4.8; 4353 -6.5; 4788 -8.1; 5267 -8.0; 5793 -6.2; 6373 -3.8; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.3; 12418 -6.9; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 595 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.14 | 6.4 dB  |
| Peaking | 2268 Hz | 2.04 | 5.3 dB  |
| Peaking | 3256 Hz | 0.58 | -4.1 dB |
| Peaking | 3731 Hz | 3.18 | 5.1 dB  |
| Peaking | 6625 Hz | 3.98 | 5.0 dB  |
| Peaking | 52 Hz   | 2.65 | 0.8 dB  |
| Peaking | 223 Hz  | 0.62 | -1.2 dB |
| Peaking | 846 Hz  | 2.6  | 1.0 dB  |
| Peaking | 5087 Hz | 9.56 | -0.9 dB |
| Peaking | 9412 Hz | 4.41 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20595/Sennheiser%20HD%20595.png)