# Superlux HD 668B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.5; 45 -2.7; 49 -3.9; 54 -5.2; 60 -6.4; 66 -7.0; 72 -7.0; 79 -7.2; 87 -7.8; 96 -8.8; 106 -8.6; 116 -7.9; 128 -8.0; 141 -8.0; 155 -7.5; 170 -7.0; 187 -6.8; 206 -6.5; 227 -5.8; 249 -6.0; 274 -5.8; 302 -5.6; 332 -5.3; 365 -4.7; 402 -4.5; 442 -4.0; 486 -3.9; 535 -3.9; 588 -3.3; 647 -2.7; 712 -3.0; 783 -2.9; 861 -3.0; 947 -3.0; 1042 -3.1; 1146 -3.4; 1261 -3.7; 1387 -4.6; 1526 -6.0; 1678 -7.5; 1846 -8.9; 2031 -9.5; 2234 -9.5; 2457 -9.1; 2703 -8.1; 2973 -7.1; 3270 -6.1; 3597 -5.0; 3957 -4.4; 4353 -4.3; 4788 -3.6; 5267 -6.9; 5793 -13.4; 6373 -8.9; 7010 -8.5; 7711 -11.3; 8482 -14.6; 9330 -14.5; 10263 -10.8; 11289 -7.2; 12418 -6.5; 13660 -6.8; 15026 -9.1; 16529 -8.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 668B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 1.62 | 7.3 dB   |
| Peaking | 1628 Hz  | 0.42 | 6.9 dB   |
| Peaking | 2050 Hz  | 1.28 | -9.9 dB  |
| Peaking | 8677 Hz  | 1.97 | -9.0 dB  |
| Peaking | 21187 Hz | 1.9  | -6.7 dB  |
| Peaking | 82 Hz    | 0.28 | 2.3 dB   |
| Peaking | 105 Hz   | 0.72 | -4.6 dB  |
| Peaking | 5130 Hz  | 3.05 | 5.6 dB   |
| Peaking | 5642 Hz  | 7.59 | -12.3 dB |
| Peaking | 15759 Hz | 4.35 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Superlux%20HD%20668B/Superlux%20HD%20668B.png)