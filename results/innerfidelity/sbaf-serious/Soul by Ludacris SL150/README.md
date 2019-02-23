# Soul by Ludacris SL150
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.0; 25 -1.2; 28 -1.4; 31 -1.9; 34 -2.4; 37 -2.6; 41 -2.8; 45 -3.1; 49 -3.6; 54 -4.2; 60 -4.6; 66 -5.3; 72 -6.0; 79 -6.7; 87 -7.5; 96 -8.2; 106 -8.7; 116 -9.3; 128 -9.9; 141 -10.3; 155 -10.5; 170 -10.4; 187 -9.9; 206 -9.6; 227 -10.3; 249 -10.8; 274 -11.0; 302 -11.5; 332 -11.3; 365 -10.7; 402 -10.2; 442 -9.6; 486 -8.9; 535 -7.6; 588 -5.9; 647 -4.6; 712 -3.7; 783 -2.9; 861 -2.6; 947 -2.9; 1042 -3.4; 1146 -3.9; 1261 -4.3; 1387 -4.4; 1526 -4.6; 1678 -4.9; 1846 -5.0; 2031 -4.9; 2234 -5.0; 2457 -5.1; 2703 -5.4; 2973 -5.5; 3270 -5.4; 3597 -4.2; 3957 -2.2; 4353 -0.8; 4788 -6.6; 5267 -7.7; 5793 -6.2; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul by Ludacris SL150 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul by Ludacris SL150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.3  | 5.6 dB  |
| Peaking | 126 Hz   | 1.03 | -3.4 dB |
| Peaking | 406 Hz   | 0.68 | -9.3 dB |
| Peaking | 689 Hz   | 0.65 | 7.8 dB  |
| Peaking | 21249 Hz | 2.15 | 2.0 dB  |
| Peaking | 392 Hz   | 9.22 | 0.5 dB  |
| Peaking | 2635 Hz  | 0.45 | -0.4 dB |
| Peaking | 4276 Hz  | 3.86 | 7.0 dB  |
| Peaking | 5394 Hz  | 2.45 | -6.0 dB |
| Peaking | 6340 Hz  | 4.82 | 8.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20by%20Ludacris%20SL150/Soul%20by%20Ludacris%20SL150.png)