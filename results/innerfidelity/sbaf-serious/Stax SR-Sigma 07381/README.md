# Stax SR-Sigma 07381
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.8; 66 -3.4; 72 -4.7; 79 -6.1; 87 -7.4; 96 -8.2; 106 -8.5; 116 -8.3; 128 -8.2; 141 -7.6; 155 -6.8; 170 -7.8; 187 -11.5; 206 -10.3; 227 -10.4; 249 -11.0; 274 -10.6; 302 -10.3; 332 -9.7; 365 -9.1; 402 -8.8; 442 -8.1; 486 -7.7; 535 -7.2; 588 -6.7; 647 -7.5; 712 -8.7; 783 -9.0; 861 -9.7; 947 -9.3; 1042 -9.0; 1146 -8.8; 1261 -7.4; 1387 -6.2; 1526 -4.4; 1678 -3.7; 1846 -2.6; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -1.7; 2973 -3.3; 3270 -2.6; 3597 -2.4; 3957 -3.4; 4353 -2.4; 4788 -1.1; 5267 -3.7; 5793 -7.0; 6373 -6.7; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.9; 13660 -9.3; 15026 -9.1; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-Sigma 07381 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Sigma 07381 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.79 | 7.2 dB  |
| Peaking | 222 Hz   | 0.74 | -4.2 dB |
| Peaking | 1006 Hz  | 1.86 | -3.8 dB |
| Peaking | 2275 Hz  | 1.31 | 6.4 dB  |
| Peaking | 4691 Hz  | 5.28 | 4.6 dB  |
| Peaking | 59 Hz    | 2.07 | 4.2 dB  |
| Peaking | 75 Hz    | 0.8  | -2.8 dB |
| Peaking | 155 Hz   | 5.28 | 3.6 dB  |
| Peaking | 6005 Hz  | 7.66 | -1.8 dB |
| Peaking | 14302 Hz | 3.22 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.2 dB |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Sigma%2007381/Stax%20SR-Sigma%2007381.png)