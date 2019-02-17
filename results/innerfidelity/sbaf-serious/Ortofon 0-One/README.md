# Ortofon 0-One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.1; 49 -1.4; 54 -1.4; 60 -0.7; 66 -1.1; 72 -2.5; 79 -3.5; 87 -4.1; 96 -4.3; 106 -4.2; 116 -4.3; 128 -4.5; 141 -4.3; 155 -3.8; 170 -3.6; 187 -3.0; 206 -2.3; 227 -1.4; 249 -0.5; 274 -0.5; 302 -0.5; 332 -2.1; 365 -4.6; 402 -6.4; 442 -7.1; 486 -7.5; 535 -7.3; 588 -6.8; 647 -4.7; 712 -3.8; 783 -5.3; 861 -6.0; 947 -6.4; 1042 -6.6; 1146 -4.8; 1261 -5.0; 1387 -5.9; 1526 -7.1; 1678 -6.5; 1846 -3.7; 2031 -0.8; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -3.6; 4353 -1.0; 4788 -2.5; 5267 -4.2; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -8.0; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ortofon 0-One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 0-One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.42 | 6.1 dB  |
| Peaking | 63 Hz   | 5.23 | 2.3 dB  |
| Peaking | 259 Hz  | 2.09 | 6.2 dB  |
| Peaking | 2899 Hz | 1.27 | 6.7 dB  |
| Peaking | 6156 Hz | 5.11 | 5.2 dB  |
| Peaking | 488 Hz  | 3.2  | -2.4 dB |
| Peaking | 691 Hz  | 7.42 | 3.0 dB  |
| Peaking | 1612 Hz | 5.09 | -3.0 dB |
| Peaking | 2070 Hz | 5.98 | 2.7 dB  |
| Peaking | 8834 Hz | 4.04 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | 6.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ortofon%200-One/Ortofon%200-One.png)