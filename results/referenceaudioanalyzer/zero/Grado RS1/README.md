# Grado RS1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.3; 54 -2.3; 60 -3.1; 66 -3.6; 72 -3.9; 79 -4.1; 87 -4.2; 96 -4.2; 106 -4.2; 116 -4.0; 128 -3.8; 141 -3.8; 155 -3.5; 170 -3.5; 187 -3.5; 206 -3.2; 227 -3.2; 249 -3.2; 274 -3.2; 302 -3.1; 332 -3.0; 365 -3.1; 402 -3.3; 442 -3.5; 486 -3.5; 535 -3.5; 588 -3.5; 647 -3.5; 712 -3.5; 783 -3.5; 861 -3.5; 947 -3.8; 1042 -3.9; 1146 -4.2; 1261 -4.6; 1387 -5.0; 1526 -5.5; 1678 -8.0; 1846 -11.3; 2031 -12.9; 2234 -13.1; 2457 -13.3; 2703 -13.8; 2973 -13.9; 3270 -13.2; 3597 -11.3; 3957 -8.8; 4353 -7.7; 4788 -10.2; 5267 -13.5; 5793 -14.4; 6373 -13.0; 7010 -9.7; 7711 -6.6; 8482 -6.5; 9330 -6.5; 10263 -7.6; 11289 -8.4; 12418 -8.3; 13660 -6.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.71 | 6.4 dB  |
| Peaking | 503 Hz   | 0.25 | 3.5 dB  |
| Peaking | 1385 Hz  | 1.9  | 3.0 dB  |
| Peaking | 2377 Hz  | 1.12 | -9.6 dB |
| Peaking | 5840 Hz  | 3.93 | -7.6 dB |
| Peaking | 2438 Hz  | 5.62 | 2.1 dB  |
| Peaking | 3955 Hz  | 1.25 | -3.3 dB |
| Peaking | 4195 Hz  | 3.62 | 5.6 dB  |
| Peaking | 8230 Hz  | 3.31 | 2.0 dB  |
| Peaking | 11704 Hz | 3.33 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 2.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | -4.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20RS1/Grado%20RS1.png)