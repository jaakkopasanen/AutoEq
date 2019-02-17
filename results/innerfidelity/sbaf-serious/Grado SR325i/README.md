# Grado SR325i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.2; 45 -2.1; 49 -3.0; 54 -4.0; 60 -5.1; 66 -6.1; 72 -6.8; 79 -7.5; 87 -8.2; 96 -8.7; 106 -8.9; 116 -9.0; 128 -9.0; 141 -8.9; 155 -8.9; 170 -8.6; 187 -8.3; 206 -8.0; 227 -7.7; 249 -7.6; 274 -7.3; 302 -7.3; 332 -7.2; 365 -6.9; 402 -6.7; 442 -6.2; 486 -6.5; 535 -6.6; 588 -6.2; 647 -6.1; 712 -6.2; 783 -6.1; 861 -6.3; 947 -6.5; 1042 -6.5; 1146 -6.7; 1261 -7.3; 1387 -8.3; 1526 -9.6; 1678 -10.3; 1846 -11.8; 2031 -15.3; 2234 -14.0; 2457 -11.7; 2703 -10.0; 2973 -7.6; 3270 -6.1; 3597 -5.7; 3957 -8.8; 4353 -15.0; 4788 -11.3; 5267 -8.3; 5793 -7.6; 6373 -7.8; 7010 -10.2; 7711 -11.7; 8482 -14.0; 9330 -16.9; 10263 -14.0; 11289 -7.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.55 | 7.1 dB   |
| Peaking | 101 Hz   | 0.74 | -4.4 dB  |
| Peaking | 2096 Hz  | 2.65 | -8.6 dB  |
| Peaking | 9084 Hz  | 2.52 | -10.4 dB |
| Peaking | 22050 Hz | 2.38 | -7.2 dB  |
| Peaking | 747 Hz   | 1.53 | 0.8 dB   |
| Peaking | 3665 Hz  | 3.68 | 5.2 dB   |
| Peaking | 4323 Hz  | 4.39 | -10.0 dB |
| Peaking | 5600 Hz  | 3.59 | 1.5 dB   |
| Peaking | 11833 Hz | 5.07 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325i/Grado%20SR325i.png)