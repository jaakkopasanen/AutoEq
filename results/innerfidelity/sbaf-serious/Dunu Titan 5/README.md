# Dunu Titan 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.8; 25 -6.8; 28 -6.9; 31 -6.9; 34 -7.0; 37 -7.1; 41 -7.1; 45 -7.1; 49 -7.2; 54 -7.3; 60 -7.4; 66 -7.6; 72 -7.7; 79 -7.9; 87 -8.1; 96 -8.2; 106 -8.2; 116 -8.1; 128 -8.2; 141 -8.0; 155 -7.8; 170 -7.6; 187 -7.3; 206 -7.0; 227 -6.6; 249 -6.2; 274 -5.8; 302 -5.3; 332 -4.8; 365 -4.3; 402 -4.0; 442 -3.6; 486 -2.7; 535 -2.7; 588 -2.2; 647 -1.7; 712 -1.8; 783 -1.5; 861 -1.8; 947 -2.2; 1042 -2.7; 1146 -3.2; 1261 -3.7; 1387 -4.5; 1526 -5.3; 1678 -6.0; 1846 -6.4; 2031 -6.6; 2234 -6.9; 2457 -6.6; 2703 -5.9; 2973 -4.2; 3270 -1.8; 3597 -0.5; 3957 -1.1; 4353 -3.7; 4788 -6.0; 5267 -8.4; 5793 -10.8; 6373 -6.5; 7010 -2.4; 7711 -2.2; 8482 -2.5; 9330 -2.5; 10263 -4.2; 11289 -2.7; 12418 -2.5; 13660 -2.5; 15026 -2.5; 16529 -2.5; 18182 -2.5; 20000 -2.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Titan 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.34 | -4.2 dB |
| Peaking | 120 Hz  | 0.9  | -3.7 dB |
| Peaking | 227 Hz  | 1.51 | -2.2 dB |
| Peaking | 2049 Hz | 2.11 | -4.8 dB |
| Peaking | 5668 Hz | 5.26 | -9.0 dB |
| Peaking | 745 Hz  | 2.43 | 1.6 dB  |
| Peaking | 2725 Hz | 5.57 | -1.5 dB |
| Peaking | 3631 Hz | 3.28 | 4.7 dB  |
| Peaking | 4898 Hz | 0.71 | -1.7 dB |
| Peaking | 7344 Hz | 3.79 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%205/Dunu%20Titan%205.png)