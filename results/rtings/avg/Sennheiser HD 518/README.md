# Sennheiser HD 518
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.3; 41 -2.1; 45 -2.9; 49 -3.5; 54 -4.2; 60 -4.9; 66 -5.6; 72 -6.1; 79 -6.7; 87 -7.3; 96 -7.8; 106 -8.3; 116 -8.9; 128 -9.3; 141 -9.5; 155 -9.6; 170 -9.7; 187 -9.7; 206 -9.5; 227 -9.2; 249 -9.0; 274 -9.0; 302 -8.9; 332 -8.7; 365 -8.5; 402 -8.4; 442 -8.4; 486 -8.3; 535 -8.1; 588 -7.8; 647 -7.4; 712 -6.8; 783 -6.8; 861 -6.6; 947 -6.4; 1042 -6.0; 1146 -5.4; 1261 -4.9; 1387 -4.1; 1526 -3.0; 1678 -2.5; 1846 -2.9; 2031 -3.6; 2234 -4.4; 2457 -4.7; 2703 -4.2; 2973 -4.7; 3270 -6.0; 3597 -6.6; 3957 -6.9; 4353 -8.0; 4788 -7.3; 5267 -5.9; 5793 -4.6; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -10.0; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 518 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 518 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.48 | 7.1 dB  |
| Peaking | 138 Hz  | 0.37 | -4.0 dB |
| Peaking | 1676 Hz | 2.01 | 4.2 dB  |
| Peaking | 2746 Hz | 5.63 | 1.6 dB  |
| Peaking | 6466 Hz | 6.83 | 5.5 dB  |
| Peaking | 2533 Hz | 1.82 | 0.2 dB  |
| Peaking | 4450 Hz | 3.59 | -2.0 dB |
| Peaking | 5673 Hz | 4.42 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20518/Sennheiser%20HD%20518.png)