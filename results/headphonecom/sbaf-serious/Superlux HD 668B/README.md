# Superlux HD 668B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.3; 45 -2.6; 49 -3.9; 54 -5.4; 60 -7.0; 66 -8.1; 72 -8.6; 79 -8.3; 87 -8.4; 96 -8.4; 106 -8.8; 116 -8.7; 128 -8.3; 141 -8.2; 155 -8.0; 170 -7.4; 187 -6.9; 206 -6.8; 227 -6.1; 249 -5.8; 274 -5.9; 302 -5.7; 332 -5.1; 365 -4.7; 402 -4.6; 442 -4.5; 486 -4.4; 535 -4.2; 588 -4.0; 647 -2.9; 712 -3.2; 783 -3.4; 861 -3.5; 947 -3.8; 1042 -3.9; 1146 -4.2; 1261 -4.6; 1387 -5.7; 1526 -7.3; 1678 -8.4; 1846 -9.6; 2031 -9.6; 2234 -8.9; 2457 -8.0; 2703 -7.1; 2973 -5.7; 3270 -4.5; 3597 -3.4; 3957 -3.6; 4353 -5.2; 4788 -5.8; 5267 -5.9; 5793 -13.3; 6373 -7.8; 7010 -7.5; 7711 -10.5; 8482 -12.8; 9330 -12.8; 10263 -9.6; 11289 -6.5; 12418 -6.5; 13660 -8.1; 15026 -9.7; 16529 -9.7; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 668B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 668B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-9.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 1.75 | 7.4 dB  |
| Peaking | 700 Hz   | 1.33 | 3.6 dB  |
| Peaking | 8730 Hz  | 2.94 | -7.0 dB |
| Peaking | 16078 Hz | 1.99 | -3.8 dB |
| Peaking | 22050 Hz | 1.99 | -1.7 dB |
| Peaking | 85 Hz    | 0.27 | 3.7 dB  |
| Peaking | 98 Hz    | 0.62 | -6.4 dB |
| Peaking | 2077 Hz  | 2.22 | -4.7 dB |
| Peaking | 3909 Hz  | 1.08 | 3.3 dB  |
| Peaking | 5700 Hz  | 9.8  | -9.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Superlux%20HD%20668B/Superlux%20HD%20668B.png)