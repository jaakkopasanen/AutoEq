# Beats Studio 2 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.8; 25 -2.8; 28 -4.3; 31 -5.3; 34 -5.8; 37 -6.0; 41 -6.1; 45 -6.2; 49 -6.2; 54 -6.3; 60 -6.3; 66 -6.4; 72 -6.5; 79 -6.7; 87 -7.0; 96 -7.2; 106 -7.1; 116 -6.8; 128 -6.6; 141 -6.2; 155 -6.0; 170 -5.6; 187 -5.2; 206 -4.8; 227 -4.2; 249 -3.6; 274 -2.8; 302 -1.8; 332 -0.6; 365 -0.5; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.8; 647 -3.9; 712 -6.7; 783 -7.8; 861 -7.8; 947 -6.8; 1042 -6.5; 1146 -6.3; 1261 -6.8; 1387 -6.2; 1526 -5.5; 1678 -5.1; 1846 -3.7; 2031 -2.6; 2234 -1.8; 2457 -1.3; 2703 -1.6; 2973 -2.8; 3270 -5.6; 3597 -5.2; 3957 -3.1; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.7; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio 2 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio 2 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.55 | 5.6 dB  |
| Peaking | 465 Hz  | 0.98 | 7.5 dB  |
| Peaking | 798 Hz  | 2.04 | -4.9 dB |
| Peaking | 2384 Hz | 2.59 | 5.0 dB  |
| Peaking | 5275 Hz | 2.17 | 6.7 dB  |
| Peaking | 105 Hz  | 1.68 | -1.1 dB |
| Peaking | 319 Hz  | 5.98 | 1.1 dB  |
| Peaking | 3405 Hz | 8.31 | -2.3 dB |
| Peaking | 7083 Hz | 0.66 | 1.0 dB  |
| Peaking | 9294 Hz | 1.92 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 6.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Studio%202%202014/Beats%20Studio%202%202014.png)