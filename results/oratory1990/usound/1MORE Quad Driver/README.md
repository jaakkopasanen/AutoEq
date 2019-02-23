# 1MORE Quad Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.6; 25 -2.2; 28 -2.7; 31 -3.3; 34 -3.9; 37 -4.4; 41 -5.1; 45 -5.6; 49 -6.2; 54 -7.0; 60 -7.6; 66 -8.5; 72 -8.8; 79 -9.6; 87 -9.7; 96 -10.0; 106 -10.6; 116 -10.6; 128 -11.1; 141 -11.0; 155 -11.1; 170 -11.2; 187 -11.2; 206 -11.1; 227 -10.9; 249 -10.7; 274 -10.3; 302 -10.0; 332 -9.6; 365 -9.1; 402 -8.6; 442 -8.1; 486 -7.5; 535 -6.9; 588 -6.3; 647 -5.6; 712 -4.9; 783 -4.1; 861 -3.5; 947 -3.0; 1042 -3.0; 1146 -3.3; 1261 -3.6; 1387 -3.8; 1526 -3.8; 1678 -3.5; 1846 -3.3; 2031 -3.3; 2234 -3.7; 2457 -4.3; 2703 -4.8; 2973 -4.7; 3270 -4.2; 3597 -4.1; 3957 -5.0; 4353 -5.9; 4788 -5.1; 5267 -3.3; 5793 -1.7; 6373 -0.5; 7010 -4.3; 7711 -5.5; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -8.1; 13660 -11.4; 15026 -13.0; 16529 -14.3; 18182 -15.5; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.34 | 6.4 dB   |
| Peaking | 201 Hz   | 0.23 | -6.6 dB  |
| Peaking | 923 Hz   | 0.5  | 5.3 dB   |
| Peaking | 6177 Hz  | 3.78 | 5.7 dB   |
| Peaking | 18175 Hz | 0.64 | -10.6 dB |
| Peaking | 1402 Hz  | 2.44 | -2.3 dB  |
| Peaking | 1416 Hz  | 1.31 | 1.6 dB   |
| Peaking | 4443 Hz  | 8.97 | -1.4 dB  |
| Peaking | 11339 Hz | 2.42 | 2.8 dB   |
| Peaking | 14073 Hz | 2.24 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB   |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -11.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/1MORE%20Quad%20Driver/1MORE%20Quad%20Driver.png)