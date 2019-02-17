# Grado RS1e Yellow Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.2; 45 -2.2; 49 -3.1; 54 -4.1; 60 -5.1; 66 -6.0; 72 -6.8; 79 -7.5; 87 -8.2; 96 -8.7; 106 -9.1; 116 -9.3; 128 -9.6; 141 -9.7; 155 -9.7; 170 -9.6; 187 -9.4; 206 -9.2; 227 -8.6; 249 -8.4; 274 -8.2; 302 -8.6; 332 -8.2; 365 -7.9; 402 -7.6; 442 -7.2; 486 -7.0; 535 -6.9; 588 -6.4; 647 -6.4; 712 -6.4; 783 -6.1; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.5; 1261 -6.6; 1387 -6.8; 1526 -6.0; 1678 -7.9; 1846 -14.0; 2031 -13.2; 2234 -10.4; 2457 -6.8; 2703 -3.9; 2973 -1.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e Yellow Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Yellow Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 33 Hz   |  0.49 | 7.7 dB   |
| Peaking | 87 Hz   |  0.63 | -4.4 dB  |
| Peaking | 181 Hz  |  0.78 | -1.8 dB  |
| Peaking | 1991 Hz |  3.73 | -10.5 dB |
| Peaking | 4014 Hz |  0.95 | 7.2 dB   |
| Peaking | 1618 Hz |  6.95 | 2.6 dB   |
| Peaking | 1794 Hz | 10.8  | -2.7 dB  |
| Peaking | 6310 Hz |  2.87 | 4.3 dB   |
| Peaking | 7478 Hz |  3.06 | -1.8 dB  |
| Peaking | 7485 Hz |  0.92 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Yellow%20Pads/Grado%20RS1e%20Yellow%20Pads.png)