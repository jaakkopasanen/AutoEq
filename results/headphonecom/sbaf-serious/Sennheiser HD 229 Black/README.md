# Sennheiser HD 229 Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -4.2; 25 -4.9; 28 -5.8; 31 -6.5; 34 -7.2; 37 -7.8; 41 -8.5; 45 -9.0; 49 -9.4; 54 -10.0; 60 -10.5; 66 -10.8; 72 -11.0; 79 -11.2; 87 -11.2; 96 -11.4; 106 -11.2; 116 -10.8; 128 -10.2; 141 -9.8; 155 -11.1; 170 -10.0; 187 -9.7; 206 -8.4; 227 -9.0; 249 -8.2; 274 -7.0; 302 -5.7; 332 -4.7; 365 -3.9; 402 -3.8; 442 -4.0; 486 -4.0; 535 -4.2; 588 -4.1; 647 -4.1; 712 -4.6; 783 -5.0; 861 -5.3; 947 -5.6; 1042 -5.7; 1146 -5.7; 1261 -5.5; 1387 -5.3; 1526 -4.8; 1678 -7.0; 1846 -6.8; 2031 -6.1; 2234 -5.4; 2457 -5.2; 2703 -5.2; 2973 -5.0; 3270 -4.9; 3597 -5.1; 3957 -6.6; 4353 -7.8; 4788 -7.5; 5267 -4.6; 5793 -1.9; 6373 -0.5; 7010 -3.2; 7711 -5.7; 8482 -9.8; 9330 -12.0; 10263 -6.5; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 229 Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 229 Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.97 | -5.8 dB |
| Peaking | 167 Hz  | 2.37 | -3.3 dB |
| Peaking | 6348 Hz | 4.82 | 6.2 dB  |
| Peaking | 9085 Hz | 5.04 | -7.2 dB |
| Peaking | 20 Hz   | 2.95 | 2.8 dB  |
| Peaking | 243 Hz  | 4.01 | -2.0 dB |
| Peaking | 387 Hz  | 1.88 | 2.3 dB  |
| Peaking | 623 Hz  | 2.54 | 1.4 dB  |
| Peaking | 4508 Hz | 6.97 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20229%20Black/Sennheiser%20HD%20229%20Black.png)