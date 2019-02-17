# Klipsch X10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.5; 25 -7.5; 28 -7.6; 31 -7.6; 34 -7.7; 37 -7.8; 41 -7.9; 45 -8.0; 49 -8.2; 54 -8.4; 60 -8.7; 66 -9.0; 72 -9.3; 79 -9.6; 87 -9.9; 96 -10.4; 106 -10.5; 116 -10.7; 128 -10.8; 141 -11.0; 155 -11.2; 170 -11.1; 187 -11.1; 206 -11.0; 227 -10.8; 249 -10.7; 274 -10.4; 302 -10.2; 332 -9.8; 365 -9.5; 402 -9.2; 442 -8.7; 486 -8.4; 535 -8.0; 588 -7.4; 647 -7.0; 712 -6.9; 783 -6.4; 861 -6.4; 947 -6.5; 1042 -6.6; 1146 -6.7; 1261 -6.8; 1387 -7.1; 1526 -7.3; 1678 -7.5; 1846 -7.1; 2031 -6.8; 2234 -6.6; 2457 -6.2; 2703 -6.6; 2973 -6.5; 3270 -4.0; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.0; 8482 -10.8; 9330 -8.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.19 | -0.7 dB |
| Peaking | 113 Hz  | 0.78 | -2.4 dB |
| Peaking | 242 Hz  | 0.71 | -3.3 dB |
| Peaking | 5098 Hz | 1.38 | 7.2 dB  |
| Peaking | 8544 Hz | 4.59 | -6.6 dB |
| Peaking | 810 Hz  | 2.52 | 1.0 dB  |
| Peaking | 3050 Hz | 0.11 | -0.1 dB |
| Peaking | 3407 Hz | 1.04 | -2.8 dB |
| Peaking | 3674 Hz | 3.6  | 5.3 dB  |
| Peaking | 6421 Hz | 5.91 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X10/Klipsch%20X10.png)