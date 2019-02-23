# Soul by Ludacris SL100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.6; 25 -4.1; 28 -4.7; 31 -5.1; 34 -5.5; 37 -5.9; 41 -6.3; 45 -6.6; 49 -6.9; 54 -7.2; 60 -7.1; 66 -7.0; 72 -7.8; 79 -8.9; 87 -10.0; 96 -10.7; 106 -11.0; 116 -11.3; 128 -11.6; 141 -11.8; 155 -12.0; 170 -12.2; 187 -12.4; 206 -12.4; 227 -12.0; 249 -11.8; 274 -11.6; 302 -11.7; 332 -12.1; 365 -11.7; 402 -11.4; 442 -10.9; 486 -10.4; 535 -9.6; 588 -8.3; 647 -6.7; 712 -5.0; 783 -3.6; 861 -3.3; 947 -3.9; 1042 -5.2; 1146 -6.8; 1261 -8.0; 1387 -8.6; 1526 -8.6; 1678 -7.9; 1846 -6.2; 2031 -4.3; 2234 -2.8; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -4.9; 4788 -7.3; 5267 -5.7; 5793 -6.8; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul by Ludacris SL100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul by Ludacris SL100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 10 Hz   | 0.51 | 5.4 dB   |
| Peaking | 141 Hz  | 0.72 | -4.1 dB  |
| Peaking | 835 Hz  | 1.28 | 12.8 dB  |
| Peaking | 994 Hz  | 0.33 | -10.4 dB |
| Peaking | 2824 Hz | 1.04 | 11.9 dB  |
| Peaking | 1572 Hz | 4.43 | -1.0 dB  |
| Peaking | 2059 Hz | 4.56 | 0.8 dB   |
| Peaking | 4058 Hz | 5.2  | 6.6 dB   |
| Peaking | 4466 Hz | 3.24 | -5.7 dB  |
| Peaking | 6652 Hz | 9.33 | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20by%20Ludacris%20SL100/Soul%20by%20Ludacris%20SL100.png)