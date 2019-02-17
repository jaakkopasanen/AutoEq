# Takstar Pro 80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.9; 25 -4.2; 28 -4.6; 31 -4.9; 34 -5.1; 37 -5.2; 41 -5.3; 45 -5.4; 49 -5.5; 54 -5.7; 60 -5.7; 66 -5.9; 72 -6.0; 79 -6.2; 87 -6.5; 96 -6.7; 106 -6.7; 116 -6.9; 128 -7.4; 141 -8.0; 155 -7.8; 170 -7.6; 187 -7.9; 206 -7.8; 227 -7.6; 249 -7.4; 274 -7.1; 302 -6.7; 332 -6.2; 365 -5.7; 402 -5.0; 442 -4.4; 486 -4.5; 535 -4.6; 588 -4.6; 647 -5.1; 712 -5.6; 783 -5.6; 861 -5.2; 947 -6.0; 1042 -6.5; 1146 -6.9; 1261 -7.7; 1387 -8.4; 1526 -9.5; 1678 -10.0; 1846 -10.4; 2031 -10.2; 2234 -8.7; 2457 -5.9; 2703 -3.1; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.7; 5267 -2.4; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.7; 9330 -10.7; 10263 -9.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Takstar Pro 80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Takstar Pro 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.13 | 2.8 dB   |
| Peaking | 1960 Hz | 1.09 | -16.8 dB |
| Peaking | 2607 Hz | 0.53 | 14.0 dB  |
| Peaking | 6228 Hz | 6.34 | 2.9 dB   |
| Peaking | 9221 Hz | 2.37 | -6.7 dB  |
| Peaking | 196 Hz  | 1.15 | -1.7 dB  |
| Peaking | 475 Hz  | 1.89 | 1.9 dB   |
| Peaking | 1311 Hz | 3.38 | -0.8 dB  |
| Peaking | 4794 Hz | 2.45 | 1.7 dB   |
| Peaking | 4930 Hz | 8.29 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Takstar%20Pro%2080/Takstar%20Pro%2080.png)