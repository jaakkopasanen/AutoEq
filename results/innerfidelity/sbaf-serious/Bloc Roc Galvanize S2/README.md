# Bloc Roc Galvanize S2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.7; 25 -3.6; 28 -4.9; 31 -6.0; 34 -7.0; 37 -7.9; 41 -8.9; 45 -9.7; 49 -10.3; 54 -10.9; 60 -11.4; 66 -11.5; 72 -11.7; 79 -11.6; 87 -11.2; 96 -11.0; 106 -11.3; 116 -11.3; 128 -11.3; 141 -11.2; 155 -11.0; 170 -10.5; 187 -10.4; 206 -10.1; 227 -9.4; 249 -8.8; 274 -8.1; 302 -8.3; 332 -8.2; 365 -7.6; 402 -7.1; 442 -6.7; 486 -6.5; 535 -5.7; 588 -4.4; 647 -3.3; 712 -2.8; 783 -2.8; 861 -3.1; 947 -3.7; 1042 -4.2; 1146 -5.0; 1261 -5.5; 1387 -6.8; 1526 -8.2; 1678 -9.0; 1846 -8.5; 2031 -8.1; 2234 -7.2; 2457 -5.7; 2703 -4.0; 2973 -2.6; 3270 -3.0; 3597 -0.8; 3957 -0.5; 4353 -1.3; 4788 -6.0; 5267 -5.9; 5793 -4.7; 6373 -4.5; 7010 -3.9; 7711 -3.7; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.0; 18182 -4.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bloc Roc Galvanize S2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bloc Roc Galvanize S2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.96 | 5.1 dB  |
| Peaking | 63 Hz   | 0.49 | -7.4 dB |
| Peaking | 198 Hz  | 0.79 | -3.9 dB |
| Peaking | 1788 Hz | 2.47 | -5.4 dB |
| Peaking | 3776 Hz | 4.68 | 4.5 dB  |
| Peaking | 482 Hz  | 1.75 | -2.0 dB |
| Peaking | 704 Hz  | 1.56 | 2.9 dB  |
| Peaking | 1419 Hz | 4.17 | -1.1 dB |
| Peaking | 4270 Hz | 8.38 | 2.8 dB  |
| Peaking | 4882 Hz | 4.06 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -7.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bloc%20Roc%20Galvanize%20S2/Bloc%20Roc%20Galvanize%20S2.png)