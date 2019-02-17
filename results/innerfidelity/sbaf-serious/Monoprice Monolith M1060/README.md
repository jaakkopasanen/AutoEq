# Monoprice Monolith M1060
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.3; 25 -2.2; 28 -2.2; 31 -2.1; 34 -2.1; 37 -2.2; 41 -2.6; 45 -3.2; 49 -3.5; 54 -3.5; 60 -3.6; 66 -3.7; 72 -3.9; 79 -4.1; 87 -4.5; 96 -5.0; 106 -5.2; 116 -5.4; 128 -5.7; 141 -6.0; 155 -6.1; 170 -6.4; 187 -6.6; 206 -6.9; 227 -6.8; 249 -6.8; 274 -6.4; 302 -6.4; 332 -6.5; 365 -6.0; 402 -5.6; 442 -5.7; 486 -6.1; 535 -6.4; 588 -6.5; 647 -6.9; 712 -7.1; 783 -6.7; 861 -6.0; 947 -6.4; 1042 -6.2; 1146 -6.7; 1261 -7.0; 1387 -7.2; 1526 -8.1; 1678 -7.3; 1846 -5.1; 2031 -3.7; 2234 -3.2; 2457 -3.8; 2703 -3.6; 2973 -2.7; 3270 -3.2; 3597 -3.0; 3957 -3.6; 4353 -0.5; 4788 -1.2; 5267 -0.5; 5793 -0.5; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Monolith M1060 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Monolith M1060 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.49 | 4.5 dB  |
| Peaking | 1188 Hz | 0.84 | -0.8 dB |
| Peaking | 1569 Hz | 3.26 | -3.8 dB |
| Peaking | 2195 Hz | 0.9  | 3.6 dB  |
| Peaking | 5223 Hz | 1.98 | 5.9 dB  |
| Peaking | 214 Hz  | 2.41 | -0.8 dB |
| Peaking | 420 Hz  | 3.97 | 1.0 dB  |
| Peaking | 687 Hz  | 6.84 | -0.8 dB |
| Peaking | 6565 Hz | 4.27 | 2.6 dB  |
| Peaking | 7608 Hz | 2.01 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monoprice%20Monolith%20M1060/Monoprice%20Monolith%20M1060.png)