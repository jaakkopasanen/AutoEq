# Soul by Ludacris SL150
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.2; 25 -3.4; 28 -3.6; 31 -4.1; 34 -4.6; 37 -4.8; 41 -5.0; 45 -5.2; 49 -5.8; 54 -6.4; 60 -6.8; 66 -7.5; 72 -8.2; 79 -8.9; 87 -9.7; 96 -10.4; 106 -10.9; 116 -11.5; 128 -12.1; 141 -12.5; 155 -12.7; 170 -12.6; 187 -12.1; 206 -11.8; 227 -12.5; 249 -13.0; 274 -13.2; 302 -13.7; 332 -13.5; 365 -12.9; 402 -12.4; 442 -11.7; 486 -11.1; 535 -9.8; 588 -8.1; 647 -6.8; 712 -5.9; 783 -5.1; 861 -4.8; 947 -5.1; 1042 -5.6; 1146 -6.1; 1261 -6.5; 1387 -6.6; 1526 -6.8; 1678 -7.1; 1846 -7.2; 2031 -7.1; 2234 -7.2; 2457 -7.3; 2703 -7.6; 2973 -7.7; 3270 -7.6; 3597 -6.4; 3957 -4.4; 4353 -3.0; 4788 -8.8; 5267 -9.9; 5793 -8.4; 6373 -0.5; 7010 -2.8; 7711 -5.1; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul by Ludacris SL150 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul by Ludacris SL150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.5  | 2.8 dB   |
| Peaking | 140 Hz  | 0.72 | -6.6 dB  |
| Peaking | 346 Hz  | 1.41 | -6.4 dB  |
| Peaking | 3620 Hz | 0.56 | -1.8 dB  |
| Peaking | 6605 Hz | 8.53 | 6.7 dB   |
| Peaking | 499 Hz  | 5.17 | -1.7 dB  |
| Peaking | 819 Hz  | 2.59 | 2.1 dB   |
| Peaking | 4308 Hz | 3.3  | 9.5 dB   |
| Peaking | 5196 Hz | 1.59 | -13.2 dB |
| Peaking | 6120 Hz | 1.41 | 7.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -6.9 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20by%20Ludacris%20SL150/Soul%20by%20Ludacris%20SL150.png)