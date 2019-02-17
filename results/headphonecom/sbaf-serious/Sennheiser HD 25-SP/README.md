# Sennheiser HD 25-SP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.7; 25 -5.4; 28 -6.2; 31 -6.9; 34 -7.3; 37 -7.4; 41 -7.9; 45 -9.1; 49 -9.8; 54 -10.2; 60 -10.5; 66 -10.7; 72 -11.0; 79 -10.7; 87 -10.4; 96 -12.1; 106 -13.4; 116 -13.5; 128 -13.2; 141 -12.5; 155 -11.5; 170 -12.0; 187 -12.9; 206 -12.9; 227 -12.4; 249 -11.3; 274 -10.4; 302 -9.3; 332 -7.6; 365 -6.4; 402 -5.5; 442 -5.3; 486 -5.2; 535 -5.1; 588 -5.1; 647 -5.2; 712 -5.4; 783 -5.6; 861 -5.9; 947 -6.2; 1042 -6.7; 1146 -7.1; 1261 -7.9; 1387 -8.9; 1526 -9.8; 1678 -10.8; 1846 -11.2; 2031 -11.1; 2234 -10.5; 2457 -10.0; 2703 -9.0; 2973 -6.8; 3270 -5.7; 3597 -5.0; 3957 -6.1; 4353 -5.6; 4788 -5.6; 5267 -2.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -12.6; 9330 -15.5; 10263 -10.8; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-SP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-SP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 108 Hz  | 0.96 | -6.4 dB  |
| Peaking | 213 Hz  | 2.7  | -4.7 dB  |
| Peaking | 1945 Hz | 2.1  | -5.4 dB  |
| Peaking | 6116 Hz | 2.55 | 7.1 dB   |
| Peaking | 9152 Hz | 4.18 | -11.1 dB |
| Peaking | 15 Hz   | 0.86 | 4.3 dB   |
| Peaking | 58 Hz   | 0.61 | -2.0 dB  |
| Peaking | 87 Hz   | 3.68 | 3.0 dB   |
| Peaking | 538 Hz  | 1.51 | 2.3 dB   |
| Peaking | 3464 Hz | 7.65 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%2025-SP/Sennheiser%20HD%2025-SP.png)