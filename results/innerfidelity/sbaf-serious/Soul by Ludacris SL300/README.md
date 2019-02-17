# Soul by Ludacris SL300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -1.7; 37 -4.5; 41 -8.7; 45 -11.1; 49 -11.7; 54 -11.4; 60 -10.8; 66 -9.9; 72 -9.1; 79 -8.6; 87 -8.3; 96 -8.3; 106 -8.1; 116 -8.0; 128 -8.1; 141 -8.2; 155 -8.2; 170 -8.2; 187 -8.1; 206 -8.0; 227 -7.8; 249 -7.8; 274 -7.5; 302 -7.4; 332 -7.5; 365 -7.7; 402 -8.1; 442 -8.5; 486 -9.6; 535 -10.4; 588 -8.9; 647 -5.6; 712 -0.7; 783 -0.5; 861 -1.1; 947 -5.3; 1042 -6.7; 1146 -8.7; 1261 -9.1; 1387 -8.4; 1526 -8.2; 1678 -7.5; 1846 -6.9; 2031 -6.8; 2234 -6.9; 2457 -5.0; 2703 -2.7; 2973 -0.5; 3270 -0.5; 3597 -3.1; 3957 -2.5; 4353 -9.7; 4788 -11.0; 5267 -8.1; 5793 -5.2; 6373 -1.7; 7010 -4.0; 7711 -6.2; 8482 -7.7; 9330 -8.6; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul by Ludacris SL300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul by Ludacris SL300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 32 Hz   | 0.79 | 15.9 dB  |
| Peaking | 46 Hz   | 0.95 | -15.9 dB |
| Peaking | 764 Hz  | 0.7  | -6.7 dB  |
| Peaking | 784 Hz  | 2.58 | 13.9 dB  |
| Peaking | 3098 Hz | 3.31 | 7.6 dB   |
| Peaking | 3873 Hz | 9.71 | 5.8 dB   |
| Peaking | 4395 Hz | 0.97 | 0.8 dB   |
| Peaking | 4580 Hz | 3.36 | -7.0 dB  |
| Peaking | 6476 Hz | 5.05 | 5.5 dB   |
| Peaking | 9179 Hz | 4    | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20by%20Ludacris%20SL300/Soul%20by%20Ludacris%20SL300.png)