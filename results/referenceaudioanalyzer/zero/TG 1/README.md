# TG 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.7; 155 -2.1; 170 -3.4; 187 -4.7; 206 -5.7; 227 -6.5; 249 -7.2; 274 -8.0; 302 -9.0; 332 -10.1; 365 -11.3; 402 -12.5; 442 -13.6; 486 -14.8; 535 -16.1; 588 -17.4; 647 -18.9; 712 -20.8; 783 -22.8; 861 -24.9; 947 -26.5; 1042 -27.2; 1146 -27.0; 1261 -26.3; 1387 -25.0; 1526 -22.8; 1678 -20.2; 1846 -17.3; 2031 -14.6; 2234 -11.9; 2457 -10.4; 2703 -9.1; 2973 -6.9; 3270 -4.1; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TG 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TG 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.42 | 5.4 dB   |
| Peaking | 123 Hz  | 0.6  | 6.1 dB   |
| Peaking | 1108 Hz | 0.66 | -22.6 dB |
| Peaking | 3765 Hz | 1.23 | 11.6 dB  |
| Peaking | 5833 Hz | 3.01 | 4.8 dB   |
| Peaking | 344 Hz  | 3.11 | 0.4 dB   |
| Peaking | 1527 Hz | 5.1  | -1.4 dB  |
| Peaking | 2245 Hz | 3.17 | 1.6 dB   |
| Peaking | 2897 Hz | 5.28 | -1.3 dB  |
| Peaking | 8084 Hz | 5.18 | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.3 dB   |
| Peaking | 125 Hz   | 1.41 | 6.0 dB   |
| Peaking | 250 Hz   | 1.41 | 0.3 dB   |
| Peaking | 500 Hz   | 1.41 | -3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -22.9 dB |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 10.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/TG%201/TG%201.png)