# Beats Tour
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.0; 23 -16.3; 25 -16.6; 28 -16.9; 31 -17.0; 34 -17.1; 37 -17.1; 41 -17.0; 45 -16.9; 49 -16.7; 54 -16.4; 60 -16.0; 66 -15.6; 72 -15.1; 79 -14.6; 87 -14.0; 96 -13.4; 106 -12.8; 116 -12.2; 128 -11.6; 141 -10.8; 155 -10.1; 170 -9.4; 187 -8.7; 206 -8.0; 227 -7.4; 249 -6.7; 274 -6.1; 302 -5.4; 332 -4.8; 365 -4.1; 402 -3.6; 442 -3.1; 486 -2.5; 535 -2.1; 588 -1.7; 647 -1.3; 712 -0.9; 783 -0.7; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.7; 1261 -1.1; 1387 -1.7; 1526 -2.4; 1678 -3.2; 1846 -4.2; 2031 -6.2; 2234 -9.8; 2457 -12.9; 2703 -14.3; 2973 -14.4; 3270 -13.6; 3597 -12.0; 3957 -10.6; 4353 -11.9; 4788 -16.4; 5267 -17.8; 5793 -14.1; 6373 -4.4; 7010 -3.3; 7711 -5.6; 8482 -5.8; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Tour GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Tour ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 36 Hz   |  0.27 | -11.3 dB |
| Peaking | 1465 Hz |  0.29 | 7.5 dB   |
| Peaking | 2755 Hz |  1.5  | -14.3 dB |
| Peaking | 5309 Hz |  2.54 | -14.7 dB |
| Peaking | 6630 Hz |  4.97 | 8.7 dB   |
| Peaking | 1934 Hz |  6.12 | 0.8 dB   |
| Peaking | 2300 Hz |  8.22 | -1.0 dB  |
| Peaking | 4149 Hz | 10.17 | 1.4 dB   |
| Peaking | 4735 Hz | 12.93 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.7 dB |
| Peaking | 62 Hz    | 1.41 | -7.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -10.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beats%20Tour/Beats%20Tour.png)