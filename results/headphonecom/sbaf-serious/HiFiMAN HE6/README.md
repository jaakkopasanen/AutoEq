# HiFiMAN HE6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.7; 25 -2.3; 28 -2.9; 31 -3.2; 34 -3.2; 37 -3.1; 41 -2.9; 45 -2.8; 49 -2.8; 54 -2.8; 60 -3.0; 66 -3.0; 72 -3.1; 79 -3.5; 87 -3.6; 96 -3.8; 106 -3.8; 116 -3.9; 128 -4.2; 141 -4.4; 155 -4.6; 170 -4.4; 187 -4.5; 206 -4.5; 227 -4.5; 249 -4.5; 274 -4.5; 302 -4.1; 332 -4.2; 365 -4.0; 402 -4.1; 442 -4.1; 486 -4.1; 535 -4.2; 588 -4.2; 647 -4.0; 712 -3.7; 783 -4.0; 861 -4.6; 947 -4.4; 1042 -4.5; 1146 -3.4; 1261 -3.7; 1387 -3.4; 1526 -3.9; 1678 -3.0; 1846 -1.2; 2031 -1.2; 2234 -2.8; 2457 -1.9; 2703 -2.5; 2973 -4.7; 3270 -4.6; 3597 -5.0; 3957 -5.0; 4353 -7.8; 4788 -5.9; 5267 -0.5; 5793 -5.1; 6373 -9.0; 7010 -9.1; 7711 -8.0; 8482 -8.8; 9330 -8.7; 10263 -4.9; 11289 -4.5; 12418 -5.7; 13660 -9.8; 15026 -10.4; 16529 -7.2; 18182 -4.4; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 2038 Hz  |  1.83 | 3.1 dB  |
| Peaking | 4371 Hz  | 10.2  | -3.3 dB |
| Peaking | 7692 Hz  |  2.33 | -4.7 dB |
| Peaking | 14711 Hz |  2.38 | -6.7 dB |
| Peaking | 17 Hz    |  1.94 | 4.5 dB  |
| Peaking | 54 Hz    |  1.02 | 1.5 dB  |
| Peaking | 4828 Hz  |  4.11 | -1.6 dB |
| Peaking | 5469 Hz  |  7.62 | 9.4 dB  |
| Peaking | 6114 Hz  |  5.73 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE6/HiFiMAN%20HE6.png)