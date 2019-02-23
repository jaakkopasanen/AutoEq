# Sennheiser HD 218
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.1; 28 -1.8; 31 -2.5; 34 -3.0; 37 -3.6; 41 -4.2; 45 -4.8; 49 -5.4; 54 -6.0; 60 -6.7; 66 -7.4; 72 -8.1; 79 -8.8; 87 -9.4; 96 -10.1; 106 -10.1; 116 -9.6; 128 -10.3; 141 -11.7; 155 -12.7; 170 -12.6; 187 -12.8; 206 -12.3; 227 -11.6; 249 -10.6; 274 -9.6; 302 -9.4; 332 -9.8; 365 -8.8; 402 -8.1; 442 -6.8; 486 -6.7; 535 -6.8; 588 -5.6; 647 -5.2; 712 -5.4; 783 -5.5; 861 -5.9; 947 -6.2; 1042 -6.3; 1146 -6.2; 1261 -6.0; 1387 -5.6; 1526 -5.3; 1678 -5.8; 1846 -6.0; 2031 -5.1; 2234 -4.3; 2457 -3.4; 2703 -2.8; 2973 -2.3; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -2.4; 4788 -7.8; 5267 -5.4; 5793 -5.9; 6373 -4.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.7; 18182 -8.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 218 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 218 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 22 Hz    |  0.78 | 6.1 dB  |
| Peaking | 89 Hz    |  1.79 | -2.4 dB |
| Peaking | 183 Hz   |  1.22 | -6.4 dB |
| Peaking | 3400 Hz  |  1.67 | 5.9 dB  |
| Peaking | 22049 Hz |  2.27 | 0.6 dB  |
| Peaking | 341 Hz   |  5.51 | -1.5 dB |
| Peaking | 667 Hz   |  2.18 | 1.6 dB  |
| Peaking | 4838 Hz  | 12.59 | -4.0 dB |
| Peaking | 6692 Hz  |  9.99 | 2.9 dB  |
| Peaking | 18253 Hz |  2.29 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20218/Sennheiser%20HD%20218.png)