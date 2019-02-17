# Grado SR225i TTVJ Flat Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.3; 45 -2.5; 49 -3.6; 54 -4.7; 60 -5.8; 66 -6.6; 72 -7.2; 79 -7.5; 87 -8.1; 96 -8.4; 106 -8.7; 116 -8.8; 128 -9.0; 141 -9.0; 155 -9.0; 170 -8.9; 187 -8.8; 206 -8.8; 227 -8.4; 249 -8.1; 274 -7.9; 302 -7.9; 332 -8.0; 365 -7.9; 402 -7.7; 442 -7.4; 486 -7.3; 535 -7.2; 588 -6.7; 647 -6.6; 712 -6.6; 783 -6.3; 861 -6.6; 947 -6.4; 1042 -6.5; 1146 -6.5; 1261 -6.7; 1387 -7.1; 1526 -7.7; 1678 -7.6; 1846 -7.9; 2031 -11.3; 2234 -10.5; 2457 -6.7; 2703 -4.5; 2973 -3.0; 3270 -2.1; 3597 -3.0; 3957 -1.5; 4353 -0.5; 4788 -0.5; 5267 -1.5; 5793 -0.5; 6373 -1.6; 7010 -5.6; 7711 -7.7; 8482 -8.3; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i TTVJ Flat Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i TTVJ Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.62 | 9.2 dB  |
| Peaking | 81 Hz    | 0.36 | -4.5 dB |
| Peaking | 2106 Hz  | 4.03 | -7.1 dB |
| Peaking | 5372 Hz  | 0.78 | 7.9 dB  |
| Peaking | 8134 Hz  | 1.69 | -6.7 dB |
| Peaking | 1490 Hz  | 6.41 | -1.3 dB |
| Peaking | 2945 Hz  | 5.36 | 1.1 dB  |
| Peaking | 5761 Hz  | 2.48 | -1.3 dB |
| Peaking | 6091 Hz  | 6.36 | 2.6 dB  |
| Peaking | 14047 Hz | 1.94 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20TTVJ%20Flat%20Pads/Grado%20SR225i%20TTVJ%20Flat%20Pads.png)