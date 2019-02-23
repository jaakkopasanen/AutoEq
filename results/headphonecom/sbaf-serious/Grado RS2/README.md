# Grado RS2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.3; 60 -2.3; 66 -2.9; 72 -3.9; 79 -4.7; 87 -5.3; 96 -5.8; 106 -6.1; 116 -6.1; 128 -6.2; 141 -6.1; 155 -5.9; 170 -5.7; 187 -5.3; 206 -5.5; 227 -5.4; 249 -5.1; 274 -4.7; 302 -4.4; 332 -4.6; 365 -4.5; 402 -4.1; 442 -4.0; 486 -3.9; 535 -3.8; 588 -3.5; 647 -3.3; 712 -3.4; 783 -3.4; 861 -3.5; 947 -3.6; 1042 -3.8; 1146 -4.1; 1261 -4.4; 1387 -5.2; 1526 -6.3; 1678 -7.2; 1846 -8.7; 2031 -11.9; 2234 -11.7; 2457 -9.8; 2703 -8.1; 2973 -6.3; 3270 -4.9; 3597 -6.9; 3957 -12.1; 4353 -9.8; 4788 -7.3; 5267 -7.4; 5793 -7.6; 6373 -9.2; 7010 -10.7; 7711 -9.2; 8482 -10.3; 9330 -14.4; 10263 -13.0; 11289 -6.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.79 | 6.9 dB  |
| Peaking | 764 Hz   | 0.52 | 3.3 dB  |
| Peaking | 2112 Hz  | 3.42 | -7.3 dB |
| Peaking | 4080 Hz  | 7.18 | -5.7 dB |
| Peaking | 9433 Hz  | 2.98 | -8.3 dB |
| Peaking | 55 Hz    | 3.15 | 1.3 dB  |
| Peaking | 107 Hz   | 2    | -1.1 dB |
| Peaking | 3322 Hz  | 9.12 | 2.9 dB  |
| Peaking | 6792 Hz  | 6.94 | -3.3 dB |
| Peaking | 11697 Hz | 4.81 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS2/Grado%20RS2.png)