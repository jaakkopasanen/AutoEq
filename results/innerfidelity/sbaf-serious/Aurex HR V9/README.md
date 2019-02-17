# Aurex HR V9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.0; 54 -1.4; 60 -1.7; 66 -2.0; 72 -2.3; 79 -2.6; 87 -3.0; 96 -3.1; 106 -3.8; 116 -4.2; 128 -4.5; 141 -4.8; 155 -4.9; 170 -5.0; 187 -5.2; 206 -5.2; 227 -5.2; 249 -5.3; 274 -5.1; 302 -5.1; 332 -5.1; 365 -5.2; 402 -5.2; 442 -5.1; 486 -5.3; 535 -5.4; 588 -5.1; 647 -5.2; 712 -5.5; 783 -5.6; 861 -6.3; 947 -6.6; 1042 -6.4; 1146 -6.2; 1261 -5.4; 1387 -5.0; 1526 -4.3; 1678 -3.8; 1846 -3.6; 2031 -5.2; 2234 -6.4; 2457 -5.7; 2703 -4.7; 2973 -3.4; 3270 -2.7; 3597 -2.2; 3957 -2.2; 4353 -3.0; 4788 -2.8; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aurex HR V9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aurex HR V9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.36 | 6.2 dB  |
| Peaking | 439 Hz  | 0.96 | 1.2 dB  |
| Peaking | 1697 Hz | 3.92 | 2.7 dB  |
| Peaking | 3602 Hz | 2.38 | 4.0 dB  |
| Peaking | 5788 Hz | 3.07 | 6.1 dB  |
| Peaking | 993 Hz  | 3.86 | -1.0 dB |
| Peaking | 1878 Hz | 0.44 | 0.4 dB  |
| Peaking | 2263 Hz | 6.56 | -1.6 dB |
| Peaking | 6599 Hz | 7.23 | 2.3 dB  |
| Peaking | 7485 Hz | 1.92 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aurex%20HR%20V9/Aurex%20HR%20V9.png)