# Sennheiser HD 428
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.0; 96 -2.8; 106 -4.1; 116 -5.0; 128 -5.5; 141 -5.7; 155 -5.9; 170 -5.5; 187 -5.2; 206 -5.0; 227 -4.4; 249 -4.4; 274 -4.9; 302 -4.6; 332 -4.9; 365 -4.9; 402 -4.7; 442 -4.8; 486 -4.6; 535 -4.4; 588 -4.2; 647 -4.6; 712 -5.4; 783 -6.1; 861 -6.4; 947 -6.6; 1042 -6.1; 1146 -4.5; 1261 -6.6; 1387 -7.2; 1526 -7.7; 1678 -8.4; 1846 -8.4; 2031 -7.6; 2234 -5.4; 2457 -3.9; 2703 -3.8; 2973 -3.5; 3270 -3.3; 3597 -3.9; 3957 -3.0; 4353 -0.5; 4788 -0.5; 5267 -2.8; 5793 -2.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 428 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 428 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.5  | 6.8 dB  |
| Peaking | 461 Hz   | 1.28 | 1.9 dB  |
| Peaking | 2867 Hz  | 4.13 | 2.0 dB  |
| Peaking | 4891 Hz  | 1.71 | 5.9 dB  |
| Peaking | 22050 Hz | 2.38 | 2.8 dB  |
| Peaking | 19 Hz    | 2.46 | 1.3 dB  |
| Peaking | 82 Hz    | 3.98 | 2.2 dB  |
| Peaking | 130 Hz   | 2.24 | -1.9 dB |
| Peaking | 759 Hz   | 0.15 | 0.3 dB  |
| Peaking | 1737 Hz  | 3.42 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20428/Sennheiser%20HD%20428.png)