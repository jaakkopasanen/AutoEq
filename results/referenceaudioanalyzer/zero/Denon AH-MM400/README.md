# Denon AH-MM400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.9; 25 -6.2; 28 -6.4; 31 -6.6; 34 -6.6; 37 -6.5; 41 -6.3; 45 -6.1; 49 -6.0; 54 -6.0; 60 -5.9; 66 -6.0; 72 -6.3; 79 -7.1; 87 -8.1; 96 -8.6; 106 -8.7; 116 -8.5; 128 -8.0; 141 -7.3; 155 -6.5; 170 -5.7; 187 -5.2; 206 -4.8; 227 -4.2; 249 -4.0; 274 -4.0; 302 -4.0; 332 -3.9; 365 -3.7; 402 -3.7; 442 -3.5; 486 -3.3; 535 -3.1; 588 -2.9; 647 -2.6; 712 -2.4; 783 -2.2; 861 -2.0; 947 -1.8; 1042 -1.5; 1146 -1.2; 1261 -0.8; 1387 -0.5; 1526 -0.8; 1678 -1.5; 1846 -2.4; 2031 -3.0; 2234 -2.8; 2457 -1.7; 2703 -1.8; 2973 -5.4; 3270 -8.3; 3597 -8.3; 3957 -6.1; 4353 -3.3; 4788 -2.3; 5267 -4.1; 5793 -6.3; 6373 -8.0; 7010 -7.8; 7711 -4.8; 8482 -3.8; 9330 -3.8; 10263 -3.8; 11289 -3.8; 12418 -3.8; 13660 -4.0; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-MM400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-MM400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.01 | -2.6 dB |
| Peaking | 108 Hz   | 1.28 | -4.9 dB |
| Peaking | 2248 Hz  | 0.32 | 2.9 dB  |
| Peaking | 3426 Hz  | 3.62 | -7.8 dB |
| Peaking | 6575 Hz  | 3.34 | -6.2 dB |
| Peaking | 1346 Hz  | 3.37 | 1.0 dB  |
| Peaking | 1595 Hz  | 2.96 | 0.7 dB  |
| Peaking | 2015 Hz  | 2.43 | -2.0 dB |
| Peaking | 2588 Hz  | 7.15 | 2.1 dB  |
| Peaking | 13076 Hz | 2.59 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-MM400/Denon%20AH-MM400.png)