# Sennheiser HD 205 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.1; 25 -7.2; 28 -7.2; 31 -7.2; 34 -7.4; 37 -7.7; 41 -7.9; 45 -8.1; 49 -8.2; 54 -8.4; 60 -8.1; 66 -7.8; 72 -8.6; 79 -9.5; 87 -9.9; 96 -10.3; 106 -10.3; 116 -10.4; 128 -10.1; 141 -9.2; 155 -9.4; 170 -9.3; 187 -9.5; 206 -9.1; 227 -9.3; 249 -8.8; 274 -8.7; 302 -8.1; 332 -6.9; 365 -5.5; 402 -4.2; 442 -4.0; 486 -5.1; 535 -6.3; 588 -6.4; 647 -4.7; 712 -2.2; 783 -2.5; 861 -4.4; 947 -5.9; 1042 -6.9; 1146 -7.7; 1261 -8.1; 1387 -8.5; 1526 -9.0; 1678 -8.9; 1846 -8.3; 2031 -7.7; 2234 -6.6; 2457 -5.0; 2703 -2.9; 2973 -2.3; 3270 -1.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.6; 5267 -3.6; 5793 -1.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 205 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 205 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 106 Hz  | 0.81 | -3.6 dB |
| Peaking | 281 Hz  | 1.28 | -4.1 dB |
| Peaking | 393 Hz  | 1.08 | 4.3 dB  |
| Peaking | 3861 Hz | 2.18 | 6.7 dB  |
| Peaking | 6178 Hz | 5.09 | 5.1 dB  |
| Peaking | 581 Hz  | 4.65 | -2.8 dB |
| Peaking | 745 Hz  | 3.13 | 4.7 dB  |
| Peaking | 1568 Hz | 1.22 | -3.2 dB |
| Peaking | 2778 Hz | 3.84 | 2.8 dB  |
| Peaking | 8651 Hz | 5.55 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20205%20II/Sennheiser%20HD%20205%20II.png)