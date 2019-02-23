# Stax SR-007
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.2; 25 -1.2; 28 -1.0; 31 -0.9; 34 -0.6; 37 -0.5; 41 -0.5; 45 -1.0; 49 -2.8; 54 -5.7; 60 -5.6; 66 -4.9; 72 -4.7; 79 -4.7; 87 -4.9; 96 -5.1; 106 -5.3; 116 -5.3; 128 -5.6; 141 -5.8; 155 -6.0; 170 -6.2; 187 -6.3; 206 -6.5; 227 -6.5; 249 -6.7; 274 -6.8; 302 -7.0; 332 -7.0; 365 -7.2; 402 -7.2; 442 -7.0; 486 -6.4; 535 -6.0; 588 -6.9; 647 -7.9; 712 -8.2; 783 -7.8; 861 -8.0; 947 -8.3; 1042 -8.0; 1146 -6.5; 1261 -4.5; 1387 -8.5; 1526 -9.4; 1678 -8.8; 1846 -6.6; 2031 -4.7; 2234 -3.5; 2457 -2.2; 2703 -0.9; 2973 -1.2; 3270 -2.4; 3597 -3.2; 3957 -3.9; 4353 -5.1; 4788 -6.5; 5267 -5.1; 5793 -3.2; 6373 -1.9; 7010 -3.4; 7711 -5.8; 8482 -9.3; 9330 -9.8; 10263 -6.4; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -6.2; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-007 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 1.04 | 5.8 dB  |
| Peaking | 1628 Hz | 0.34 | -2.7 dB |
| Peaking | 2804 Hz | 1.77 | 7.5 dB  |
| Peaking | 6530 Hz | 3.69 | 5.0 dB  |
| Peaking | 8903 Hz | 4.67 | -4.9 dB |
| Peaking | 46 Hz   | 2.99 | 2.1 dB  |
| Peaking | 54 Hz   | 5.18 | -3.5 dB |
| Peaking | 1258 Hz | 7.26 | 4.2 dB  |
| Peaking | 1441 Hz | 5.53 | -2.3 dB |
| Peaking | 1627 Hz | 7.82 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-007/Stax%20SR-007.png)