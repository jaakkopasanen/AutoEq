# Sennheiser HD 429
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.9; 25 -10.0; 28 -10.2; 31 -10.3; 34 -10.4; 37 -10.4; 41 -10.5; 45 -10.5; 49 -10.5; 54 -10.4; 60 -10.4; 66 -10.3; 72 -10.1; 79 -9.7; 87 -8.9; 96 -7.3; 106 -8.5; 116 -10.0; 128 -10.6; 141 -10.8; 155 -10.2; 170 -10.6; 187 -10.7; 206 -10.6; 227 -10.6; 249 -10.0; 274 -8.9; 302 -8.1; 332 -7.8; 365 -7.6; 402 -8.0; 442 -8.2; 486 -8.6; 535 -9.0; 588 -9.1; 647 -9.0; 712 -9.3; 783 -9.2; 861 -8.8; 947 -8.6; 1042 -8.7; 1146 -9.2; 1261 -9.3; 1387 -9.2; 1526 -9.7; 1678 -9.5; 1846 -8.6; 2031 -7.6; 2234 -5.8; 2457 -4.4; 2703 -4.4; 2973 -3.7; 3270 -3.3; 3597 -3.4; 3957 -1.2; 4353 -0.5; 4788 -1.2; 5267 -2.3; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 429 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 429 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.99 | -2.9 dB |
| Peaking | 37 Hz   | 0.84 | -1.9 dB |
| Peaking | 551 Hz  | 0.05 | -2.9 dB |
| Peaking | 4149 Hz | 1.09 | 7.7 dB  |
| Peaking | 6261 Hz | 4.56 | 4.1 dB  |
| Peaking | 98 Hz   | 5.66 | 3.3 dB  |
| Peaking | 210 Hz  | 0.72 | -2.2 dB |
| Peaking | 339 Hz  | 1.55 | 3.1 dB  |
| Peaking | 1643 Hz | 3.07 | -1.8 dB |
| Peaking | 2440 Hz | 4.55 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20429/Sennheiser%20HD%20429.png)