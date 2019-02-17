# Grado RS2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.7; 54 -1.8; 60 -3.1; 66 -4.0; 72 -4.9; 79 -6.0; 87 -6.9; 96 -7.7; 106 -8.1; 116 -8.3; 128 -8.5; 141 -8.5; 155 -8.3; 170 -8.1; 187 -7.8; 206 -7.9; 227 -7.8; 249 -7.6; 274 -7.2; 302 -6.9; 332 -6.7; 365 -7.0; 402 -6.7; 442 -6.4; 486 -6.6; 535 -6.5; 588 -6.2; 647 -6.0; 712 -6.2; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.4; 1387 -8.5; 1526 -10.0; 1678 -10.6; 1846 -12.5; 2031 -15.7; 2234 -13.5; 2457 -11.8; 2703 -10.9; 2973 -8.7; 3270 -7.7; 3597 -7.3; 3957 -11.6; 4353 -14.6; 4788 -15.5; 5267 -12.7; 5793 -12.9; 6373 -14.3; 7010 -15.9; 7711 -15.9; 8482 -17.2; 9330 -17.3; 10263 -11.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.3; 18182 -8.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 42 Hz    |  0.36 | 8.0 dB   |
| Peaking | 104 Hz   |  0.72 | -6.6 dB  |
| Peaking | 2052 Hz  |  2.91 | -8.6 dB  |
| Peaking | 4656 Hz  |  3.81 | -7.5 dB  |
| Peaking | 8111 Hz  |  1.83 | -11.2 dB |
| Peaking | 3481 Hz  | 10.67 | 2.4 dB   |
| Peaking | 6481 Hz  |  3.53 | -2.9 dB  |
| Peaking | 9456 Hz  |  4.32 | -8.7 dB  |
| Peaking | 9940 Hz  |  1.32 | 5.6 dB   |
| Peaking | 17863 Hz |  2.19 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB   |
| Peaking | 62 Hz    | 1.41 | 2.2 dB   |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.6 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS2/Grado%20RS2.png)