# Sennheiser HD 25-SP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.5; 25 -4.1; 28 -5.0; 31 -5.6; 34 -6.0; 37 -6.1; 41 -6.7; 45 -7.8; 49 -8.5; 54 -8.9; 60 -9.2; 66 -9.4; 72 -9.8; 79 -9.5; 87 -9.2; 96 -10.8; 106 -12.1; 116 -12.2; 128 -12.0; 141 -11.2; 155 -10.3; 170 -10.7; 187 -11.7; 206 -11.7; 227 -11.1; 249 -10.0; 274 -9.2; 302 -8.0; 332 -6.4; 365 -5.2; 402 -4.2; 442 -4.0; 486 -3.9; 535 -3.8; 588 -3.8; 647 -3.9; 712 -4.1; 783 -4.3; 861 -4.6; 947 -5.0; 1042 -5.4; 1146 -5.8; 1261 -6.6; 1387 -7.6; 1526 -8.5; 1678 -9.5; 1846 -9.9; 2031 -9.8; 2234 -9.2; 2457 -8.7; 2703 -7.8; 2973 -5.6; 3270 -4.4; 3597 -3.8; 3957 -4.8; 4353 -4.3; 4788 -4.4; 5267 -2.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -11.3; 9330 -14.2; 10263 -9.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-SP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-SP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 2.4  | 3.7 dB  |
| Peaking | 111 Hz  | 1.3  | -5.5 dB |
| Peaking | 209 Hz  | 3.31 | -4.4 dB |
| Peaking | 5997 Hz | 2.41 | 6.7 dB  |
| Peaking | 9138 Hz | 4.47 | -9.7 dB |
| Peaking | 56 Hz   | 3.03 | -1.7 dB |
| Peaking | 268 Hz  | 2.2  | -2.7 dB |
| Peaking | 552 Hz  | 0.63 | 3.5 dB  |
| Peaking | 1948 Hz | 1.34 | -4.5 dB |
| Peaking | 3402 Hz | 3.35 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%2025-SP/Sennheiser%20HD%2025-SP.png)