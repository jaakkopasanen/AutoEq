# Sennheiser HD 518
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -1.8; 41 -2.7; 45 -3.4; 49 -4.1; 54 -4.7; 60 -5.4; 66 -6.2; 72 -6.7; 79 -7.3; 87 -7.8; 96 -8.3; 106 -9.0; 116 -9.5; 128 -9.9; 141 -10.1; 155 -10.2; 170 -10.3; 187 -10.2; 206 -10.0; 227 -9.7; 249 -9.5; 274 -9.4; 302 -9.3; 332 -9.1; 365 -8.9; 402 -8.9; 442 -8.7; 486 -8.6; 535 -8.4; 588 -8.1; 647 -7.7; 712 -7.0; 783 -7.0; 861 -6.9; 947 -6.7; 1042 -6.2; 1146 -5.7; 1261 -5.1; 1387 -4.3; 1526 -3.2; 1678 -2.6; 1846 -3.0; 2031 -3.5; 2234 -3.9; 2457 -4.1; 2703 -4.0; 2973 -4.9; 3270 -6.6; 3597 -7.2; 3957 -7.5; 4353 -8.8; 4788 -7.3; 5267 -5.9; 5793 -5.1; 6373 -2.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.7; 18182 -10.4; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 518 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 518 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.5  | 7.4 dB  |
| Peaking | 137 Hz  | 0.31 | -4.5 dB |
| Peaking | 1830 Hz | 1.28 | 4.0 dB  |
| Peaking | 4246 Hz | 3.55 | -2.8 dB |
| Peaking | 6508 Hz | 5.44 | 4.4 dB  |
| Peaking | 301 Hz  | 1.17 | 1.5 dB  |
| Peaking | 326 Hz  | 0.65 | -1.1 dB |
| Peaking | 712 Hz  | 7.2  | 0.6 dB  |
| Peaking | 2790 Hz | 8.04 | 1.2 dB  |
| Peaking | 3351 Hz | 8.73 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20518/Sennheiser%20HD%20518.png)