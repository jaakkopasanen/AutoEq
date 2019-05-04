# Sennheiser HD 599
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.3; 31 -1.9; 34 -2.4; 37 -2.8; 41 -3.2; 45 -3.6; 49 -4.0; 54 -4.5; 60 -5.1; 66 -5.6; 72 -6.0; 79 -6.5; 87 -7.0; 96 -7.6; 106 -8.1; 116 -8.5; 128 -8.9; 141 -9.2; 155 -9.4; 170 -9.4; 187 -9.3; 206 -9.1; 227 -8.8; 249 -8.6; 274 -8.5; 302 -8.3; 332 -8.0; 365 -7.8; 402 -7.6; 442 -7.3; 486 -7.2; 535 -7.0; 588 -6.7; 647 -6.1; 712 -5.6; 783 -5.3; 861 -5.0; 947 -4.9; 1042 -4.7; 1146 -4.3; 1261 -4.1; 1387 -3.5; 1526 -2.8; 1678 -2.5; 1846 -3.5; 2031 -5.1; 2234 -5.8; 2457 -5.2; 2703 -5.5; 2973 -6.6; 3270 -7.5; 3597 -7.1; 3957 -7.3; 4353 -8.6; 4788 -7.9; 5267 -6.3; 5793 -5.9; 6373 -3.6; 7010 -4.0; 7711 -6.2; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -10.6; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 599 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 599 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.31 | 6.6 dB  |
| Peaking | 158 Hz  | 0.59 | -3.4 dB |
| Peaking | 1541 Hz | 1.01 | 3.9 dB  |
| Peaking | 4478 Hz | 0.73 | -2.1 dB |
| Peaking | 6560 Hz | 3.87 | 4.7 dB  |
| Peaking | 831 Hz  | 1.9  | 1.4 dB  |
| Peaking | 1051 Hz | 0.78 | -1.0 dB |
| Peaking | 1701 Hz | 3.71 | 1.6 dB  |
| Peaking | 2159 Hz | 3.24 | -1.4 dB |
| Peaking | 2559 Hz | 5.1  | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20599/Sennheiser%20HD%20599.png)