# Sennheiser HD 280 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.3; 28 -7.5; 31 -7.7; 34 -7.8; 37 -7.8; 41 -7.8; 45 -7.6; 49 -7.3; 54 -6.6; 60 -5.3; 66 -3.0; 72 -0.5; 79 -0.7; 87 -4.5; 96 -6.1; 106 -1.5; 116 -0.7; 128 -2.8; 141 -3.6; 155 -2.9; 170 -3.5; 187 -5.4; 206 -6.4; 227 -6.9; 249 -7.3; 274 -7.5; 302 -7.4; 332 -7.4; 365 -7.2; 402 -7.4; 442 -7.1; 486 -6.9; 535 -7.0; 588 -7.3; 647 -7.2; 712 -7.1; 783 -7.1; 861 -7.0; 947 -6.9; 1042 -7.2; 1146 -7.3; 1261 -7.1; 1387 -6.9; 1526 -6.4; 1678 -7.2; 1846 -7.9; 2031 -8.2; 2234 -8.7; 2457 -8.9; 2703 -7.1; 2973 -4.0; 3270 -4.1; 3597 -5.6; 3957 -6.0; 4353 -5.4; 4788 -5.3; 5267 -3.7; 5793 -4.2; 6373 -6.0; 7010 -6.6; 7711 -8.2; 8482 -10.7; 9330 -12.7; 10263 -11.9; 11289 -8.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 74 Hz   | 5.77 | 6.2 dB  |
| Peaking | 119 Hz  | 2.89 | 5.2 dB  |
| Peaking | 2177 Hz | 2.32 | -3.2 dB |
| Peaking | 7382 Hz | 0.51 | 3.7 dB  |
| Peaking | 9376 Hz | 1.83 | -9.9 dB |
| Peaking | 37 Hz   | 1.85 | -1.7 dB |
| Peaking | 163 Hz  | 6.55 | 3.6 dB  |
| Peaking | 332 Hz  | 0.49 | -1.1 dB |
| Peaking | 3101 Hz | 5.51 | 4.8 dB  |
| Peaking | 3257 Hz | 2.24 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)