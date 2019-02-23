# Westone UM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.5; 34 -1.9; 37 -2.4; 41 -2.9; 45 -3.3; 49 -3.7; 54 -4.1; 60 -4.7; 66 -5.2; 72 -5.6; 79 -6.1; 87 -6.7; 96 -7.2; 106 -7.7; 116 -7.9; 128 -8.4; 141 -8.7; 155 -8.9; 170 -9.1; 187 -9.3; 206 -9.5; 227 -9.5; 249 -9.6; 274 -9.5; 302 -9.5; 332 -9.5; 365 -9.4; 402 -9.2; 442 -9.0; 486 -9.0; 535 -9.0; 588 -8.6; 647 -8.5; 712 -8.5; 783 -8.4; 861 -8.6; 947 -8.9; 1042 -9.3; 1146 -9.6; 1261 -9.9; 1387 -10.4; 1526 -10.7; 1678 -10.8; 1846 -10.2; 2031 -9.4; 2234 -8.4; 2457 -6.7; 2703 -5.2; 2973 -3.2; 3270 -2.1; 3597 -2.5; 3957 -3.5; 4353 -3.8; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.36 | 6.4 dB  |
| Peaking | 218 Hz  | 0.41 | -3.3 dB |
| Peaking | 1665 Hz | 1.11 | -4.5 dB |
| Peaking | 3215 Hz | 2.32 | 5.2 dB  |
| Peaking | 5605 Hz | 2.59 | 6.6 dB  |
| Peaking | 6557 Hz | 7.37 | 2.3 dB  |
| Peaking | 7687 Hz | 2.24 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20UM1/Westone%20UM1.png)