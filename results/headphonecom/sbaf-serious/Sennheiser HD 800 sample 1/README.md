# Sennheiser HD 800 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.7; 31 -2.1; 34 -2.3; 37 -2.5; 41 -2.5; 45 -2.1; 49 -2.1; 54 -2.9; 60 -3.3; 66 -4.0; 72 -4.8; 79 -5.3; 87 -5.8; 96 -6.0; 106 -6.3; 116 -6.6; 128 -6.9; 141 -7.3; 155 -7.4; 170 -7.4; 187 -7.7; 206 -7.7; 227 -7.7; 249 -7.7; 274 -7.5; 302 -7.3; 332 -7.1; 365 -6.9; 402 -6.8; 442 -6.7; 486 -6.4; 535 -6.2; 588 -6.0; 647 -5.7; 712 -5.6; 783 -5.4; 861 -5.3; 947 -5.0; 1042 -4.8; 1146 -4.0; 1261 -3.4; 1387 -2.9; 1526 -3.3; 1678 -3.5; 1846 -3.0; 2031 -3.1; 2234 -2.7; 2457 -1.7; 2703 -1.8; 2973 -2.0; 3270 -2.5; 3597 -3.1; 3957 -5.5; 4353 -6.3; 4788 -5.9; 5267 -7.5; 5793 -12.5; 6373 -10.3; 7010 -5.3; 7711 -4.6; 8482 -4.9; 9330 -6.8; 10263 -5.1; 11289 -4.9; 12418 -5.1; 13660 -9.6; 15026 -9.9; 16529 -7.3; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.21 | 4.3 dB  |
| Peaking | 162 Hz   | 0.41 | -3.7 dB |
| Peaking | 2390 Hz  | 1.02 | 3.0 dB  |
| Peaking | 5925 Hz  | 5.39 | -9.2 dB |
| Peaking | 14736 Hz | 2.41 | -5.9 dB |
| Peaking | 3511 Hz  | 3.13 | 1.6 dB  |
| Peaking | 4087 Hz  | 4.25 | -2.7 dB |
| Peaking | 7315 Hz  | 7.24 | 1.7 dB  |
| Peaking | 16285 Hz | 5.74 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%20sample%201/Sennheiser%20HD%20800%20sample%201.png)