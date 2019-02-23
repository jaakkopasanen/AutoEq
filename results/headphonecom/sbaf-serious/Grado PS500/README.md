# Grado PS500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.3; 31 -2.2; 34 -3.2; 37 -4.1; 41 -5.1; 45 -6.1; 49 -7.0; 54 -8.1; 60 -9.1; 66 -10.0; 72 -10.6; 79 -11.0; 87 -11.3; 96 -11.7; 106 -11.7; 116 -11.6; 128 -11.4; 141 -11.1; 155 -10.8; 170 -10.4; 187 -10.1; 206 -9.8; 227 -9.4; 249 -9.0; 274 -8.6; 302 -8.1; 332 -7.7; 365 -7.3; 402 -6.9; 442 -6.9; 486 -6.5; 535 -6.3; 588 -6.1; 647 -6.0; 712 -6.2; 783 -6.2; 861 -6.5; 947 -6.8; 1042 -7.2; 1146 -7.6; 1261 -8.3; 1387 -9.4; 1526 -10.6; 1678 -10.6; 1846 -9.8; 2031 -11.9; 2234 -10.2; 2457 -6.5; 2703 -3.9; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -3.3; 4353 -2.5; 4788 -0.7; 5267 -0.5; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.1; 9330 -11.1; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.9  | 7.0 dB  |
| Peaking | 101 Hz   | 0.64 | -5.9 dB |
| Peaking | 2034 Hz  | 1.61 | -6.9 dB |
| Peaking | 3104 Hz  | 2.03 | 8.2 dB  |
| Peaking | 5486 Hz  | 2.8  | 5.9 dB  |
| Peaking | 659 Hz   | 1.53 | 1.1 dB  |
| Peaking | 1475 Hz  | 6.88 | -1.5 dB |
| Peaking | 6539 Hz  | 9.23 | 2.5 dB  |
| Peaking | 9531 Hz  | 4.49 | -6.0 dB |
| Peaking | 10888 Hz | 3.22 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS500/Grado%20PS500.png)