# Grado RS2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.0; 72 -1.9; 79 -2.9; 87 -3.8; 96 -4.6; 106 -5.1; 116 -5.2; 128 -5.4; 141 -5.4; 155 -5.2; 170 -5.0; 187 -4.7; 206 -4.8; 227 -4.7; 249 -4.5; 274 -4.2; 302 -3.8; 332 -3.6; 365 -3.9; 402 -3.7; 442 -3.3; 486 -3.5; 535 -3.4; 588 -3.1; 647 -3.0; 712 -3.1; 783 -2.9; 861 -3.2; 947 -3.3; 1042 -3.4; 1146 -3.6; 1261 -4.3; 1387 -5.5; 1526 -6.9; 1678 -7.5; 1846 -9.4; 2031 -12.6; 2234 -10.4; 2457 -8.7; 2703 -7.8; 2973 -5.6; 3270 -4.6; 3597 -4.3; 3957 -8.5; 4353 -11.5; 4788 -12.4; 5267 -9.6; 5793 -9.8; 6373 -11.3; 7010 -12.8; 7711 -12.9; 8482 -14.2; 9330 -14.2; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.61 | 6.8 dB   |
| Peaking | 2038 Hz  | 2.02 | -9.7 dB  |
| Peaking | 2632 Hz  | 0.14 | 4.9 dB   |
| Peaking | 4570 Hz  | 4.23 | -7.8 dB  |
| Peaking | 8095 Hz  | 1.34 | -11.7 dB |
| Peaking | 65 Hz    | 3.77 | 1.7 dB   |
| Peaking | 110 Hz   | 2.26 | -0.9 dB  |
| Peaking | 3479 Hz  | 7.47 | 2.5 dB   |
| Peaking | 10052 Hz | 0.22 | -0.5 dB  |
| Peaking | 10971 Hz | 5.53 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB |
| Peaking | 16000 Hz | 1.41 | 1.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS2/Grado%20RS2.png)