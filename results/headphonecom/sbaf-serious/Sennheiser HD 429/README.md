# Sennheiser HD 429
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.0; 25 -8.1; 28 -8.2; 31 -8.4; 34 -8.5; 37 -8.5; 41 -8.5; 45 -8.6; 49 -8.5; 54 -8.5; 60 -8.4; 66 -8.4; 72 -8.2; 79 -7.7; 87 -6.9; 96 -5.3; 106 -6.5; 116 -8.0; 128 -8.6; 141 -8.9; 155 -8.3; 170 -8.6; 187 -8.7; 206 -8.7; 227 -8.6; 249 -8.1; 274 -7.0; 302 -6.2; 332 -5.8; 365 -5.7; 402 -6.1; 442 -6.3; 486 -6.7; 535 -7.0; 588 -7.1; 647 -7.1; 712 -7.4; 783 -7.2; 861 -6.9; 947 -6.6; 1042 -6.7; 1146 -7.3; 1261 -7.3; 1387 -7.2; 1526 -7.8; 1678 -7.6; 1846 -6.6; 2031 -5.6; 2234 -3.9; 2457 -2.5; 2703 -2.5; 2973 -1.8; 3270 -1.3; 3597 -1.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 429 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 429 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 1.17 | -2.0 dB |
| Peaking | 60 Hz   | 2.93 | -1.4 dB |
| Peaking | 176 Hz  | 1.72 | -2.4 dB |
| Peaking | 1525 Hz | 1.88 | -2.5 dB |
| Peaking | 4100 Hz | 0.92 | 6.6 dB  |
| Peaking | 14 Hz   | 1.63 | -0.7 dB |
| Peaking | 347 Hz  | 5.02 | 1.4 dB  |
| Peaking | 2463 Hz | 5.62 | 1.5 dB  |
| Peaking | 6185 Hz | 2.44 | 6.4 dB  |
| Peaking | 6830 Hz | 1.2  | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20429/Sennheiser%20HD%20429.png)