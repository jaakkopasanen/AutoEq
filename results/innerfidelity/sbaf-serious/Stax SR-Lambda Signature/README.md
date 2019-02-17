# Stax SR-Lambda Signature
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.9; 34 -2.3; 37 -4.1; 41 -6.1; 45 -7.5; 49 -8.2; 54 -8.1; 60 -7.7; 66 -6.8; 72 -6.1; 79 -6.0; 87 -5.9; 96 -5.8; 106 -5.6; 116 -5.4; 128 -5.4; 141 -5.3; 155 -5.3; 170 -5.3; 187 -5.2; 206 -5.2; 227 -5.1; 249 -5.1; 274 -5.0; 302 -5.0; 332 -5.0; 365 -5.1; 402 -5.0; 442 -4.7; 486 -4.7; 535 -4.9; 588 -4.8; 647 -5.0; 712 -5.3; 783 -5.3; 861 -5.7; 947 -6.1; 1042 -6.7; 1146 -7.1; 1261 -8.1; 1387 -9.4; 1526 -10.3; 1678 -10.7; 1846 -10.8; 2031 -8.6; 2234 -5.5; 2457 -2.5; 2703 -3.9; 2973 -5.1; 3270 -5.7; 3597 -5.9; 3957 -6.5; 4353 -7.1; 4788 -6.2; 5267 -4.6; 5793 -3.8; 6373 -6.2; 7010 -7.3; 7711 -6.5; 8482 -9.0; 9330 -9.8; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.3; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-Lambda Signature GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Lambda Signature ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.89 | 7.0 dB  |
| Peaking | 1743 Hz | 2.71 | -5.5 dB |
| Peaking | 2492 Hz | 4.04 | 5.2 dB  |
| Peaking | 5623 Hz | 6.81 | 3.2 dB  |
| Peaking | 9015 Hz | 5.52 | -4.0 dB |
| Peaking | 52 Hz   | 2.02 | -3.8 dB |
| Peaking | 87 Hz   | 0.17 | 1.2 dB  |
| Peaking | 562 Hz  | 0.89 | 1.2 dB  |
| Peaking | 1344 Hz | 4.32 | -1.4 dB |
| Peaking | 4222 Hz | 5.36 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Lambda%20Signature/Stax%20SR-Lambda%20Signature.png)