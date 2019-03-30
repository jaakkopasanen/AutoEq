# Stax SR-40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.4; 41 -2.7; 45 -3.7; 49 -4.4; 54 -5.0; 60 -5.2; 66 -5.2; 72 -5.4; 79 -5.7; 87 -5.8; 96 -5.9; 106 -6.1; 116 -6.1; 128 -6.2; 141 -6.5; 155 -6.4; 170 -6.4; 187 -6.4; 206 -6.4; 227 -6.5; 249 -6.3; 274 -6.1; 302 -5.9; 332 -5.8; 365 -5.8; 402 -5.8; 442 -5.9; 486 -6.3; 535 -6.7; 588 -6.4; 647 -5.9; 712 -5.8; 783 -6.2; 861 -6.4; 947 -6.6; 1042 -7.2; 1146 -7.8; 1261 -7.8; 1387 -7.3; 1526 -7.1; 1678 -7.1; 1846 -6.9; 2031 -6.1; 2234 -4.7; 2457 -3.3; 2703 -2.4; 2973 -2.3; 3270 -2.9; 3597 -3.8; 3957 -5.2; 4353 -6.5; 4788 -7.1; 5267 -7.5; 5793 -8.6; 6373 -9.7; 7010 -10.4; 7711 -10.7; 8482 -10.6; 9330 -9.7; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.01 | 6.7 dB  |
| Peaking | 801 Hz   | 0.67 | 2.0 dB  |
| Peaking | 1361 Hz  | 0.6  | -3.0 dB |
| Peaking | 2854 Hz  | 1.65 | 5.9 dB  |
| Peaking | 7527 Hz  | 1.61 | -4.7 dB |
| Peaking | 365 Hz   | 3.15 | 0.5 dB  |
| Peaking | 541 Hz   | 7.33 | -0.8 dB |
| Peaking | 9470 Hz  | 3.76 | -1.6 dB |
| Peaking | 10896 Hz | 1.85 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Stax%20SR-40/Stax%20SR-40.png)