# 1MORE Quad Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.6; 25 -2.2; 28 -2.7; 31 -3.3; 34 -3.9; 37 -4.4; 41 -5.1; 45 -5.6; 49 -6.2; 54 -7.0; 60 -7.6; 66 -8.5; 72 -8.8; 79 -9.6; 87 -9.7; 96 -10.0; 106 -10.6; 116 -10.6; 128 -11.1; 141 -11.0; 155 -11.1; 170 -11.2; 187 -11.2; 206 -11.1; 227 -10.9; 249 -10.7; 274 -10.3; 302 -10.0; 332 -9.6; 365 -9.1; 402 -8.6; 442 -8.1; 486 -7.5; 535 -6.9; 588 -6.3; 647 -5.6; 712 -4.9; 783 -4.1; 861 -3.5; 947 -3.0; 1042 -3.0; 1146 -3.3; 1261 -3.6; 1387 -3.8; 1526 -3.8; 1678 -3.5; 1846 -3.3; 2031 -3.3; 2234 -3.7; 2457 -4.3; 2703 -4.8; 2973 -4.7; 3270 -4.2; 3597 -4.1; 3957 -5.0; 4353 -5.9; 4788 -5.1; 5267 -3.3; 5793 -1.7; 6373 -0.5; 7010 -4.2; 7711 -2.7; 8482 -2.9; 9330 -2.9; 10263 -2.9; 11289 -4.1; 12418 -8.1; 13660 -11.4; 15026 -13.0; 16529 -14.3; 18182 -15.5; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.78 | 4.1 dB   |
| Peaking | 119 Hz   | 0.46 | -7.3 dB  |
| Peaking | 316 Hz   | 0.83 | -3.7 dB  |
| Peaking | 4265 Hz  | 5.42 | -2.8 dB  |
| Peaking | 18099 Hz | 0.66 | -14.1 dB |
| Peaking | 954 Hz   | 4.13 | 1.3 dB   |
| Peaking | 2789 Hz  | 2.98 | -1.6 dB  |
| Peaking | 6147 Hz  | 7.69 | 3.6 dB   |
| Peaking | 10509 Hz | 1.76 | 3.7 dB   |
| Peaking | 13719 Hz | 1.88 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB   |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.8 dB  |
| Peaking | 250 Hz   | 1.41 | -6.6 dB  |
| Peaking | 500 Hz   | 1.41 | -3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -16.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/1MORE%20Quad%20Driver/1MORE%20Quad%20Driver.png)