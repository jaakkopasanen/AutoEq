# Klipsch Image X10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.6; 25 -13.8; 28 -13.9; 31 -14.0; 34 -14.0; 37 -14.0; 41 -14.0; 45 -14.0; 49 -14.0; 54 -14.0; 60 -14.0; 66 -13.9; 72 -13.8; 79 -13.7; 87 -13.6; 96 -13.4; 106 -13.3; 116 -13.1; 128 -12.9; 141 -12.7; 155 -12.4; 170 -12.2; 187 -11.9; 206 -11.6; 227 -11.3; 249 -10.9; 274 -10.5; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.1; 442 -8.6; 486 -8.1; 535 -7.7; 588 -7.2; 647 -6.7; 712 -6.2; 783 -5.8; 861 -5.3; 947 -4.9; 1042 -4.4; 1146 -4.0; 1261 -3.7; 1387 -3.4; 1526 -3.1; 1678 -3.0; 1846 -3.2; 2031 -3.5; 2234 -4.0; 2457 -5.0; 2703 -7.2; 2973 -10.2; 3270 -10.9; 3597 -8.2; 3957 -4.8; 4353 -2.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image X10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image X10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.34 | -4.5 dB |
| Peaking | 98 Hz   | 0.26 | -6.0 dB |
| Peaking | 1648 Hz | 0.66 | 4.0 dB  |
| Peaking | 3177 Hz | 3.2  | -8.2 dB |
| Peaking | 5208 Hz | 1.98 | 6.7 dB  |
| Peaking | 4538 Hz | 5.33 | 1.3 dB  |
| Peaking | 5193 Hz | 4.72 | -1.1 dB |
| Peaking | 6450 Hz | 4.04 | 3.7 dB  |
| Peaking | 7322 Hz | 1.74 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Klipsch%20Image%20X10/Klipsch%20Image%20X10.png)