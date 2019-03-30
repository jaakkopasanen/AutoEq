# Sennheiser HD 451
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.8; 25 -6.3; 28 -6.9; 31 -7.4; 34 -7.7; 37 -8.1; 41 -8.4; 45 -8.7; 49 -8.8; 54 -8.9; 60 -9.1; 66 -9.0; 72 -8.7; 79 -8.4; 87 -7.9; 96 -7.1; 106 -7.1; 116 -8.1; 128 -8.9; 141 -9.4; 155 -9.5; 170 -9.2; 187 -8.8; 206 -8.4; 227 -7.9; 249 -7.2; 274 -6.4; 302 -6.2; 332 -6.1; 365 -5.8; 402 -5.6; 442 -5.8; 486 -5.9; 535 -5.9; 588 -5.9; 647 -5.6; 712 -5.2; 783 -4.7; 861 -4.3; 947 -4.5; 1042 -4.8; 1146 -4.6; 1261 -4.3; 1387 -4.4; 1526 -4.5; 1678 -4.3; 1846 -4.0; 2031 -3.7; 2234 -3.3; 2457 -3.4; 2703 -3.6; 2973 -3.4; 3270 -3.3; 3597 -3.5; 3957 -2.5; 4353 -0.5; 4788 -2.8; 5267 -6.4; 5793 -8.4; 6373 -9.0; 7010 -6.8; 7711 -5.0; 8482 -5.2; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 451 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 451 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 1.03 | -3.7 dB |
| Peaking | 166 Hz  | 1.34 | -3.8 dB |
| Peaking | 3162 Hz | 0.52 | 1.9 dB  |
| Peaking | 4422 Hz | 5.86 | 4.3 dB  |
| Peaking | 6034 Hz | 3.13 | -5.4 dB |
| Peaking | 98 Hz   | 2.01 | -1.1 dB |
| Peaking | 100 Hz  | 4.38 | 2.1 dB  |
| Peaking | 574 Hz  | 3.22 | -0.7 dB |
| Peaking | 852 Hz  | 5.79 | 0.7 dB  |
| Peaking | 2283 Hz | 7.4  | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20451/Sennheiser%20HD%20451.png)