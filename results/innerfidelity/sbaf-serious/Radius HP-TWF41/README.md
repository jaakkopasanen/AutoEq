# Radius HP-TWF41
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.8; 25 -3.2; 28 -3.8; 31 -4.2; 34 -4.6; 37 -4.9; 41 -5.3; 45 -5.7; 49 -6.0; 54 -6.4; 60 -6.9; 66 -7.3; 72 -7.7; 79 -8.2; 87 -8.6; 96 -9.3; 106 -9.6; 116 -9.8; 128 -10.2; 141 -10.5; 155 -10.7; 170 -10.9; 187 -11.1; 206 -11.1; 227 -11.1; 249 -11.2; 274 -11.1; 302 -10.9; 332 -10.8; 365 -10.7; 402 -10.4; 442 -10.0; 486 -9.8; 535 -9.5; 588 -8.8; 647 -8.3; 712 -7.6; 783 -6.9; 861 -6.6; 947 -6.3; 1042 -6.2; 1146 -6.1; 1261 -6.0; 1387 -6.1; 1526 -6.2; 1678 -6.1; 1846 -5.7; 2031 -5.3; 2234 -4.9; 2457 -4.2; 2703 -3.9; 2973 -2.4; 3270 -1.2; 3597 -0.9; 3957 -1.9; 4353 -3.3; 4788 -2.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -8.3; 10263 -7.7; 11289 -7.0; 12418 -6.5; 13660 -6.5; 15026 -7.1; 16529 -9.4; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Radius HP-TWF41 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-TWF41 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.61 | 4.8 dB  |
| Peaking | 213 Hz   | 0.5  | -5.0 dB |
| Peaking | 3370 Hz  | 1.64 | 4.8 dB  |
| Peaking | 5946 Hz  | 2.28 | 6.4 dB  |
| Peaking | 8839 Hz  | 1.29 | -2.4 dB |
| Peaking | 511 Hz   | 1.02 | -2.9 dB |
| Peaking | 778 Hz   | 0.54 | 2.9 dB  |
| Peaking | 1549 Hz  | 0.67 | -1.1 dB |
| Peaking | 13904 Hz | 1.69 | 0.9 dB  |
| Peaking | 16385 Hz | 2.8  | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-TWF41/Radius%20HP-TWF41.png)