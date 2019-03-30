# Marantz MPH-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -2.0; 25 -3.3; 28 -5.1; 31 -6.7; 34 -8.0; 37 -9.0; 41 -10.0; 45 -10.8; 49 -11.4; 54 -12.1; 60 -12.6; 66 -12.9; 72 -13.0; 79 -12.9; 87 -12.6; 96 -12.3; 106 -12.3; 116 -12.2; 128 -12.0; 141 -11.9; 155 -11.6; 170 -11.4; 187 -10.8; 206 -10.0; 227 -9.3; 249 -8.8; 274 -8.4; 302 -8.1; 332 -8.1; 365 -8.1; 402 -8.2; 442 -8.4; 486 -8.4; 535 -8.7; 588 -8.7; 647 -8.4; 712 -8.4; 783 -8.1; 861 -8.0; 947 -7.8; 1042 -7.7; 1146 -7.4; 1261 -7.2; 1387 -6.7; 1526 -6.0; 1678 -5.7; 1846 -5.4; 2031 -5.2; 2234 -5.2; 2457 -5.1; 2703 -4.7; 2973 -3.7; 3270 -2.7; 3597 -1.4; 3957 -0.8; 4353 -0.8; 4788 -2.8; 5267 -7.4; 5793 -7.8; 6373 -7.7; 7010 -7.0; 7711 -6.5; 8482 -6.8; 9330 -6.8; 10263 -6.8; 11289 -6.8; 12418 -6.8; 13660 -6.8; 15026 -6.8; 16529 -6.8; 18182 -6.8; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Marantz MPH-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Marantz MPH-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.15 | 9.1 dB  |
| Peaking | 71 Hz   | 0.42 | -6.8 dB |
| Peaking | 689 Hz  | 1.41 | -1.5 dB |
| Peaking | 4370 Hz | 1.41 | 10.6 dB |
| Peaking | 5468 Hz | 1.89 | -8.0 dB |
| Peaking | 15 Hz   | 0.11 | 0.3 dB  |
| Peaking | 167 Hz  | 3.1  | -0.9 dB |
| Peaking | 279 Hz  | 2.72 | 0.7 dB  |
| Peaking | 1803 Hz | 5.21 | 0.7 dB  |
| Peaking | 7383 Hz | 7.13 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -6.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Marantz%20MPH-1/Marantz%20MPH-1.png)