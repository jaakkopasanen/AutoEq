# Grado RS2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.2; 45 -2.1; 49 -2.9; 54 -3.6; 60 -4.3; 66 -4.6; 72 -4.7; 79 -4.7; 87 -4.7; 96 -4.7; 106 -4.5; 116 -4.3; 128 -4.1; 141 -3.9; 155 -3.7; 170 -3.6; 187 -3.3; 206 -3.1; 227 -3.2; 249 -3.3; 274 -3.2; 302 -3.1; 332 -3.1; 365 -3.1; 402 -2.9; 442 -2.7; 486 -2.9; 535 -3.1; 588 -3.1; 647 -3.1; 712 -3.1; 783 -3.2; 861 -3.2; 947 -3.3; 1042 -3.5; 1146 -3.9; 1261 -4.2; 1387 -4.6; 1526 -5.2; 1678 -5.9; 1846 -7.8; 2031 -10.2; 2234 -11.4; 2457 -11.5; 2703 -11.1; 2973 -10.2; 3270 -8.7; 3597 -7.2; 3957 -9.0; 4353 -14.8; 4788 -17.4; 5267 -17.3; 5793 -16.5; 6373 -15.8; 7010 -13.0; 7711 -8.1; 8482 -6.5; 9330 -7.8; 10263 -10.9; 11289 -12.5; 12418 -12.5; 13660 -10.2; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.93 | 6.5 dB   |
| Peaking | 1707 Hz  | 0.08 | 4.0 dB   |
| Peaking | 2305 Hz  | 2.06 | -7.8 dB  |
| Peaking | 5354 Hz  | 1.69 | -15.1 dB |
| Peaking | 12183 Hz | 1.97 | -8.4 dB  |
| Peaking | 3699 Hz  | 8.53 | 3.8 dB   |
| Peaking | 6415 Hz  | 0.44 | -0.7 dB  |
| Peaking | 6741 Hz  | 8.08 | -2.8 dB  |
| Peaking | 8237 Hz  | 4.63 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -6.2 dB |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20RS2/Grado%20RS2.png)