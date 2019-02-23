# Dunu Titan 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.8; 25 -6.8; 28 -6.9; 31 -6.9; 34 -7.0; 37 -7.1; 41 -7.1; 45 -7.1; 49 -7.2; 54 -7.3; 60 -7.4; 66 -7.6; 72 -7.7; 79 -7.9; 87 -8.1; 96 -8.2; 106 -8.2; 116 -8.1; 128 -8.2; 141 -8.0; 155 -7.8; 170 -7.6; 187 -7.3; 206 -7.0; 227 -6.6; 249 -6.2; 274 -5.8; 302 -5.3; 332 -4.8; 365 -4.3; 402 -4.0; 442 -3.6; 486 -2.7; 535 -2.7; 588 -2.2; 647 -1.7; 712 -1.8; 783 -1.5; 861 -1.8; 947 -2.2; 1042 -2.7; 1146 -3.2; 1261 -3.7; 1387 -4.5; 1526 -5.3; 1678 -6.0; 1846 -6.4; 2031 -6.6; 2234 -6.9; 2457 -6.6; 2703 -5.9; 2973 -4.2; 3270 -1.8; 3597 -0.5; 3957 -1.1; 4353 -3.7; 4788 -6.0; 5267 -8.4; 5793 -10.8; 6373 -6.5; 7010 -2.7; 7711 -4.4; 8482 -4.6; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Titan 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.31 | -2.1 dB |
| Peaking | 133 Hz  | 0.78 | -2.6 dB |
| Peaking | 686 Hz  | 1.45 | 3.6 dB  |
| Peaking | 3698 Hz | 5.39 | 5.1 dB  |
| Peaking | 5647 Hz | 5.99 | -7.0 dB |
| Peaking | 1076 Hz | 2.28 | 1.2 dB  |
| Peaking | 2179 Hz | 1.4  | -2.7 dB |
| Peaking | 3291 Hz | 5.22 | 2.2 dB  |
| Peaking | 6192 Hz | 8.68 | -1.5 dB |
| Peaking | 6945 Hz | 6.02 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%205/Dunu%20Titan%205.png)