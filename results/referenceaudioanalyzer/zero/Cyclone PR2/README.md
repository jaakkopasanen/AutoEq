# Cyclone PR2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -1.0; 116 -1.6; 128 -2.2; 141 -2.8; 155 -3.4; 170 -4.1; 187 -4.6; 206 -5.1; 227 -5.6; 249 -6.1; 274 -6.8; 302 -7.5; 332 -8.1; 365 -8.6; 402 -8.9; 442 -9.3; 486 -9.4; 535 -9.7; 588 -9.9; 647 -10.1; 712 -10.4; 783 -10.7; 861 -11.1; 947 -11.6; 1042 -12.3; 1146 -13.0; 1261 -13.2; 1387 -13.0; 1526 -13.1; 1678 -13.6; 1846 -13.6; 2031 -12.6; 2234 -11.0; 2457 -9.1; 2703 -7.2; 2973 -5.6; 3270 -4.4; 3597 -4.0; 3957 -4.6; 4353 -5.2; 4788 -4.6; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cyclone PR2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cyclone PR2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.17 | 6.6 dB  |
| Peaking | 328 Hz  | 0.59 | -4.2 dB |
| Peaking | 1882 Hz | 0.55 | -8.7 dB |
| Peaking | 3199 Hz | 1.45 | 7.9 dB  |
| Peaking | 5908 Hz | 2.97 | 7.4 dB  |
| Peaking | 16 Hz   | 1.07 | 1.1 dB  |
| Peaking | 53 Hz   | 0.47 | -0.4 dB |
| Peaking | 94 Hz   | 2.75 | 0.9 dB  |
| Peaking | 7818 Hz | 7.55 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | 4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Cyclone%20PR2/Cyclone%20PR2.png)