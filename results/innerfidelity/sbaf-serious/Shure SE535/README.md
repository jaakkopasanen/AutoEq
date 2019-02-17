# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.0; 25 -2.1; 28 -2.3; 31 -2.4; 34 -2.5; 37 -2.7; 41 -2.9; 45 -3.0; 49 -3.2; 54 -3.5; 60 -3.9; 66 -4.3; 72 -4.6; 79 -5.0; 87 -5.4; 96 -5.8; 106 -6.1; 116 -6.4; 128 -6.7; 141 -7.1; 155 -7.3; 170 -7.5; 187 -7.6; 206 -7.8; 227 -7.9; 249 -7.9; 274 -7.8; 302 -7.8; 332 -7.7; 365 -7.6; 402 -7.4; 442 -7.2; 486 -7.1; 535 -7.0; 588 -6.5; 647 -6.4; 712 -6.3; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -6.8; 1387 -7.2; 1526 -7.4; 1678 -7.4; 1846 -7.2; 2031 -6.9; 2234 -6.3; 2457 -4.4; 2703 -2.8; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.65 | 4.2 dB  |
| Peaking | 52 Hz   | 0.92 | 1.9 dB  |
| Peaking | 228 Hz  | 0.81 | -1.7 dB |
| Peaking | 1873 Hz | 1.79 | -3.1 dB |
| Peaking | 3972 Hz | 0.93 | 7.2 dB  |
| Peaking | 776 Hz  | 3.99 | 0.6 dB  |
| Peaking | 3083 Hz | 3.81 | 2.1 dB  |
| Peaking | 3589 Hz | 1.35 | -1.4 dB |
| Peaking | 6197 Hz | 2.42 | 5.0 dB  |
| Peaking | 7548 Hz | 1.55 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE535/Shure%20SE535.png)