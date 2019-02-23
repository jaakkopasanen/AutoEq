# Monoprice Monolith M1060
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.1; 25 -4.0; 28 -4.0; 31 -3.9; 34 -3.9; 37 -4.0; 41 -4.4; 45 -5.0; 49 -5.2; 54 -5.3; 60 -5.4; 66 -5.5; 72 -5.7; 79 -5.9; 87 -6.3; 96 -6.8; 106 -7.0; 116 -7.2; 128 -7.5; 141 -7.8; 155 -7.9; 170 -8.2; 187 -8.4; 206 -8.7; 227 -8.6; 249 -8.6; 274 -8.2; 302 -8.2; 332 -8.3; 365 -7.8; 402 -7.4; 442 -7.5; 486 -7.9; 535 -8.2; 588 -8.3; 647 -8.7; 712 -8.9; 783 -8.5; 861 -7.8; 947 -8.2; 1042 -8.0; 1146 -8.5; 1261 -8.8; 1387 -9.0; 1526 -9.9; 1678 -9.1; 1846 -6.9; 2031 -5.5; 2234 -5.0; 2457 -5.6; 2703 -5.4; 2973 -4.5; 3270 -5.0; 3597 -4.8; 3957 -5.4; 4353 -1.3; 4788 -3.0; 5267 -0.5; 5793 -1.0; 6373 -3.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.5; 20000 -15.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Monolith M1060 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Monolith M1060 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.59 | 2.7 dB  |
| Peaking | 208 Hz   | 0.88 | -2.1 dB |
| Peaking | 726 Hz   | 1.47 | -2.0 dB |
| Peaking | 1489 Hz  | 4.04 | -3.4 dB |
| Peaking | 5150 Hz  | 1.78 | 5.6 dB  |
| Peaking | 2050 Hz  | 1.47 | -1.4 dB |
| Peaking | 2139 Hz  | 3.28 | 2.9 dB  |
| Peaking | 2926 Hz  | 7.27 | 1.4 dB  |
| Peaking | 8259 Hz  | 4.83 | -1.2 dB |
| Peaking | 19833 Hz | 1.43 | -9.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monoprice%20Monolith%20M1060/Monoprice%20Monolith%20M1060.png)