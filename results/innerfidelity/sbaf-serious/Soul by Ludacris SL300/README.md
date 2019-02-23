# Soul by Ludacris SL300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -1.9; 37 -4.7; 41 -8.9; 45 -11.3; 49 -11.9; 54 -11.6; 60 -11.1; 66 -10.1; 72 -9.3; 79 -8.8; 87 -8.6; 96 -8.5; 106 -8.3; 116 -8.2; 128 -8.3; 141 -8.4; 155 -8.4; 170 -8.4; 187 -8.3; 206 -8.2; 227 -8.1; 249 -8.0; 274 -7.7; 302 -7.7; 332 -7.7; 365 -7.9; 402 -8.3; 442 -8.7; 486 -9.8; 535 -10.6; 588 -9.1; 647 -5.8; 712 -0.7; 783 -0.5; 861 -1.2; 947 -5.5; 1042 -6.9; 1146 -8.9; 1261 -9.3; 1387 -8.6; 1526 -8.4; 1678 -7.7; 1846 -7.2; 2031 -7.0; 2234 -7.1; 2457 -5.2; 2703 -2.9; 2973 -0.5; 3270 -0.5; 3597 -3.3; 3957 -2.7; 4353 -9.9; 4788 -11.2; 5267 -8.3; 5793 -5.5; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -8.8; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul by Ludacris SL300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul by Ludacris SL300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.86 | 13.7 dB  |
| Peaking | 46 Hz   | 1.06 | -13.8 dB |
| Peaking | 787 Hz  | 3.4  | 10.7 dB  |
| Peaking | 973 Hz  | 0.27 | -3.5 dB  |
| Peaking | 3073 Hz | 2.66 | 8.8 dB   |
| Peaking | 534 Hz  | 5.82 | -3.2 dB  |
| Peaking | 2062 Hz | 0.11 | 0.5 dB   |
| Peaking | 4698 Hz | 6.54 | -6.5 dB  |
| Peaking | 6561 Hz | 5.77 | 5.4 dB   |
| Peaking | 9258 Hz | 3.87 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20by%20Ludacris%20SL300/Soul%20by%20Ludacris%20SL300.png)