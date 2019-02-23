# Jays A Jays 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.6; 25 -4.9; 28 -5.3; 31 -5.5; 34 -5.7; 37 -5.9; 41 -6.1; 45 -6.3; 49 -6.4; 54 -6.5; 60 -6.7; 66 -6.9; 72 -7.0; 79 -7.2; 87 -7.4; 96 -7.5; 106 -7.5; 116 -7.4; 128 -7.3; 141 -7.2; 155 -7.0; 170 -6.7; 187 -6.4; 206 -6.1; 227 -5.6; 249 -5.3; 274 -4.7; 302 -4.3; 332 -3.8; 365 -3.3; 402 -2.8; 442 -2.3; 486 -2.0; 535 -1.6; 588 -1.0; 647 -0.8; 712 -0.7; 783 -0.5; 861 -0.7; 947 -1.1; 1042 -1.6; 1146 -2.1; 1261 -2.7; 1387 -3.5; 1526 -4.5; 1678 -5.4; 1846 -6.1; 2031 -6.8; 2234 -8.0; 2457 -9.3; 2703 -9.9; 2973 -7.4; 3270 -3.7; 3597 -1.3; 3957 -1.2; 4353 -3.3; 4788 -5.0; 5267 -6.5; 5793 -8.8; 6373 -7.6; 7010 -4.2; 7711 -4.2; 8482 -4.4; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays A Jays 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays A Jays 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.48 | -3.2 dB |
| Peaking | 726 Hz  | 0.71 | 4.5 dB  |
| Peaking | 2712 Hz | 1.54 | -8.2 dB |
| Peaking | 3592 Hz | 2.46 | 7.7 dB  |
| Peaking | 5830 Hz | 5.07 | -4.9 dB |
| Peaking | 6462 Hz | 7.44 | -1.4 dB |
| Peaking | 6763 Hz | 3.03 | -0.1 dB |
| Peaking | 7124 Hz | 4.94 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jays%20A%20Jays%205/Jays%20A%20Jays%205.png)