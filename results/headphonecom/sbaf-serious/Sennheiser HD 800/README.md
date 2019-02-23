# Sennheiser HD 800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.6; 31 -2.0; 34 -2.2; 37 -2.4; 41 -2.5; 45 -2.4; 49 -2.3; 54 -2.6; 60 -3.2; 66 -3.3; 72 -4.1; 79 -4.9; 87 -5.4; 96 -5.7; 106 -6.0; 116 -6.3; 128 -6.5; 141 -6.9; 155 -7.0; 170 -7.0; 187 -7.2; 206 -7.3; 227 -7.3; 249 -7.2; 274 -7.1; 302 -6.9; 332 -6.6; 365 -6.5; 402 -6.3; 442 -6.1; 486 -5.9; 535 -5.6; 588 -5.4; 647 -5.1; 712 -4.8; 783 -4.6; 861 -4.5; 947 -3.9; 1042 -3.6; 1146 -2.7; 1261 -2.4; 1387 -2.3; 1526 -2.7; 1678 -2.5; 1846 -2.3; 2031 -2.2; 2234 -2.5; 2457 -1.4; 2703 -1.3; 2973 -2.3; 3270 -2.3; 3597 -2.8; 3957 -5.5; 4353 -6.0; 4788 -5.9; 5267 -7.3; 5793 -10.8; 6373 -11.2; 7010 -6.3; 7711 -5.2; 8482 -6.7; 9330 -9.4; 10263 -6.5; 11289 -5.3; 12418 -5.3; 13660 -6.6; 15026 -8.1; 16529 -6.8; 18182 -5.9; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.87 | 4.5 dB  |
| Peaking | 1219 Hz  | 1.69 | 3.0 dB  |
| Peaking | 2549 Hz  | 1.23 | 4.7 dB  |
| Peaking | 6057 Hz  | 6.31 | -6.8 dB |
| Peaking | 10439 Hz | 0.16 | -1.2 dB |
| Peaking | 219 Hz   | 0.69 | -2.1 dB |
| Peaking | 7873 Hz  | 2.92 | 5.7 dB  |
| Peaking | 9204 Hz  | 1.47 | -7.7 dB |
| Peaking | 11057 Hz | 1.66 | 5.3 dB  |
| Peaking | 14864 Hz | 3.45 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)